from django.urls import path

from .views import (
    adicionar_categorias,
    adicionar_embalagem,
    adicionar_local,
    editar_categoria,
    editar_embalagem,
    editar_local,
    excluir_categoria,
    excluir_embalagem,
    excluir_local,
    inicio,
    listar_categorias,
    listar_embalagem,
    listar_locais,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    # locais
    path('locais/', listar_locais, name='listar_locais'),
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
    path('embalagem/', listar_embalagem, name='listar_embalagem'),
    path('embalagem/adicionar/', adicionar_embalagem, name='adicionar_embalagem'),
    path('embalagem/editar/<int:pk>/', editar_embalagem, name='editar_embalagem'),
    path('embalagem/excluir/<int:pk>/', excluir_embalagem, name='excluir_embalagem'),
    path('local/editar/<int:pk>/', editar_local, name='editar_local'),
    path('local/excluir/<int:pk>/', excluir_local, name='excluir_local'),
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/adicionar/', adicionar_categorias, name='adicionar_categoria'),
    path('categoria/editar/<int:pk>/', editar_categoria, name='editar_categoria'),
    path('categoria/excluir/<int:pk>/', excluir_categoria, name='excluir_categoria'),
]
