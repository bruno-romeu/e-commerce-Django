from django.contrib import admin
from velas.models import Categoria
from velas.models import Produto
from velas.models import Tamanho
from velas.models import Essencia
from velas.models import Estoque

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_categoria',)
    search_fields = ('categoria',)

class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('nome_tamanho', 'peso', 'altura', 'diâmetro', 'circunferência')
    search_fields = ('nome_tamanho',)

class EssenciaAdmin(admin.ModelAdmin):
    list_display = ('essencia',)
    search_fields = ('essencia',)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'exibir_tamanhos',  'essencia', 'descricao', 'foto')
    search_fields = ('categoria', 'essencia')

    def exibir_tamanhos(self, obj):
        return ", ".join([tamanho.peso and tamanho.nome_tamanho for tamanho in obj.tamanhos.all()])
    exibir_tamanhos.short_description = 'Tamanhos Disponíveis'

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('quant_velas',)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Tamanho, TamanhoAdmin)
admin.site.register(Essencia, EssenciaAdmin)
admin.site.register(Estoque, EstoqueAdmin)