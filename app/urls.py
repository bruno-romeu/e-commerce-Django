from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from velas.views import HomeListView, SobreTemplateView,ContatoTemplateView, enviarFormulario, ProdutosCategoria, PersonalizarTemplateView, ProdutoDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeListView.as_view(), name='home'),
    path('sobre/', SobreTemplateView.as_view(), name='sobre'),
    path('contato/', ContatoTemplateView, name='contato'),
    path('enviar_formulario/', enviarFormulario, name='enviar_formulario'),
    path('produto/<str:nome_categoria>/', ProdutosCategoria, name='produtos'),
    path('personalizar/', PersonalizarTemplateView.as_view(), name='personalizar'),
    path('detail/<int:pk>/', ProdutoDetailView.as_view(), name='detail'),
    path('accounts/', include("accounts.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
