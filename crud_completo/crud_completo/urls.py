"""crud_completo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud_completo.views import paginas, categorias, produtos

urlpatterns = [
    # PÁGINA PRINCIPAL
    path('', paginas.home, name='home'),

    # PÁGINAS DO CRUD DE CATEGORIA
    path('categorias', categorias.listar, name='categorias'),
    path('categorias/criar', categorias.criar, name='categorias.criar'),
    path('categorias/editar/<id>', categorias.editar, name='categorias.editar'),
    path('categorias/excluir/<id>', categorias.excluir, name='categorias.excluir'),

    # PÁGINAS DO CRUD DE PRODUTOS
    path('produtos', produtos.listar, name='produtos'),
    path('produtos/criar', produtos.criar, name='produtos.criar'),
    path('produtos/editar/<id>', produtos.editar, name='produtos.editar'),
    path('produtos/excluir/<id>', produtos.excluir, name='produtos.excluir'),
]
