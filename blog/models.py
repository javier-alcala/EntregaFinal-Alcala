from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    edad = models.IntegerField()
    biografia = models.TextField()
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f'Usuario: {self.usuario} - Edad: {self.edad}'


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete= models.CASCADE)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fechaDeCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.titulo}" por {self.autor}'


class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fechaDeCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor} en "{self.post.titulo}"'