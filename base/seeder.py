from .models import Author, Genre

def seeder_func():
    authors = ['Albert Kamiu','Vaja Pshavelasa','Ilia chavchavadze','Iakob Gogebashvili']
    genres = ['Comedy', 'Drama','Melodrama','Distoric']

    for author in authors:
        if not Author.objects.filter(name=author).exists():
            new_author = Author(name=author)
            new_author.save()

    for genre in genres:
        if not Author.objects.filter(name=genre).exists():
            new_genre = Genre(name=genre)
            new_genre.save()

