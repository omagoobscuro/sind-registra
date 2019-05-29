from django.forms import ModelForm
from .models import Empresa, Associado, Agendamento, LancamentoTotal, DebitoTotal, Financeiro,Juridico
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

class LancamentoTotalForm(ModelForm):
  class Meta:
    model = LancamentoTotal
    fields = "__all__"


class DebitoTotalForm(ModelForm):
  class Meta:
    model = DebitoTotal
    fields = "__all__"

class FinanceiroForm(ModelForm):
  class Meta:
    model = Financeiro
    fields = "__all__"

class AgendamentoForm(ModelForm):
  class Meta:
    model = Agendamento
    fields = "__all__"

  
f = AgendamentoForm() # Note, this is an unbound form
f.is_valid()
False
f.errors # No errors
{}
f = AgendamentoForm({}) # Now, the form is bound (to an empty dictionary)
f.is_valid()
False
f.errors # dictionary of errors
{'inicio': [u'This field is required.'], 'email': [u'This field is required.']}

 

class JuridicoForm(ModelForm):
  class Meta:
    model = Juridico
    fields = "__all__"