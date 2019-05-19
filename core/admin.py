from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import (Empresa, Associado, Agendamento, Lancamento, Debito,
 LancamentoTotal, DebitoTotal, Financeiro
)
from django.http import HttpResponse
from django.http import HttpResponseRedirect



# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cnpj',)
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

   
class LancamentoAdmin(admin.ModelAdmin):
    list_display = ('empresa','valor','vencimento','data_envio','status', )    

class LancamentoTotalAdmin(admin.ModelAdmin):
    list_display = ('valor','empresa' )   

class DebitoAdmin(admin.ModelAdmin):
    list_display = ('empresa','valor', 'vencimento', )    

class DebitoTotalAdmin(admin.ModelAdmin):
    list_display = ('valor','empresa', )       

class FinanceiroAdmin(admin.ModelAdmin):
    list_display = ('debito', 'lancamento','consulta', 'total',)
    list_filter = ('debito', 'lancamento',)

     
admin.site.register(Empresa , EmpresaAdmin)
admin.site.register(Associado , AssociadoAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(Lancamento, LancamentoAdmin)
admin.site.register(LancamentoTotal, LancamentoTotalAdmin)
admin.site.register(DebitoTotal, DebitoTotalAdmin)
admin.site.register(Financeiro, FinanceiroAdmin)


admin.site.site_header = 'Administração'