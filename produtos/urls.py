from django.urls import path

from .views import adicionar_local, inicio, listar_locais

urlpatterns = [
    path('', inicio, name='inicio'),
    # locais
    path('locais/', listar_locais, name='listar_locais'),
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
]
