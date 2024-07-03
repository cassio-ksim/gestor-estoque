from django.shortcuts import redirect, render

from .forms import EmbalagemForm, LocalForm
from .models import Embalagem, Local


def inicio(request):
    return render(request, 'menu.html')


def listar_locais(request):
    consulta = request.GET.get('q')
    tipo = request.GET.get('tipo')
    locais = Local.objects.all()
    if consulta:
        locais = locais.filter(nome__icontains=consulta)
    if tipo:
        locais = locais.filter(tipo=tipo)
    return render(
        request, 'produtos/listar_locais.html', {'locais': locais}
    )


def adicionar_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_locais')
    else:
        form = LocalForm()
    return render(request, 'produtos/adicionar_local.html', {'form': form})


def listar_embalagem(request):
    nome = request.GET.get('q')
    sigla = request.GET.get('sigla')
    embalagens = Embalagem.objects.all()
    if nome:
        nome = embalagens.filter(nome__icontains=nome)
    if sigla:
        embalagens = embalagens.filter(sigla=sigla)
    return render(
        request, 'produtos/listar_embalagem.html', {'embalagens': embalagens}
    )


def adicionar_embalagem(request):
    if request.method == 'POST':
        form = EmbalagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_embalagem')
    else:
        form = EmbalagemForm()
    return render(request, 'produtos/adicionar_embalagem.html', {'form': form})

def editar_embalagem(request, pk):
    embalagem = Embalagem.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmbalagemForm(request.POST, instance=embalagem)
        if form.is_valid():
            form.save()
            return redirect('listar_embalagem')
    else:
        form = EmbalagemForm(instance=embalagem)
    return render(request, 'produtos/editar_embalagem.html', {'form': form})

def excluir_embalagem(request, pk):
    embalagem = Embalagem.objects.get(pk=pk)
    embalagem.delete()
    return redirect('listar_embalagem')

def editar_local(request, pk):
    local = Local.objects.get(pk=pk)
    if request.method == 'POST':
        form = LocalForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            return redirect('listar_locais')
    else:
        form = LocalForm(instance=local)
    return render(request, 'produtos/editar_locais.html', {'form': form})

def excluir_local(request, pk):
    local = Local.objects.get(pk=pk)
    local.delete()
    return redirect('listar_locais')