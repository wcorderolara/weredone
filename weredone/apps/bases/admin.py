from django.contrib import admin
from .models import TipoObjeto, TipoObjetivo, ClaseObjetivo, EstadosGenerale, Tags


@admin.register(TipoObjeto, TipoObjetivo, ClaseObjetivo, EstadosGenerale, Tags)
class TipoObjetoAdmin(admin.ModelAdmin):
    pass


class TipoObjetivoAdmin(admin.ModelAdmin):
    pass


class ClaseObjetivoAdmin(admin.ModelAdmin):
    pass


class EstadosGeneralesAdmin(admin.ModelAdmin):
    pass


class TagsAdmin(admin.ModelAdmin):
    pass
