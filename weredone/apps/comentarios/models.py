from django.db import models
from apps.bases.models import *
from apps.usuarios.models import *

class TipoComentario(models.Model):
	Descripcion = models.CharField(max_length=75)
	Status = models.BooleanField(default = True)
	
	class Meta:
		db_table = 'tipo_comentario'

	def __unicode__(self):
		return self.Descripcion

class Comentarios(models.Model):
	idComentarioPadre = models.ForeignKey('self')
	idTipoComentario = models.ForeignKey(TipoComentario)
	idTipoObjeto = models.ForeignKey(TipoObjetivo)
	idUsuarioComenta = models.ForeignKey(Usuario)
	Comentario = models.CharField(max_length=200)
	Status = models.BooleanField(default = True)

	class Meta:
		db_table = 'comentarios'

	def __unicode__(self):
		return self.Comentario



