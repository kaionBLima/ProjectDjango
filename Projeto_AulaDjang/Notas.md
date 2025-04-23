Instalando Django e configurando ambiente virtual:

py -m venv .venv

.venv/Scripts/activate

py -m pip install Django

django-admin startproject projectDjango

cd projectDjango

py manage.py runserver

Clica no Link https://Endereço/ que irá te direcionar para um site com Django em funcionamento

Entra na urls.py:   
    path('', )

Cria um arquivo view dentro projectDjango e dentro dela digita:
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world")

Volto na urls.py:
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home)
]

Vou no link que me foi gerado quando criei o ambiente virtual Django e o atualizo


Crio uma pasta Templates e crio arquivos html

Vou em settings:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates']}]

Vou em views e digito:
from django.shortcuts import render