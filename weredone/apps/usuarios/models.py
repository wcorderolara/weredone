from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TipoUsuario(models.Model):
  Descripcion = models.CharField(max_length=100)
  Status = models.BooleanField(default=True)

  class Meta:
    db_table = 'tipo_usuario'

  def __unicode__(self):
    return self.Descripcion


class Usuario(models.Model):
  idUsuario = models.ForeignKey('self')
  idTipoUsuario = models.ForeignKey(TipoUsuario)
  Nombre = models.CharField(max_length=100)
  Email = models.EmailField(max_length=200, blank=False, unique=True)
  Password = models.CharField(max_length=250, blank=False, unique=True)
  Avatar = models.CharField(max_length=100, blank=True)
  FechaCreacion = models.DateField(auto_now_add=True)
  UltimaVisita = models.DateField(auto_now_add=True)
  Status = models.BooleanField(default=True)

  class Meta:
    db_table = 'usuarios'

  def __unicode__(self):
    return self.Nombre
