from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Moovie
from .serialazers import MoovieSerialazer
from django.http import JsonResponse
import json

class MoovieViewSet(viewsets.ModelViewSet):
    queryset = Moovie.objects.all()
    serializer_class = MoovieSerialazer

class MooviesView(ListView):
    def get(self, request):
        movies = Moovie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})


class MovieDetailView(DetailView):
    def get(self, request, slug):
        movie = Moovie.objects.get(url=slug)
        return render(request, "movies/movie_detail.html", {"movie": movie})

def movie_detail_json(request, movie_id):
    movie = get_object_or_404(Moovie, id=movie_id)
    movie_json = {
        'title': movie.title,
        'tagline': movie.tagline,
        'description': movie.description,
        'year': movie.year,
        # Другие поля фильма, которые вам нужны
    }
    return JsonResponse(movie_json)
