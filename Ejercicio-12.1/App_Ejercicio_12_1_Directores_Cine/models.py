from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Genre of the movie")

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=32)
    summary = models.TextField(max_length=550, help_text="summary of the movie")
    genre_of_movie = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField('died', null=True, blank=True)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)