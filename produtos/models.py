from django.db import models
from utils.base_models import BaseModel


class Local(BaseModel):
    TIPOS_DE_LOCAL = [
        ('F', 'Fisico'),
        ('D', 'Digital'),
    ]

    name = models.CharField(max_length=50, verbose_name='nome do local armazenado')
    tipo = models.CharField(max_length=1, choices=TIPOS_DE_LOCAL, verbose_name='tipo do local movimentado')

    class Meta:
        db_table = 'locais'
        

class Movimentacao(BaseModel):
    TIPOS_MOVIMENTACAO = [
        (1, 'entrada'),
        (-1, 'saida'),
    ]

    produto = models.ForeignKey("produtos.Produto", on_delete=models.CASCADE, verbose_name='produto da movimentação')
    fornecedor = models.ForeignKey('produtos.Fornecedor', on_delete=models.CASCADE, verbose_name='fornecedor do produto movimentado')
    quantidade = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='quantidade movimentada')
    local = models.ForeignKey('produtos.Local', on_delete=models.CASCADE, verbose_name='local da movimentação')
    tipo = models.IntegerField(choices=TIPOS_MOVIMENTACAO, verbose_name='tipo de movimentação')

    class Meta:
        db_table = 'movimentacoes'
       

class Embalagem(BaseModel):
    nome = models.CharField(max_length=50, verbose_name='nome da embalagem')
    unidade = models.CharField(max_length=3, verbose_name='sigla da embalagem')

    class Meta:
        db_table = 'embalagens'
    

class Produto(BaseModel):
    nome = models.CharField(max_length=100, verbose_name='nome do produto')
    categoria = models.ForeignKey('produtos.Categoria',on_delete=models.CASCADE,verbose_name='categoria do produto')
    embalagens = models.ManyToManyField('produtos.Embalagem', verbose_name='embalagens do produto')

    class Meta:
        db_table = 'produtos'

class Categoria(BaseModel):
    nome = models.CharField(max_length=100, verbose_name='nome da categoria', unique=True)

    class Meta:
        db_table = 'categorias'

class Fornecedor(BaseModel):
    nome_social = models.CharField(max_length=100, verbose_name='nome do social')
    nome_fantazia = models.CharField(max_length=100,verbose_name='nome fantazia')
    produtos = models.ManyToManyField('produtos.Produto',verbose_name='produtos do fornecedor')
    

    class Meta:
        db_table = 'fornecedores'