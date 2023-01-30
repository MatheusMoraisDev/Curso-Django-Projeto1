from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def contatos(request):
    return HttpResponse("CONTATOS")


def sobre(request):
    return HttpResponse("SOBRE")
