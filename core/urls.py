from django.urls import include, path,re_path

from .views import (home,
lista_empresas,
lista_associados,
lista_lancamentos,
lista_debitos,
empresa_novo,
associado_novo,
lancamento_novo,
debito_novo,
associado_update,
lancamento_update,
empresa_update,
debito_update,
associado_delete,
lancamento_delete,
empresa_delete,
debito_delete,
PdfEmpresa,
PdfAssociado,
PdfLancamento,
PdfDebitos,
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

    path('lancamentos/', lista_lancamentos, name = 'core_lista_lancamentos'),
    path('lancamento-novo/', lancamento_novo, name = 'core_lancamento_novo'),
    re_path('lancamento-update/(?P<id>\d+)/$', lancamento_update, name = 'core_lancamento_update'),
    re_path('lancamento-delete/(?P<id>\d+)/$', lancamento_delete, name = 'core_lancamento_delete'),   

    path('debitos/', lista_debitos, name = 'core_lista_debitos'),
    path('debito-novo/', debito_novo, name = 'core_debito_novo'),
    re_path('debito-update/(?P<id>\d+)/$', debito_update, name = 'core_debito_update'),
    re_path('debito-delete/(?P<id>\d+)/$', debito_delete, name = 'core_debito_delete'),       

    path(r'', home, name = 'home'),
    re_path(r'relatorio/$', PdfEmpresa.as_view(), name='relatorio_pdf'),
    path(r'relatorio_associados', PdfAssociado.as_view(), name='relatorio_associados'),
    path(r'relatorio_lancamentos', PdfLancamento.as_view(), name='relatorio_lancamentos'),
    path(r'relatorio_debitos', PdfDebitos.as_view(), name='relatorio_debitos'),

    path('agendamento/', lista_agendamento, name='core_lista_agendamento'),
    path('agendamento-novo/', agendamento_novo, name = 'core_agendamento_novo'),
    re_path(r'agendamento-update/(?P<id>\d+)/$', agendamento_update, name = 'core_agendamento_update'),
    re_path(r'agendamento-delete/(?P<id>\d+)/$', agendamento_delete, name = 'core_agendamento_delete'), 
    
]
