from django import forms

from .models import Categoria, Embalagem, Local, Fornecedor, Produto


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome', 'tipo']


class EmbalagemForm(forms.ModelForm):
    class Meta:
        model = Embalagem
        fields = ['nome', 'sigla']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome_social', 'nome_fantazia']


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'embalagens', 'estoque_minimo', 'estoque_maximo',]


        