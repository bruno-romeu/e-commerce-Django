from django.shortcuts import render, get_object_or_404
from velas.models import Produto, Categoria, Tamanho
from django.views.generic import ListView, TemplateView, DetailView

from velas.forms import ClienteModelForm
from django.http import JsonResponse

class HomeListView(ListView):
    model = Produto
    template_name = 'home.html'
    context_object_name = 'velas'


    def get_queryset(self):
        velas = super().get_queryset().order_by('essencia')
        search = self.request.GET.get('search')
        if search:
            velas = velas.filter(essencia__essencia__icontains=search)
        return velas

class SobreTemplateView(TemplateView):
    template_name = 'sobre.html'
    context_object_name = 'sobre'

def ContatoTemplateView(request):
    return render (request, 'contato.html')

def enviarFormulario(request):
    if request.method == 'POST':
        dados_cliente = ClienteModelForm(request.POST)
        if dados_cliente.is_valid():
            dados_cliente.save()
            return JsonResponse({'status': 'sucesso'})
    return JsonResponse({'status': 'erro'}, status=400)



def ProdutosCategoria(request, nome_categoria):
    categoria = get_object_or_404(Categoria, nome_categoria=nome_categoria)
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'produtos.html', {'produtos':produtos, 'categoria':categoria})


class PersonalizarTemplateView(TemplateView):
    template_name = 'personalizar.html'
    context_object_name = 'personalizar'


class ProdutoDetailView(DetailView):
    template_name = 'detail.html'
    model = Produto

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        produto = self.object
        tamanhos = produto.tamanhos.all()
        print(f'produto: {produto}, tamanhos: {tamanhos}')
        context['tamanhos_disponiveis'] = tamanhos
        return context
    

        cep_destino = self.request.GET.get("cep", "")
        cep_origem = "93800-120"

        if cep_destino:
            try:
                frete = calcular_frete(
                    cep_origem=cep_origem,
                    cep_destino=cep_destino,
                    peso=produto.peso,
                    formato=1,
                    comprimento=produto.comprimento,
                    altura=produto.altura,
                    largura=produto.largura,
                    servico=FRETE_SEDEX
                )
                context["frete"] = frete
            except Exception as e:
                context["frete_erro"] = f"Erro ao calcular frete: {e}"
        return context
    
    def ProdutosCategoria(request, nome_categoria):
        categoria = get_object_or_404(Categoria, nome_categoria=nome_categoria)
        produtos = Produto.objects.filter(categoria=categoria)
        return render(request, 'produtos.html', {'produtos':produtos, 'categoria':categoria})