from datetime import date
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"
    

class Actor(models.Model):
    name = models.CharField('Актер', max_length=100)
    age = models.PositiveSmallIntegerField("Возраса", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")
    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Актеры и режисеры"
        verbose_name_plural = "Актеры и режисеры"
        
    
class Genre(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        
    
class Moovie(models.Model):
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default="")
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="moovies/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=0)
    country = models.CharField("Страна", max_length=100)
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actors")
    genre = models.ManyToManyField(Genre, verbose_name="жанры")
    primier = models.DateField("Примьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="Указывать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField("Сборы в США", default=0, help_text="Указывать сумму в долларах")
    fees_in_world = models.PositiveIntegerField("Сборы в Мире", default=0, help_text="Указывать сумму в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})
    
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        

class MoovieShoots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Moovie, verbose_name="Фильм", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"
        

class RaitingStar(models.Model):
    value = models.PositiveSmallIntegerField("Значение", default=0)
    
    def __str__(self):
        return self.value
    
    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        
class Raiting(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RaitingStar, verbose_name="звезда", on_delete=models.CASCADE)
    movie = models.ForeignKey(Moovie, verbose_name="фильм", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.star} - {self.movie}"
    
    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
    
    
class Revievs(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, null=True)
    moovie = models.ForeignKey(Moovie, verbose_name="фильм", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.name} - {self.movie}"
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    