from django.shortcuts import get_object_or_404, redirect, render
from crud_completo.models import *
from django.forms import ModelForm

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto # Classe usada para entrada/saída de dados do formulário
        fields = '__all__' # Campos usados no formulário (neste caso, todos)

def listar(request):
    '''
    Lista todas as produtos exitentes
    '''
    produtos =  Produto.objects.all()

    return render(request, 'produtos/lista.html', {
        'produtos': produtos
    })


def criar(request):
    '''
    Ação para cadastrar uma nova categoria
    '''
    frm = ProdutoForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('produtos')

    return render(request, 'produtos/form.html',{
        'titulo' : 'Cadastrar categoria',
        'frm':frm
    })

def editar(request,id):
    '''
    Ação para editar uma categoria
    '''
    categoria = get_object_or_404(Produto, pk=id)
    frm = ProdutoForm(request.POST or None, instance=categoria)

    if frm.is_valid():
        frm.save()
        return redirect('produtos')

    return render(request, 'produtos/form.html',{
        'titulo' : 'Editar categoria',
        'frm':frm
    })

def excluir(request,id):
    '''
    Exclui uma categoria do banco de dados
    '''
    categoria = get_object_or_404(Produto, pk=id)
    categoria.delete()

    return redirect('produtos')
