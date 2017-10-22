from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    
    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()
        
    def __str__(self):    
        return self.titulo

        
class Commentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.CharField(max_length=50)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)


