from django.http import HttpResponse
from django.shortcuts import render

def contact(request):
    return HttpResponse(
        "Nome: Kaion\n Idade: 20\n Cidade: São Paulo\n"
        "Telefone: (11) 99999-9999\n"
        "E-mail: kaionbrandom.@gmail.com")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
