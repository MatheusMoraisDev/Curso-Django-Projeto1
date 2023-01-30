from django.urls import path

from recipes.views import contatos, home, sobre

urlpatterns = [
    path('', home),
    path('contatos/', contatos),
    path('sobre/', sobre),
]
