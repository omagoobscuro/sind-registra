from django.urls import include, path

from .views import (home,
lista_empresas,
lista_associados,
lista_pagamentos,
empresa_novo,
associado_novo,
pagamento_novo,
associado_update,
pagamento_update,
empresa_update,
associado_delete,
pagamento_delete,
empresa_delete,
PdfEmpresa,
PdfAssociado,
PdfPagamento
)


urlpatterns = [
    path('associados/',lista_associados, name = 'core_lista_associados'),
    path('associado-novo/', associado_novo, name = 'core_associado_novo'),
    path('associado-update/(?P<id>\d+)/$', associado_update, name = 'core_associado_update'),
    path('associado-delete/(?P<id>\d+)/$', associado_delete, name = 'core_associado_delete'),

    path('empresas/', lista_empresas, name = 'core_lista_empresas'),
    path('empresa-novo/', empresa_novo, name = 'core_empresa_novo'),
    path('empresa-update/(?P<id>\d+)/$', empresa_update, name = 'core_empresa_update'),
    path('empresa-delete/(?P<id>\d+)/$', empresa_delete, name = 'core_empresa_delete'),    

    path('pagamentos/', lista_pagamentos, name = 'core_lista_pagamentos'),
    path('pagamento-novo/', pagamento_novo, name = 'core_pagamento_novo'),
    path('pagamento-update/(?P<id>[0-9]+)/$', pagamento_update, name = 'core_pagamento_update'),
    path('pagamento-delete/(?P<id>\d+)/$', pagamento_delete, name = 'core_pagamento_delete'),   

    path(r'', home, name = 'home'),
    path(r'relatorio/$', PdfEmpresa.as_view(), name='relatorio_pdf'),
    path(r'relatorio_associados', PdfAssociado.as_view(), name='relatorio_associados'),
    path(r'relatorio_pagamentos', PdfPagamento.as_view(), name='relatorio_pagamentos'),
    
]
