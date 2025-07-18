from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete= models.CASCADE)
    contenido = models.TextField()
    fechaDeCreacion = models.DateTimeField(auto_now_add=True)

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete= models.CASCADE)
    contenido = models.TextField()
    fechaDeCreacion = models.DateTimeField(auto_now_add=True)