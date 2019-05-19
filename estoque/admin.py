from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Produto,Compra

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_medio',)
    search_fields = ('nome',)
    list_filter = ( 'nome',)
       
class ComprasAdmin(admin.ModelAdmin):
    list_display = ('produto','quantidade', 'valor',)
    search_fields = ('quantidade', 'produto')
    list_filter = ('produto', 'quantidade','valor',)


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Compra, ComprasAdmin )
