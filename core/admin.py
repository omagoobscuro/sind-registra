from django.contrib import admin
from .models import Empresa, Associado, Pagamento

# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cnpj',)

class AssociadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone', 'cpf', 'data_filiacao' )   

class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'valor_pago', 'data_pagamento', )       


admin.site.register(Empresa , EmpresaAdmin)
admin.site.register(Associado , AssociadoAdmin)
admin.site.register(Pagamento , PagamentoAdmin)

admin.site.site_header = 'Administração'