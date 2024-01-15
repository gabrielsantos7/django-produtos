from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Produto


def cadastrar(request):
    if request.method == "GET":
        return render(request, "cadastrar.html")
    elif request.method == "POST":
        nome = request.POST["nome"]
        preco = request.POST["preco"]
        validade = request.POST["validade"]
        quantidade = request.POST["quantidade"]

        produto = Produto(
            nome=nome, preco=preco, validade=validade, quantidade=quantidade
        )
        produto.save()

        return redirect("cadastrar")


def listar(request):
    nome = request.GET.get("nome")
    if nome:
        produtos = Produto.objects.filter(nome__icontains=nome)
    else:
        produtos = Produto.objects.all()
    return render(request, "listar.html", {"produtos": produtos, "nome": nome})


def detalhes(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, "detalhes.html", {"produto": produto})

def editar(request, id):
    produto = Produto.objects.get(id=id)
    status = None

    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.preco = request.POST.get('preco')
        produto.validade = request.POST.get('validade')
        produto.quantidade = request.POST.get('quantidade')

        produto.save()
        status = 'Sucesso!'

    return render(request, 'editar.html', {'produto': produto, 'status': status})

def deletar(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect("listar")

def handle404(request, exception):
    return render(request, '404.html', status=404)