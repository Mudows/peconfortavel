from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Produto, Fabricante
from .forms import ClienteForm, ProdutoForm, FabricanteForm

# Página inicial
def index(request):
    return render(request, 'index.html')

# ---------- Cliente ----------
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            # O save do model já faz hash da senha
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cadastro_cliente.html', {'form': form})

# ---------- Produto ----------
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def cadastro_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)  # para imagens
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'cadastro_produto.html', {'form': form})

# ---------- Fabricante ----------
def lista_fabricantes(request):
    fabricantes = Fabricante.objects.all()
    return render(request, 'lista_fabricantes.html', {'fabricantes': fabricantes})

def cadastro_fabricante(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fabricantes')
    else:
        form = FabricanteForm()
    return render(request, 'cadastro_fabricante.html', {'form': form})

# ---------- Contato (estático) ----------
def contato(request):
    return render(request, 'contato.html')