from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Empresa, Associado, Agendamento, LancamentoTotal, DebitoTotal, Financeiro
from .forms import EmpresaForm, AssociadoForm, AgendamentoForm, LancamentoTotalForm, DebitoTotalForm,FinanceiroForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.conf import settings



class Home(LoginRequiredMixin, TemplateView):
    template_name = "core/index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            return redirect('/admin/')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensagem'] = 'sind-registra'
        return context


# @login_required
# def home(request):
#     context = {'mensagem': 'sind-registra'}
#     return render(request, 'core/index.html', context)
        
@login_required
def home(request):
    context = {'mensagem': 'sind-registra'}
    return render(request, 'core/index.html', context)

@login_required
def lista_empresas(request):
    empresas = Empresa.objects.all()
    form = EmpresaForm()
    return render(request, 'core/lista_empresas.html', {'empresas': empresas, 'form': form})

def empresa_novo(request):
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Empresa adicionada com sucesso")
        return redirect('core_lista_empresas')
    else:
            form = EmpresaForm()
    return render    
    
def empresa_update(request, id):
    data = {}
    empresa = Empresa.objects.get(id=id)
    form = EmpresaForm(request.POST or None, instance=empresa)
    data['empresa'] = empresa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request,"Empresa editada com sucesso")
            return redirect('core_lista_empresas')    
    else:
        return render(request, 'core/update_empresa.html', data)  

def empresa_delete(request, id):
     empresa = Empresa.objects.get(id=id)   
     if request.method == 'POST':
             empresa.delete()
             messages.warning(request,"Empresa deletada com sucesso")
             return redirect('core_lista_empresas')
     else:
             return render(request, 'core/delete_empresa.html', {'empresa': empresa})    

@login_required
def lista_associados(request):
    associados = Associado.objects.all()
    form = AssociadoForm(request.POST)
    return render(request, 'core/lista_associados.html', {'associados': associados, 'form': form})    

def associado_novo(request):
        form = AssociadoForm(request.POST or None)
        if form.is_valid():
             form.save()
        messages.warning(request,"Associado adicionado com sucesso")
        return redirect('core_lista_associados')   


def associado_update(request, id):
    data = {}
    associado = Associado.objects.get(id=id)
    form = AssociadoForm(request.POST or None, instance=associado)
    data['associado'] = associado
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.warning(request,"Associado Editado com sucesso")
            return redirect('core_lista_associados')    
    else:
        return render(request, 'core/update_associado.html', data)

def associado_delete(request, id):
     associado = Associado.objects.get(id=id)   
     if request.method == 'POST':
             associado.delete()
             messages.warning(request,"Associado deletado com sucesso")
             return redirect('core_lista_associados')
     else:
             return render(request, 'core/delete_associado.html', {'associado': associado}) 

@login_required
def lista_lancamentos(request):
    lancamentos = Lancamento.objects.all()
    form = LancamentoForm(request.POST)
    return render(request, 'core/lista_lancamentos.html', {'lancamentos': lancamentos, 'form': form})    

def lancamento_novo(request):
    form = LancamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.warning(request,"Lançamento adicionado com sucesso")
    return redirect('core_lista_lancamentos')   
    

def lancamento_update(request, id):
    data = {}
    lancamento = Lancamento.objects.get(id=id)
    form = LancamentoForm(request.POST or None, instance=lancamento)
    data['lancamento'] = lancamento
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.warning(request,"Lançamento editado com sucesso")
            return redirect('core_lista_lancamentos')    
    else:
        return render(request, 'core/update_lancamento.html', data)

def lancamento_delete(request, id):
     lancamento = Lancamento.objects.get(id=id)   
     if request.method == 'POST':
             associado.delete()
             messages.warning(request,"Lançamento deletado com sucesso")
             return redirect('core_lista_lancamentos')
     else:
             return render(request, 'core/delete_lancamento.html', {'lancamento': lancamento}) 
 
@login_required
def lista_lancamentostotal(request):
    lancamentostotal = LancamentoTotal.objects.all()
    form = LancamentoTotalForm(request.POST)
    return render(request, 'core/lista_lancamentostotal.html', {'lancamentostotal': lancamentostotal, 'form': form})    

def lancamentototal_novo(request):
    form = LancamentoTotalForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.warning(request,"Lançamento adicionado com sucesso")
    return redirect('core_lista_lancamentostotal')   
    

def lancamentototal_update(request, id):
    data = {}
    lancamentototal = LancamentoTotal.objects.get(id=id)
    form = LancamentoTotalForm(request.POST or None, instance=lancamentototal)
    data['lancamentototal'] = lancamentototal
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.warning(request,"Lançamento editado com sucesso")
            return redirect('core_lista_lancamentostotal')    
    else:
        return render(request, 'core/update_lancamentototal.html', data)

def lancamentototal_delete(request, id):
     lancamentototal = LancamentoTotal.objects.get(id=id)   
     if request.method == 'POST':
             lancamentototal.delete()
             messages.warning(request,"Lançamento deletado com sucesso")
             return redirect('core_lista_lancamentostotal')
     else:
             return render(request, 'core/delete_lancamentototal.html', {'lancamentototal': lancamentototal}) 

@login_required
def lista_debitos(request):
    debitos = Debito.objects.all()
    form = DebitoForm(request.POST)
    return render(request, 'core/lista_debitos.html', {'debitos': debitos, 'form': form})    

def debito_novo(request):
    form = DebitoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.warning(request,"Debito adicionado com sucesso")
    return redirect('core_lista_debitos')   
    

def debito_update(request, id):
    data = {}
    debito = Debito.objects.get(id=id)
    form = DebitoForm(request.POST or None, instance=debito)
    data['debito'] = debito
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.warning(request,"Debito atualizado com sucesso")
            return redirect('core_lista_debitos')    
    else:
        return render(request, 'core/update_debito.html', data)

def debito_delete(request, id):
     debito = Debito.objects.get(id=id)   
     if request.method == 'POST':
             debito.delete()
             messages.warning(request,"Debito deletado com sucesso")
             return redirect('core_lista_debitos')
     else:
             return render(request, 'core/delete_debito.html', {'debito': debito})  

@login_required
def lista_debitostotal(request):
    debitostotal = DebitoTotal.objects.all()
    form = DebitoTotalForm(request.POST)
    return render(request, 'core/lista_debitostotal.html', {'debitostotal': debitostotal, 'form': form})    

def debitototal_novo(request):
    form = DebitoTotalForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.warning(request,"Debito adicionado com sucesso")
    return redirect('core_lista_debitostotal')   
    

def debitototal_update(request, id):
    data = {}
    debitototal = DebitoTotal.objects.get(id=id)
    form = DebitoTotalForm(request.POST or None, instance=debitototal)
    data['debitototal'] = debitototal
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.warning(request,"Debito atualizado com sucesso")
            return redirect('core_lista_debitostotal')    
    else:
        return render(request, 'core/update_debitototal.html', data)

def debitototal_delete(request, id):
     debitototal = DebitoTotal.objects.get(id=id)   
     if request.method == 'POST':
             debitototal.delete()
             messages.warning(request,"Debito deletado com sucesso")
             return redirect('core_lista_debitostotal')
     else:
             return render(request, 'core/delete_debitototal.html', {'debitototal': debitototal})               

@login_required
def lista_financeiros(request):
    financeiros = Financeiro.objects.all()
    form = FinanceiroForm(request.POST)
    return render(request, 'core/lista_financeiros.html', {'financeiros': financeiros, 'form': form})    

def financeiro_novo(request):
    form = FinanceiroForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.warning(request,"Financeiro adicionado com sucesso")
    return redirect('core_lista_financeiros')   
    

def financeiro_update(request, id):
    data = {}
    financeiro = financeiro.objects.get(id=id)
    form = FinanceiroForm(request.POST or None, instance=financeiro)
    data['financeiro'] = financeiro
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.warning(request,"Financeiro atualizado com sucesso")
            return redirect('core_lista_financeiros')    
    else:
        return render(request, 'core/update_financeiro.html', data)

def financeiro_delete(request, id):
     financeiro = Financeiro.objects.get(id=id)   
     if request.method == 'POST':
             financeiro.delete()
             messages.warning(request,"Financeiro deletado com sucesso")
             return redirect('core_lista_financeiros')
     else:
             return render(request, 'core/delete_financeiro.html', {'financeiro': financeiro})  

@login_required
def lista_agendamento(request):
    agendamentos = Agendamento.objects.all()
    form = AgendamentoForm(request.POST)
    return render(request, 'core/lista_agendamento.html', {'agendamentos': agendamentos, 'form': form})    
  

def agendamento_novo(request):
    form = AgendamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.warning(request,"Agendamento adicionado com sucesso")

   
def agendamento_update(request, id):
    data = {}
    agendamento = Agendamento.objects.get(id=id)
    form = AgendamentoForm(request.POST or None, instance=agendamento)
    data['agendamento'] = agendamento
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.warning(request,"Agendamento atualizado com sucesso")
            return redirect('core_lista_agendamento')    
    else:
        return render(request, 'core/update_agendamento.html', data)   

def agendamento_delete(request, id):
     agendamento = Agendamento.objects.get(id=id)   
     if request.method == 'POST':
             agendamento.delete()
             messages.warning(request,"Agendamento deletado com sucesso")
             return redirect('core_lista_agendamento')
     else:
             return render(request, 'core/delete_agendamento.html', {'agendamento': agendamento})            

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class PdfEmpresa(View):
    def get(self, request):
        empresas = Empresa.objects.all()
        params = {
            'empresas': empresas,
            'request': request,
        }
        return Render.render('core/relatorio_empresas.html', params, 'relatorio_empresas')

class PdfAssociado(View):
    def get(self, request):
        associados = Associado.objects.all()
        params = {
            'associados': associados,
            'request': request,
        }
        return Render.render('core/relatorio_associados.html', params, 'relatorio_associados') 

class PdfLancamento(View):
    def get(self, request):
        lancamentostotal = LancamentoTotal.objects.all()
        params = {
            'lancamentostotal': lancamentostotal,
            'request': request,
        }
        return Render.render('core/relatorio_lancamentos.html', params, 'relatorio_lancamentos')


class PdfDebitos(View):
    def get(self, request):
        debitostotal = DebitoTotal.objects.all()
        params = {
            'debitostotal': debitostotal,
            'request': request,
        }
        return Render.render('core/relatorio_debitos.html', params, 'relatorio_debitos')

class PdfFinanceiro(View):
    def get(self, request):
        financeiros = Financeiro.objects.all()
        params = {
            'financeiros': financeiros,
            'request': request,
        }
        return Render.render('core/relatorio_financeiro.html', params, 'relatorio_financeiro')        