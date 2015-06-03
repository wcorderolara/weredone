from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
  Desciption = models.CharField(max_length=100)
  Status = models.BooleanField
