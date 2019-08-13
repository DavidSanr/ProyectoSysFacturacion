from django.db import models

# Create your models here.
from django.contrib.auth.models import  User




class ClaseModelo(models.Model):
    estado = models.BooleanField(default= True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE,related_name='usuarioCreador')
    usuario_modificador = models.ForeignKey(User,related_name='usuarioModificador',blank = True,null=True,on_delete=models.CASCADE)

    class Meta:
        abstract = True
    
    