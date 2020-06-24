from django.shortcuts import render
from django.views.generic import CreateView
from .models import Livro
from .forms import CadastroLivro
from django.shortcuts import render, redirect

class CadastroView(CreateView):
    model = Livro
    fields = ("nome", "categoria")
    template_name = "cadastro/index.html"

    def post(self, request, *args, **kwargs):
        form = CadastroLivro(data=request.POST)

        