from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User, Genre, Author, Comment,Travel
from django.db.models import Q
from  django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, UserForm,TravelForm
from .seeder import seeder_func
from django.contrib import messages
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    travels = Travel.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(autor__name__icontains=q) | Q(genre__name__icontains=q))
    travels = list(dict.fromkeys(travels))
    heading ="Online Library"
    genres = Genre.objects.all()
    context = {"travels": travels, "heading": heading, 'genres': genres}
    return render(request, 'base/home.html', context)

def about(request):
    return render(request, 'base/about.html')

def profile(request, pk):
    user = User.objects.get(id=pk)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    travels = user.travels.filter(Q(name__icontains=q)
                                  | Q(description__icontains=q) | Q(autor__name__icontains=q) | Q(genre__name__icontains=q))
    travels = list(dict.fromkeys(travels))
    heading = "My Library"
    genres = Genre.objects.all()

    context = {"travels": travels, "heading": heading, 'genres': genres}
    return render(request, 'base/profile.html', context)
def adding(request,id):
    user = request.user
    travel=Travel.objects.get(id=id)
    user.travels.add(travel)
    return redirect('profile',request.user.id)
@login_required(login_url='login')
def delete(request,id):
    obj = Travel.objects.get(id=id)
    if request.method=="POST":
        request.user.travels.remove(obj)
        return redirect('profile',request.user.id)

    return render(request, 'base/delete.html', {'obj': obj})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profile', request.user.id)

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist!')
            return render(request, 'base/login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            messages.error(request, 'User or password is not correct!')

    return render(request, 'base/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')
def register_user(request):
    form = MyUserCreationForm
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('profile', user.id)
        else:
            messages.error(request, 'Follow the Instruction and create proper user and password ')

    context = {'form': form}
    return render(request, 'base/register.html', context)

def reading(request, id):
    travel = Travel.objects.get(id=id)
    travel_comments = Comment.objects.filter(travel=travel)

    if request.method == 'POST':
        Comment.objects.create(
            user=request.user,
            travel=travel,
            body=request.POST.get('body')
        )
        return redirect('reading', id=id)  # Redirect to the same page to avoid resubmission

    return render(request, 'base/reading.html', {'travel': travel, 'comments': travel_comments})

@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method=='POST':
        form=UserForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile',user.id)

    context = {'form':form}
    return render(request, 'base/update_user.html',context)
def delete_comment(request, id):
    comment=Comment.objects.get(id=id)
    travel=comment.travel
    if request.method=='POST':
        comment.delete()
        return redirect('reading',travel.id)
    return render(request, 'base/delete.html',{'obj':comment})

def add_travel(request):
    authors = Author.objects.all()
    genres = Genre.objects.all()
    form = TravelForm()

    if request.method == 'POST':
        travel_author = request.POST.get('author')
        travel_genre = request.POST.get('genre')

        author, created = Author.objects.get_or_create(name=travel_author)
        genre, created = Genre.objects.get_or_create(name=travel_genre)

        form = TravelForm(request.POST)

        new_travel= Travel(
            picture=request.FILES['picture'],
            name=form.data['name'],
            autor=author,  # Update 'author' to 'autor'
            description=form.data['description'],
            file=request.FILES['file'],
            creator=request.user)
        if not (Travel.objects.filter(file = request.FILES['file']) or Travel.objects.filter(name = new_travel.name)):
            new_travel.save()
            new_travel.genre.add(genre)
        else:
            messages.error(request, 'ფაილი იგივე სახელით უკვე არსებობს ბაზაში!')

        return redirect('home')

    context = {'form': form, 'authors': authors, 'genres': genres}
    return render(request,'base/add_travel.html',context)
def delete_travel(request, id):
    obj = Travel.objects.get(id=id)
    if request.method == 'POST':
        obj.picture.delete()
        obj.file.delete()
        obj.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj': obj })