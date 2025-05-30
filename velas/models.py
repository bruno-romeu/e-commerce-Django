from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    id_cat = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=25, default='nome_categoria')

    def __str__(self):
        return self.nome_categoria
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Tamanho(models.Model):
    id_tamanho = models.AutoField(primary_key=True)
    nome_tamanho = models.CharField(max_length=25, blank=True, null=True)
    peso = models.CharField(blank=True, null=True)
    altura = models.FloatField(default=5.0)
    diâmetro = models.FloatField(default=3.0)
    circunferência = models.FloatField(default=3.0)

    def __str__(self):
        return f'{self.nome_tamanho} - {self.peso}'
    
    class Meta:
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanhos'


class Essencia(models.Model):
    id_essencia = models.AutoField(primary_key=True)
    nome_essencia = models.CharField(max_length=25, default='nome essencia')

    def __str__(self):
        return self.nome_essencia
    
    class Meta:
        verbose_name = 'Essência'
        verbose_name_plural = 'Essências'


class Produto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='vela_categoria')
    tamanhos = models.ForeignKey(Tamanho, related_name='produto', on_delete=models.PROTECT, default='tamanho')
    essencia = models.ManyToManyField(Essencia)
    valor = models.DecimalField(max_digits=10 ,decimal_places=2, default=0)
    descricao = models.TextField(max_length=200, blank=True, null=True)
    foto = models.ImageField(upload_to='velas/', blank=True, null=True)

    def __str__(self):
        return f'{self.id_prod}'
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Estoque(models.Model):
    quant_velas = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'
        ordering =  ['created_at']

    
class Destaques(models.Model):
    id = models.AutoField(primary_key=True)
    destaque = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='prod_destaque')


class Clientes(models.Model):
    id_cli = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Número = models.CharField(max_length=11)
    Mensagem = models.TextField(max_length=1000, default='')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carrinho', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Carrinho de {self.usuario.username if self.usuario else 'Cliente Anônimo'}'
    
    def total(self):
        return sum(item.subtotal() for item in self.itens.all())
    
    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.quantidade}x {self.produto.id_prod} - R$ {self.preco_unitario}"

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens do Carrinho'