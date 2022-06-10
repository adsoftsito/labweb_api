from django.db import models

# Create your models here.
class Movie(models.Model):
    movieId = models.IntegerField()
    title  = models.TextField(blank=True)
    genres = models.TextField(blank=True)

class Rating(models.Model):
    userId = models.IntegerField()
    movieId = models.IntegerField()
    rating = models.FloatField()
    timestamp = models.BigIntegerField(default=0)
