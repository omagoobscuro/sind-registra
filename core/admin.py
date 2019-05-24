from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import (Empresa, Associado, Agendamento,
LancamentoTotal, DebitoTotal, Financeiro
)
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import format_html




# Register your models here.


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cnpj','telefone', 'email')
    search_fields = ('nome', 'cnpj',)
    list_filter = ( 'nome', 'cnpj',  'telefone', )

class AssociadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone', 'cpf', 'data_filiacao', 'data_nascimento' )   
    search_fields = ('nome', 'cpf',)
    list_filter = ( 'nome', 'cpf',  'telefone', )

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome','inicio', 'fim','assunto', )  
    search_fields = ('nome', 'cpf',)
    list_filter = ( 'nome', 'inicio',  'assunto', )

 
class LancamentoTotalAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'valor', 'data_envio','status',)
    search_fields = ('empresa', 'status',)
    list_filter = ( 'empresa', 'status',  'valor', )

class DebitoTotalAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'valor', 'vencimento',)
    search_fields = ('empresa', 'vencimento',)
    list_filter = ('empresa', 'valor',  'vencimento',)       

class FinanceiroAdmin(admin.ModelAdmin):
    list_display = ('empresa_lancamento','empresa_debito','debito', 'lancamento','consulta', 'total',)
    list_filter = ('debito', 'lancamento',)

     
admin.site.register(Empresa , EmpresaAdmin)
admin.site.register(Associado , AssociadoAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(LancamentoTotal, LancamentoTotalAdmin)
admin.site.register(DebitoTotal, DebitoTotalAdmin)
admin.site.register(Financeiro, FinanceiroAdmin)


admin.site.site_header = 'Administração'