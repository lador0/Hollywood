from django.db import models

class Actor(models.Model):
    actor_id = models.IntegerField(verbose_name="ID актера", unique=False)
    name = models.CharField(max_length=100, verbose_name="Имя актера")

    def __str__(self):
        return self.name
    
class Writer(models.Model):
    writer_id = models.CharField(max_length=200, verbose_name="ID сценариста", unique=False)
    name = models.CharField(max_length=100, verbose_name="Имя сценариста")

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    movie_id = models.CharField(max_length=200, verbose_name="ID фильма", unique=False)
    title = models.CharField(max_length=200, verbose_name="Название фильма")
    imdb_rating = models.FloatField(verbose_name="Рейтинг фильма")
    genre = models.TextField(verbose_name="Жанры")
    description = models.TextField(verbose_name="Описание фильма")
    writer = models.CharField(max_length=200, verbose_name="Имя сценариста",null=True)
    writers = models.ManyToManyField(Writer, verbose_name="ID сценариста", blank=True)
    writers_names = models.TextField(verbose_name="Имя сценариста")
    director = models.CharField(max_length=100, verbose_name="Режиссер")
    actors = models.ManyToManyField(Actor, verbose_name="ID актера", blank=True)
    actors_names = models.TextField(verbose_name="Список имен, разделенных запятыми")
    
    def __str__(self):
        return self.title
