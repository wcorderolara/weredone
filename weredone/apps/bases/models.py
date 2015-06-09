from django.db import models
# class TipoUsuario(models.Model):
#   Description = models.CharField(max_length=100)
#   Status = models.BooleanField(default=True)

#   def __unicode__(self):
# 		return "%s" % (self.Description)


class TipoObjeto(models.Model):
  Descripcion = models.CharField(max_length=100)
  Status = models.BooleanField(default=True)

  class Meta:
    db_table = 'tipo_objeto'

  def __unicode__(self):
    return "%s" % (self.Descripcion)


class TipoObjetivo(models.Model):
  Descripcion = models.CharField(max_length=25)
  Status = models.BooleanField(default=True)

  class Meta:
    db_table = 'tipo_objetivo'

  def __unicode__(self):
    return "%s" % (self.Descripcion)


class ClaseObjetivo(models.Model):
  Descripcion = models.CharField(max_length=25)
  Status = models.BooleanField(default=True)

  class Meta:
    db_table = 'clase_objetivo'

  def __unicode__(self):
    return "%s" % (self.Descripcion)


class EstadosGenerales(models.Model):
    idTipoObjeto = models.ForeignKey(TipoObjeto)
    Descripcion = models.CharField(max_length=25)
    Status = models.BooleanField(default=True)

    class Meta:
      db_table = 'estados_generales'

    def __unicode__(self):
      return self.Descripcion

class Tags(models.Model):
  idTipoObjeto = models.ForeignKey(TipoObjeto)
  Descripcion = models.CharField(max_length=50)
  ColorTag = models.CharField(max_length=7)
  Status = models.BooleanField(default=True)

  class Meta:
    db_table = 'tags'

  def __unicode__(self):
    return self.Description



# class TipoComentario(models.Model):
#   Description = models.CharField(max_length=25)
#   Status = models.BooleanField(default=True)

#   def __unicode__(self):
#     return "%s" % (self.Description)


# class TipoInconveniente(models.Model):
#   Description = models.CharField(max_length=25)
#   Status = models.BooleanField(default=True)

#   def __unicode__(self):
# 		return "%s" % (self.Description)