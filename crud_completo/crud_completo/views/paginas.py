from django.shortcuts import render


def home(request):
    '''
    Página inicial da aplicação
    '''
    return render(request, 'home.html', {})