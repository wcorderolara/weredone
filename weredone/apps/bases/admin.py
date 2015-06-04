from django.contrib import admin
from .models import TipoUsuario, TipoObjeto, TipoObjetivo, TipoComentario, TipoInconveniente


@admin.register(TipoUsuario, TipoObjeto, TipoObjetivo, TipoComentario, TipoInconveniente)
class TipoUsuarioAdmin(admin.ModelAdmin):
    pass


class TipoObjetoAdmin(admin.ModelAdmin):
    pass


class TipoObjetivoAdmin(admin.ModelAdmin):
    pass


class TipoComentarioAdmin(admin.ModelAdmin):
    pass


class TipoInconvenienteAdmin(admin.ModelAdmin):
    pass
