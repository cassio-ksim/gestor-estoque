from django.shortcuts import redirect, render

from .forms import CategoriaForm, EmbalagemForm, LocalForm, FornecedorForm, ProdutoForm
from .models import Categoria, Embalagem, Local, Fornecedor, Produto


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


def listar_categorias(request):
    nome = request.GET.get('nome')
    categorias = Categoria.objects.all()
    if nome:
        categorias = categorias.filter(nome__icontains=nome)
    return render(
        request, 'produtos/listar_categorias.html', {'categorias': categorias}
    )


def adicionar_categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'produtos/adicionar_categoria.html', {'form': form})


def editar_categoria(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'produtos/editar_categorias.html', {'form': form})


def excluir_categoria(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    categoria.delete()
    return redirect('listar_categorias')


def listar_fornecedores(request):
    consulta = request.GET.get('q')
    fornecedores = Fornecedor.objects.all()
    if consulta:
        fornecedores = fornecedores.filter(nome__icontains=consulta)
    return render(request, 'produtos/listar_fornecedores.html', {'fornecedores': fornecedores})

def adicionar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm()
    return render(request, 'produtos/adicionar_fornecedor.html', {'form': form})

def editar_fornecedor(request, pk):
    fornecedor = Fornecedor.objects.get(pk=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'produtos/editar_fornecedor.html', {'form': form})

def excluir_fornecedor(request, pk):
    fornecedor = Fornecedor.objects.get(pk=pk)
    fornecedor.delete()
    return redirect('listar_fornecedores')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/adicionar_produto.html', {'form': form})

def editar_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar_produtos.html', {'form': form})

def excluir_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    produto.delete()
    return redirect('listar_produtos')