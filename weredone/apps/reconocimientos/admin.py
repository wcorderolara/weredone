from django.contrib import admin
from .models import TipoReconocimiento, ReconocimientoUsuario


@admin.register(TipoReconocimiento, ReconocimientoUsuario)
class TipoReconocimientoAdmin(admin.ModelAdmin):
    pass


class ReconocimientoUsuariosAdmin(admin.ModelAdmin):
    pass
