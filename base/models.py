from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)
    Desc = models.CharField(max_length=300, default="No Description")

    def __str__(self):
        return  self.name
class Travel(models.Model):
    creator = models.ForeignKey('User', on_delete=models.SET("Unknown Creator"), related_name='created_travels')
    picture = models.ImageField(null=True, blank=True)
    file = models.FileField(null=True)
    name = models.CharField(max_length=100)
    autor = models.ForeignKey(Author, on_delete=models.SET("Unknown Author"))
    genre = models.ManyToManyField(Genre, related_name='travels',blank=True)
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name", "created"]

    def __str__(self):
        return f"{self.name} _ {self.autor}"

class User(AbstractUser):
    travels = models.ManyToManyField(Travel, related_name='users',blank=True)
    avatar = models.ImageField(null=True, default='avatar.svg')
    bio = models.TextField(null=True)

class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    travel = models.ForeignKey('Travel', on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body
