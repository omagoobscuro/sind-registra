from django.urls import include, path,re_path

from .views import (home,
lista_empresas,
lista_associados,
lista_lancamentostotal,
lista_debitostotal,
lista_financeiros,
empresa_novo,
associado_novo,
lancamentototal_novo,
debitototal_novo,
financeiro_novo,
associado_update,
lancamentototal_update,
empresa_update,
debitototal_update,
financeiro_update,
associado_delete,
lancamentototal_delete,
empresa_delete,
debitototal_delete,
financeiro_delete,
PdfEmpresa,
PdfAssociado,
PdfLancamento,
PdfDebitos,
PdfFinanceiro,
lista_agendamento,
agendamento_novo,
agendamento_update,
agendamento_delete
)


urlpatterns = [
    path('associados/',lista_associados, name = 'core_lista_associados'),
    path('associado-novo/', associado_novo, name = 'core_associado_novo'),
    re_path('associado-update/(?P<id>\d+)/$', associado_update, name = 'core_associado_update'),
    re_path('associado-delete/(?P<id>\d+)/$', associado_delete, name = 'core_associado_delete'),

    path('empresas/', lista_empresas, name = 'core_lista_empresas'),
    path('empresa-novo/', empresa_novo, name = 'core_empresa_novo'),
    re_path('empresa-update/(?P<id>\d+)/$', empresa_update, name = 'core_empresa_update'),
    re_path('empresa-delete/(?P<id>\d+)/$', empresa_delete, name = 'core_empresa_delete'),   

    path('lancamentostotal/', lista_lancamentostotal, name = 'core_lista_lancamentostotal'),
    path('lancamentototal-novo/', lancamentototal_novo, name = 'core_lancamentototal_novo'),
    re_path('lancamentototal-update/(?P<id>\d+)/$', lancamentototal_update, name = 'core_lancamentototal_update'),
    re_path('lancamentototal-delete/(?P<id>\d+)/$', lancamentototal_delete, name = 'core_lancamentototal_delete'),     

    path('debitostotal/', lista_debitostotal, name = 'core_lista_debitostotal'),
    path('debitototal-novo/', debitototal_novo, name = 'core_debitototal_novo'),
    re_path('debitototal-update/(?P<id>\d+)/$', debitototal_update, name = 'core_debitototal_update'),
    re_path('debitototal-delete/(?P<id>\d+)/$', debitototal_delete, name = 'core_debitototal_delete'),   

    path('financeiro/', lista_financeiros, name = 'core_lista_financeiros'),
    path('financeiro-novo/', financeiro_novo, name = 'core_financeiro_novo'),
    re_path('financeiro-update/(?P<id>\d+)/$', financeiro_update, name = 'core_financeiro_update'),
    re_path('financeiro-delete/(?P<id>\d+)/$', financeiro_delete, name = 'core_financeiro_delete'),         

    path(r'', home, name = 'home'),
    re_path(r'relatorio/$', PdfEmpresa.as_view(), name='relatorio_pdf'),
    path(r'relatorio_associados', PdfAssociado.as_view(), name='relatorio_associados'),
    path(r'relatorio_lancamentos', PdfLancamento.as_view(), name='relatorio_lancamentos'),
    path(r'relatorio_debitos', PdfDebitos.as_view(), name='relatorio_debitos'),
    path(r'relatorio_financeiro', PdfFinanceiro.as_view(), name='relatorio_financeiro'),

    path('agendamento/', lista_agendamento, name='core_lista_agendamento'),
    path('agendamento-novo/', agendamento_novo, name = 'core_agendamento_novo'),
    re_path(r'agendamento-update/(?P<id>\d+)/$', agendamento_update, name = 'core_agendamento_update'),
    re_path(r'agendamento-delete/(?P<id>\d+)/$', agendamento_delete, name = 'core_agendamento_delete'), 
    
]