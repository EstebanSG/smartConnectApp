"""SmartConnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from apps.convocatorias import views
from django.conf.urls import url, include

from django.conf import settings
from django.conf.urls.static import static





from django.urls import reverse_lazy
from django.contrib.auth.views import (
    
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
#include('haystack.urls')
app_name = "convocatorias"
urlpatterns = [
    path('inicio/', views.index_view, name='home'),
    path('result/', views.search_view, name='search'),
    path('admin/', admin.site.urls),
    path('misconvocatorias/', views.misconvocatorias_view, name='misconvocatorias'),
    path('registro/', views.registrarse_view, name='registro'),
    path('cregistro/', views.registrarse2_view, name='registro2'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('editar/', views.editarperfil_view, name='editarperfil'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('', LoginView.as_view(template_name='index.html'), name='login'),
    path('misconvocatorias/(?P<pk>\d+)/', views.agregarConvocatoriaCliente, name="agregarConvocatoriaCliente"),
    path('misconvocatoriasn/(?P<pk>\d+)/', views.eliminarConvocatoriaCliente, name='eliminarConvocatoriaCliente'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
