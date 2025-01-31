from django.contrib import admin
from velas.models import Categoria
from velas.models import Produto
from velas.models import Tamanho
from velas.models import Essencia
from velas.models import Estoque
from velas.models import Destaques

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_categoria',)
    search_fields = ('categoria',)

class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('nome_tamanho', 'peso', 'altura', 'diâmetro', 'circunferência')
    search_fields = ('nome_tamanho',)

class EssenciaAdmin(admin.ModelAdmin):
    list_display = ('nome_essencia',)
    search_fields = ('nome_essencia',)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'exibir_essencias',  'tamanhos', 'descricao', 'foto')
    search_fields = ('categoria', 'tamanhos')

    def exibir_essencias(self, obj):
        return ", ".join([essencia.nome_essencia for essencia in obj.essencia.all()])
    exibir_essencias.short_description = 'Tamanhos Disponíveis'

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('quant_velas',)

class DestaqueAdmin(admin.ModelAdmin):
    list_display = ('destaque',)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Tamanho, TamanhoAdmin)
admin.site.register(Essencia, EssenciaAdmin)
admin.site.register(Estoque, EstoqueAdmin)
admin.site.register(Destaques, DestaqueAdmin)