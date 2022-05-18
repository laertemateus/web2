from django.shortcuts import get_object_or_404, redirect, render
from crud_completo.models import *
from django.forms import ModelForm

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria # Classe usada para entrada/saída de dados do formulário
        fields = '__all__' # Campos usados no formulário (neste caso, todos)

def listar(request):
    '''
    Lista todas as categorias exitentes
    '''
    categorias =  Categoria.objects.all()

    return render(request, 'categorias/lista.html', {
        'categorias':categorias
    })


def criar(request):
    '''
    Ação para cadastrar uma nova categoria
    '''
    frm = CategoriaForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('categorias')

    return render(request, 'categorias/form.html',{
        'titulo' : 'Cadastrar categoria',
        'frm':frm
    })

def editar(request,id):
    '''
    Ação para editar uma categoria
    '''
    categoria = get_object_or_404(Categoria, pk=id)
    frm = CategoriaForm(request.POST or None, instance=categoria)

    if frm.is_valid():
        frm.save()
        return redirect('categorias')

    return render(request, 'categorias/form.html',{
        'titulo' : 'Editar categoria',
        'frm':frm
    })

def excluir(request,id):
    '''
    Exclui uma categoria do banco de dados
    '''
    categoria = get_object_or_404(Categoria, pk=id)
    categoria.delete()

    return redirect('categorias')
