from django.shortcuts import render
from django import forms

class FormularioSoma(forms.Form):
    numero1 = forms.CharField(widget=forms.NumberInput)
    numero2 = forms.CharField(widget=forms.NumberInput)

def index(request):
    formulario = FormularioSoma(request.POST or None)

    if request.method == 'POST' and formulario.is_valid():
        n1 = float(formulario.clean()['numero1'])
        n2 = float(formulario.clean()['numero2'])
        resultado = n1 + n2

        return render(request, 'resultado.html', {
            'resultado' : resultado
        })



    return render(request, 'index.html',{
        'frm' : formulario
    })