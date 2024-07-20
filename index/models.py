from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    año = models.IntegerField()
    director = models.CharField(max_length=255)
    poster = models.URLField()

    def __str__(self):  
        return self.titulo
