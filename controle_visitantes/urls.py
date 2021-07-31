from os import name
from django.contrib import admin
from django.urls import path

from usuarios.views import index
from visitantes.views import (registrar_visitantes , informacoes_visitante)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("registrar-visitante/" , registrar_visitantes , name="registrar_visitantes"),
    path("visitantes/<int:id>/", informacoes_visitante , name="informacoes_visitante")
]
