from django.shortcuts import render, get_object_or_404, redirect
from velas.models import Produto, Categoria, Tamanho
from django.views.generic import ListView, TemplateView, DetailView
from velas.forms import ClienteModelForm
from brazilcep import get_address_from_cep, exceptions
from .utils import calcular_frete_melhor_envio
from django.http import JsonResponse
import json


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
        essencia = produto.essencia.all()
        print(f'produto: {produto}, essencia: {essencia}')
        context['essencias_disponiveis'] = essencia

        tamanho = produto.tamanhos
    

        cep_destino = self.request.GET.get("cep", "").strip()
        cep_origem = "93800-120"

        if cep_destino:
            if tamanho:
                try:
                    fretes = calcular_frete_melhor_envio(
                        cep_origem=cep_origem,
                        cep_destino=cep_destino,
                        peso=tamanho.peso,
                        diâmetro=tamanho.diâmetro,
                        altura=tamanho.altura,
                        circunferência=tamanho.circunferência,
                    )

                    serviços_disponíveis = []
                    for frete in fretes:
                        if frete.get('price') and frete.get('delivery_time'):
                            serviços_disponíveis.append({
                                'servico':frete['name'],
                                'preco':frete['price'],
                                'prazo':frete['delivery_time']
                            })

                    context["frete"] = serviços_disponíveis
                except Exception as e:
                    try:
                        erro_data = json.loads(str(e))
                        erros = erro_data.get("errors", {})
                        mensagens=  []

                        for campo, mensagem_lista in erros.items():
                            mensagens.append(f'{mensagem_lista[0]}')
                        msg_erro = " ".join(mensagens) if mensagens else "Ocorreu um erro desconhecido."
                    except:
                        msg_erro = 'Informe um CEP válido para calcular o frete.'
                    
                    context['frete_erro'] = msg_erro
            else:
                context["frete_erro"] = "Nenhum tamanho disponível ou CEP não informado."
        return context
    
    def ProdutosCategoria(request, nome_categoria):
        categoria = get_object_or_404(Categoria, nome_categoria=nome_categoria)
        produtos = Produto.objects.filter(categoria=categoria)
        return render(request, 'produtos.html', {'produtos':produtos, 'categoria':categoria})




