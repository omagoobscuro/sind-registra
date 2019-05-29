from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import (Empresa, Associado, Agendamento,
LancamentoTotal, DebitoTotal, Financeiro,Juridico
)
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.html import format_html
from django.template.response import TemplateResponse



# Register your models here.

def relatorio(self, request, obj):
    return redirect('relatorio_pdf')

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cnpj','telefone', 'email',)
    search_fields = ('nome', 'cnpj',)
    list_filter = ( 'nome', 'cnpj',  'telefone', )
    actions=[relatorio]
   
def relatorio_associados(self, request, obj):
    return redirect('relatorio_associados')

class AssociadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone', 'cpf', 'data_filiacao', 'data_nascimento')   
    search_fields = ('nome', 'cpf',)
    list_filter = ( 'nome', 'cpf',  'telefone', )
    actions=[relatorio_associados]


class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome','inicio', 'fim','assunto', )  
    search_fields = ('nome', 'cpf',)
    list_filter = ( 'nome', 'inicio',  'assunto', )

def relatorio_lancamentos(self, request, obj):
    return redirect('relatorio_lancamentos')

class LancamentoTotalAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'valor', 'data_envio','status',)
    search_fields = ('empresa', 'status',)
    list_filter = ( 'empresa', 'status',  'valor', )
    actions=[relatorio_lancamentos]

class DebitoTotalAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'valor', 'vencimento',)
    search_fields = ('empresa', 'vencimento',)
    list_filter = ('empresa', 'valor',  'vencimento',)       

def relatorio_financeiro(self, request, obj):
    return redirect('relatorio_financeiro')

class FinanceiroAdmin(admin.ModelAdmin):
    list_display = ('empresa_lancamento','empresa_debito','debito', 'lancamento','consulta', 'total',)
    list_filter = ('debito', 'lancamento',)
    actions=[relatorio_financeiro]

def relatorio_juridico(self, request, obj):
    return redirect('relatorio_juridico')

class JuridicoAdmin(admin.ModelAdmin):
    list_display = ('processo', 'motivo', 'reclamante','reclamado','status','advogado')
    search_fields = ('processo', 'reclamante','reclamado')
    list_filter = ( 'processo', 'reclamante',  'reclamado' )
    actions=[relatorio_juridico]

     
admin.site.register(Empresa , EmpresaAdmin)
admin.site.register(Associado , AssociadoAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(LancamentoTotal, LancamentoTotalAdmin)
admin.site.register(DebitoTotal, DebitoTotalAdmin)
admin.site.register(Financeiro, FinanceiroAdmin)
admin.site.register(Juridico, JuridicoAdmin)


admin.site.site_header = 'Administração'