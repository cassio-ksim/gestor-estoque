from django.db import models

from utils.base_models import BaseModel


class Local(BaseModel):
    TIPOS_DE_LOCAL = [
        ('F', 'Fisico'),
        ('D', 'Digital'),
    ]

    nome = models.CharField(
        max_length=50, verbose_name='nome do local armazenado'
    )  # noqa: E501
    tipo = models.CharField(
        max_length=1,
        choices=TIPOS_DE_LOCAL,
        verbose_name='tipo do local movimentado',
    )  # noqa: E501

    class Meta:
        db_table = 'locais'


class Movimentacao(BaseModel):
    TIPOS_MOVIMENTACAO = [
        (1, 'entrada'),
        (-1, 'saida'),
    ]

    produto = models.ForeignKey(
        'produtos.Produto',
        on_delete=models.CASCADE,
        verbose_name='produto da movimentação',
    )  # noqa: E501
    fornecedor = models.ForeignKey(
        'produtos.Fornecedor',
        on_delete=models.CASCADE,
        verbose_name='fornecedor do produto movimentado',
    )  # noqa: E501
    quantidade = models.DecimalField(
        max_digits=10, decimal_places=6, verbose_name='quantidade movimentada'
    )  # noqa: E501
    local = models.ForeignKey(
        'produtos.Local',
        on_delete=models.CASCADE,
        verbose_name='local da movimentação',
    )  # noqa: E501
    tipo = models.IntegerField(
        choices=TIPOS_MOVIMENTACAO, verbose_name='tipo de movimentação'
    )  # noqa: E501

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=6,
        verbose_name='preço do produto na movimentação',
    )

    codigo_fabricante = models.CharField(
        max_length=20,
        verbose_name='código do fabricante',
    )

    class Meta:
        db_table = 'movimentacoes'


class Embalagem(BaseModel):
    nome = models.CharField(max_length=50, verbose_name='nome da embalagem')
    sigla = models.CharField(max_length=3, verbose_name='sigla da embalagem')

    class Meta:
        db_table = 'embalagens'


class Produto(BaseModel):
    nome = models.CharField(max_length=100, verbose_name='nome do produto')
    categoria = models.ForeignKey(
        'produtos.Categoria',
        on_delete=models.CASCADE,
        verbose_name='categoria do produto',
    )  # noqa: E501
    embalagens = models.ManyToManyField(
        'produtos.Embalagem', verbose_name='embalagens do produto'
    )  # noqa: E501

    estoque_minimo = models.FloatField(
        verbose_name='estoque mínimo do produto',
    )

    estoque_maximo = models.FloatField(
        verbose_name='estoque maximo do produto'
    )

    class Meta:
        db_table = 'produtos'


class Categoria(BaseModel):
    nome = models.CharField(
        max_length=100, verbose_name='nome da categoria', unique=True
    )  # noqa: E501

    class Meta:
        db_table = 'categorias'


class Fornecedor(BaseModel):
    nome_social = models.CharField(
        max_length=100, verbose_name='nome do social'
    )  # noqa: E501
    nome_fantazia = models.CharField(
        max_length=100, verbose_name='nome fantazia'
    )  # noqa: E501
    produtos = models.ManyToManyField(
        'produtos.Produto', verbose_name='produtos do fornecedor'
    )  # noqa: E501

    class Meta:
        db_table = 'fornecedores'
