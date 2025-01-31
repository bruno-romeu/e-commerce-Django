"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from velas.views import HomeListView, SobreTemplateView,ContatoTemplateView, enviarFormulario, ProdutosCategoria, PersonalizarTemplateView, ProdutoDetailView
from velas.models import Categoria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeListView.as_view(), name='home'),
    path('sobre/', SobreTemplateView.as_view(), name='sobre'),
    path('contato/', ContatoTemplateView, name='contato'),
    path('enviar_formulario/', enviarFormulario, name='enviar_formulario'),
    path('produto/<str:nome_categoria>/', ProdutosCategoria, name='produtos'),
    path('personalizar/', PersonalizarTemplateView.as_view(), name='personalizar'),
    path('detail/<int:pk>/', ProdutoDetailView.as_view(), name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
