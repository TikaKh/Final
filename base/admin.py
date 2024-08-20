from django.contrib import admin
from .models import Author, User, Genre, Comment, Travel
admin.site.register(Travel)
admin.site.register(Author)
admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Comment)