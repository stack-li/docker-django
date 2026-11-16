from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'completada', 'creada_en')
    list_filter = ('completada',)
    search_fields = ('titulo',)