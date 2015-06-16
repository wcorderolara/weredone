from django.db import models
from apps.bases.models import *
from apps.usuarios.models import *


class Proyecto(models.Model):
	idAdministrador = models.ForeignKey(Usuario)
	nombreProyecto = models.CharField(max_length=100)
	Descripcion = models.TextField(max_length=500)
	porcentajeAvance = models.DecimalField(max_digits=3,decimal_places=2, blank=True)
	fechaCreacion = models.DateField(auto_now_add=True)
	idEstadoProyecto = models.ForeignKey(EstadosGenerales)
	Status = models.BooleanField(default=True)

	class Meta:
		db_table = 'proyectos'

class miembroProyecto(models.Model):
	idProyecto = models.ForeignKey(Proyecto)
	idUsuario = models.ForeignKey(Usuario)
	isAdmin = models.BooleanField(default=False)
	fechaIngreso = models.DateField(auto_now_add = True)
	Status = models.BooleanField(default=True)

	class Meta:
		db_table = 'miembro_proyecto'

class objetivoProyecto(models.Model):
	idProyecto = models.ForeignKey(Proyecto)
	idClaseObjetivo = models.ForeignKey(ClaseObjetivo)
	idTipoObjetivo = models.ForeignKey(TipoObjetivo)
	idNivelPrioridad = models.ForeignKey(nivelPrioridad)
	tituloObjetivo = models.CharField(max_length=250)
	Descripcion = models.TextField(max_length=1000)
	progresoObjetivo = models.DecimalField(max_digits=3, decimal_places=2, blank=True)
	usuarioCreacion = models.ForeignKey(Usuario)
	fechaEntrega = models.DateField(blank=False)
	fechaCreacion = models.DateField(auto_now_add=True)
	idEstadoObjetivo = models.ForeignKey(EstadosGenerales)
	calificacionObjetivo = models.PositiveSmallIntegerField(blank=True)
	Status = models.BooleanField(default=True)

	class Meta:
		db_table = 'objetivo_proyecto'

class tagObjetivoProyecto(models.Model):
	idObjetivoProyecto = models.ForeignKey(objetivoProyecto)
	Descripcion = models.CharField(max_length=50)
	colorTag = models.CharField(max_length=6)
	Status = models.BooleanField(default=True)

	class Meta:
		db_table = 'tag_objetivo_proyecto'

class tareaObjetivo(models.Model):
	idObjetivoProyecto = models.ForeignKey(objetivoProyecto)
	usuarioCreacion = models.ForeignKey(Usuario)
	idNivelPrioridad = models.ForeignKey(nivelPrioridad)
	tareaObjetvio = models.CharField(max_length=250)
	Descripcion = models.TextField(max_length=1000)
	progresoTarea = models.DecimalField(max_digits=3, decimal_places=2, blank=True)
	fechaEntrega = models.DateField(blank=False)
	fechaCreacion = models.DateField(auto_now_add=True)
	idEstadoTarea = models.ForeignKey(EstadosGenerales)
	Status = models.BooleanField(default=True)

	class Meta:
		db_table = 'tarea_objetivo'

class archivoTarea(models.Model):
	idTareaObjetivo = models.ForeignKey(tareaObjetivo)
	archivoTarea = models.FileField(upload_to='files/')		
	Status = models.BooleanField(default=True)

	class Meta:
		db_table = 'archivo_tarea_objetivo'


class tareasMiembroProyecto(models.Model):
	idTareaObjetivo = models.ForeignKey(tareaObjetivo)
	idMiembroProyecto = models.ForeignKey(miembroProyecto)
	Status = models.BooleanField(default=True)

	class Meta:
		db_table = 'tareas_miembro_proyecto'