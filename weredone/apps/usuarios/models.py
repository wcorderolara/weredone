from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TipoUsuario(models.Model):
  Descripcion = models.CharField(max_length=100)
  Status = models.BooleanField(default=True)

  def __unicode__(self):
    return self.Descripcion


class Usuario(models.Model):
  idUsuario = models.ForeignKey(User)
  idTipoUsuario = models.ForeignKey(TipoUsuario)
  Nombre = models.CharField(max_length=100)
  Email = models.EmailField(max_length=200, blank=False, unique=True)
  Password = models.CharField(max_length=250, blank=False, unique=True)
  Avatar = models.CharField(max_length=100, blank=True)
  FechaCreacion = models.DateField()
  UltimaVisita = models.DateField()
  Status = models.BooleanField(default=True)

  def __unicode__(self):
    return self.Nombre
