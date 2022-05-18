from django.db import models


class Categoria(models.Model):
    '''
    Categoria do produto
    '''
    nome = models.CharField(max_length=500)


    def __str__(self):
        return self.nome

class Produto(models.Model):
    '''
    Produto
    '''
    nome = models.CharField(max_length=500)
    preco =models.DecimalField(max_digits=10,decimal_places=2)
    descricao =models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
