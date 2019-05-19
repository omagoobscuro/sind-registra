from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Juridico

# Register your models here.
class JuridicoAdmin(admin.ModelAdmin):
    list_display = ('processo','motivo', 'reclamante', 'reclamado', 'data_entrada', 'status',)   
    search_fields = ('processo', 'reclamante', 'reclamado',)
    list_filter = ( 'processo', 'reclamante',  'reclamado', 'status', )



admin.site.register(Juridico, JuridicoAdmin)