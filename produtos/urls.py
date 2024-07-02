from django.urls import path

from .views import (
    adicionar_embalagem,
    adicionar_local,
    inicio,
    listar_embalagem,
    listar_locais,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    # locais
    path('locais/', listar_locais, name='listar_locais'),
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
    path('embalagem/', listar_embalagem, name='listar_embalagem'),
    path('embalagem/adicionar/', adicionar_embalagem, name='adicionar_embalagem'),  # noqa: E501
]
