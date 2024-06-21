"""
URL configuration for REST project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# API/urls.py (archivo de la aplicación API)
from django.urls import path
from .views import crear_usuarios, lista_usuarios, actualizar_usuario, eliminar_usuario, autenticar_usuario, obtener_usuario_por_username

urlpatterns = [
    path('crear-usuario/', crear_usuarios, name='crear-usuario'),
    path('usuarios/', lista_usuarios, name='lista-usuarios'),
    path('actualizar-usuario/<int:usuario_id>/', actualizar_usuario, name='actualizar_usuario'),
    path('eliminar-usuario/<int:pk>/', eliminar_usuario, name='eliminar-usuario'),
    path('authenticate/', autenticar_usuario, name='autenticar-usuario'),
    path('usuario/<str:username>/', obtener_usuario_por_username, name='obtener-usuario-por-username')
]
