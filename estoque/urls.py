from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("listar/", views.listar, name="listar"),
    path("produto/<int:id>/", views.detalhes, name="detalhes"),
    path("produto/<int:id>/editar/", views.editar, name="editar"),
    path("deletar/<int:id>/", views.deletar, name="deletar")
]

handler404 = 'estoque.views.handle404'
