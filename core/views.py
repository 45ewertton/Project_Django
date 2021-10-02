from django.shortcuts import redirect, render
from core.forms import AlunoForm
from core.models import Aluno

# Create your views here.
def index(request):
    context = {}
    context['db'] = Aluno.objects.all()
    return render(request, 'index.html', context)

def form(request):
    context = {}
    context['form'] = AlunoForm()
    return render(request, 'form.html', context)

def create(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

def view(request, pk):
    context = {}
    context['db'] = Aluno.objects.get(pk=pk)
    return render(request, 'view.html', context)

def edit(request, pk):
    context = {}
    context['db'] = Aluno.objects.get(pk=pk)
    context['form'] = AlunoForm(instance=context['db'])
    return render(request, 'form.html', context)

def update(request, pk):
    context = {}
    context['db'] = Aluno.objects.get(pk=pk)
    form = AlunoForm(request.POST or None, instance=context['db'])
    if form.is_valid():
        form.save()
        return redirect('index')

def delete(request, pk):
    db = Aluno.objects.get(pk=pk)
    db.delete()
    return redirect('index')