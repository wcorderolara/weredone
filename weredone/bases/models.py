from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
  Description = models.CharField(max_length=100)
  Status = models.BooleanField(default=True)

  def __unicode__(self):
		return "%s" % (self.Description)

class TipoObjeto(models.Model):
  Description = models.CharField(max_length=100)
  Status = models.BooleanField(default=True)

  def __unicode__(self):
		return "%s" % (self.Description)

class TipoObjetivo(models.Model):
  Description = models.CharField(max_length=25)
  Status = models.BooleanField(default=True)

  def __unicode__(self):
		return "%s" % (self.Description)

class TipoComentario(models.Model):
  Description = models.CharField(max_length=25)
  Status = models.BooleanField(default=True)

  def __unicode__(self):
		return "%s" % (self.Description)

class TipoInconveniente(models.Model):
  Description = models.CharField(max_length=25)
  Status = models.BooleanField(default=True)

  def __unicode__(self):
		return "%s" % (self.Description)