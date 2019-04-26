from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views.generic.base import View
from django.http import HttpResponse
from .models import Empresa, Associado, Pagamento
from .forms import EmpresaForm, AssociadoForm, PagamentoForm


# Create your views here.
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
            return redirect('core_lista_empresas')    
    else:
        return render(request, 'core/update_empresa.html', data)  

def empresa_delete(request, id):
     empresa = Empresa.objects.get(id=id)   
     if request.method == 'POST':
             empresa.delete()
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
            return redirect('core_lista_associados')    
    else:
        return render(request, 'core/update_associado.html', data)

def associado_delete(request, id):
     associado = Associado.objects.get(id=id)   
     if request.method == 'POST':
             associado.delete()
             return redirect('core_lista_associados')
     else:
             return render(request, 'core/delete_associado.html', {'associado': associado}) 

@login_required
def lista_pagamentos(request):
    pagamentos = Pagamento.objects.all()
    form = PagamentoForm(request.POST)
    return render(request, 'core/lista_pagamentos.html', {'pagamentos': pagamentos, 'form': form})    

def pagamento_novo(request):
    form = PagamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pagamentos')
   
def pagamento_update(request, id):
    data = {}
    pagamento = Pagamento.objects.get(id=id)
    form = PagamentoForm(request.POST or None, instance=pagamento)
    data['pagamento'] = pagamento
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pagamentos')    
    else:
        return render(request, 'core/update_pagamento.html', data)   

def pagamento_delete(request, id):
     pagamento = Pagamento.objects.get(id=id)   
     if request.method == 'POST':
             pagamento.delete()
             return redirect('core_lista_pagamentos')
     else:
             return render(request, 'core/delete_pagamento.html', {'pagamento': pagamento})           

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

class PdfPagamento(View):
    def get(self, request):
        pagamentos = Pagamento.objects.all()
        params = {
            'pagamentos': pagamentos,
            'request': request,
        }
        return Render.render('core/relatorio_pagamentos.html', params, 'relatorio_pagamentos') 