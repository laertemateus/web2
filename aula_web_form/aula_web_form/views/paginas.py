
from tabnanny import verbose
from django import forms
from django.shortcuts import render


class SomaForm(forms.Form):
    numero1 = forms.CharField(max_length=100, widget=forms.NumberInput(),label='Número 1')
    numero2 = forms.CharField(max_length=100, widget=forms.NumberInput(), label='Número 2')


def soma(request):
    form = SomaForm(request.POST or None)

    if form.is_valid():
        n1 = int(form.cleaned_data['numero1'])
        n2 = int(form.cleaned_data['numero2'])
        resultado = n1+n2

        return render(request,'resultado.html',{
            'resultado':resultado
        })
    return render(request, 'soma.html', {
        'form':form
    })