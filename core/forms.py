from django.forms import ModelForm
from .models import Empresa, Associado, Pagamento


class EmpresaForm(ModelForm):
  class Meta:
    model = Empresa
    fields = "__all__"


class AssociadoForm(ModelForm):
  class Meta:
    model = Associado
    fields = "__all__"


class PagamentoForm(ModelForm):
  class Meta:
    model = Pagamento
    fields = "__all__"  