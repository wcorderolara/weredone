from django.db import models
from apps.bases.models import *
from apps.usuarios.models import *

class TipoInconveniente(models.Model):
	Descripcion = models.CharField(max_length=75)
	Status = models.BooleanField(default=True)

	class Meta:
		db_table = 'tipo_inconveniente'

	def __unicode__(self):
		return self.Descripcion

class Inconveniente(models.Model):
	idTipoObjeto = models.ForeignKey(TipoObjeto)
	idTipoInconveniente = models.ForeignKey(TipoInconveniente)
	idUsuarioReporta = models.ForeignKey(Usuario)
	Descripcion = models.TextField(max_length=500)
	FechaReporte = models.DateField(auto_now_add=True)
	FechaSolucion = models.DateField(blank=True)
	idEstadoGeneral = models.ForeignKey(EstadosGenerales)
	Status = models.BooleanField(default=True)

	class Meta:
		db_table = 'inconvenientes'

	def __unicode__(self):
		return self.Descripcion
