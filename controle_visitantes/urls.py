from os import name
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from dashboard.views import index
from visitantes.views import (registrar_visitantes , informacoes_visitante , finalizar_visita)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name = "login.html") , name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name = "logout.html") , name="logout"),
    path("", index, name="index"),
    path("registrar-visitante/" , registrar_visitantes , name="registrar_visitantes"),
    path("visitantes/<int:id>/", informacoes_visitante , name="informacoes_visitante"),
    path("visitantes/<int:id>/finalizar-visita" , finalizar_visita , name="finalizar_visita")
]
