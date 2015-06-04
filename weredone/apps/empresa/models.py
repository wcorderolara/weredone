from django.db import models

# Create your models here.


class Empresa(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(blank=False)

    def __unicode__(self):
        return "%s" % (self.Name)
