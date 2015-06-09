from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.
class TipoReconocimiento(models.Model):
  Descripcion = models.CharField(max_length=100)
  Status = models.BooleanField(default=True)

  class Meta:
    db_table = 'tipo_reconocimiento'

  def __unicode__(self):
    return "%s" % (self.Descripcion)


class ReconocimientoUsuario(models.Model):
  idUsuario = models.ForeignKey(Usuario)
  idReconocimiento = models.ForeignKey(TipoReconocimiento)
  Descripcion = models.CharField(max_length=140)
  Status = models.BooleanField(default=True)

  class Meta:
    db_table = 'reconocimientos_usuario'

  def __unicode__(self):
    return self.Descripcion
