from django.contrib import admin
from .models import Category, Actor, Genre, Moovie, MoovieShoots, Raiting, RaitingStar, Revievs

# Register your models here.

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Moovie)
admin.site.register(MoovieShoots)
admin.site.register(Raiting)
admin.site.register(RaitingStar)
admin.site.register(Revievs)


