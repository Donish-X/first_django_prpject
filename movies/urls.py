from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

from . import views



urlpatterns = [
    path('', views.MooviesView.as_view()),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name='movie_detail'),
    path('movie_detail_json/<int:movie_id>/', views.movie_detail_json, name='movie_detail_json'),
]
