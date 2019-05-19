from django.forms import ModelForm
from .models import Empresa, Associado, Agendamento, Lancamento, Debito
from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
import datetime


class EmpresaForm(ModelForm):
  class Meta:
    model = Empresa
    fields = "__all__"


class AssociadoForm(ModelForm):
  class Meta:
    model = Associado
    fields = "__all__"

class LancamentoForm(ModelForm):
  class Meta:
    model = Lancamento
    fields = "__all__"    

class DebitoForm(ModelForm):
  class Meta:
    model = Debito
    fields = "__all__"


class AgendamentoForm(ModelForm):
  class Meta:
    model = Agendamento
    fields = "__all__" 

    