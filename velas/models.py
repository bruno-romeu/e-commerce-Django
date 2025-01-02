from django.db import models

class Categoria(models.Model):
    id_cat = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.nome_categoria


class Tamanho(models.Model):
    id_tamanho = models.AutoField(primary_key=True)
    nome_tamanho = models.CharField(max_length=25, blank=True, null=True)
    peso = models.CharField(blank=True, null=True)
    altura = models.FloatField(default=5.0)
    diâmetro = models.FloatField(default=3.0)
    circunferência = models.FloatField(default=3.0)

    def __str__(self):
        return f'{self.nome_tamanho} - {self.peso}'


class Essencia(models.Model):
    id_essencia = models.AutoField(primary_key=True)
    essencia = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.essencia


class Produto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='vela_categoria')
    tamanhos = models.ManyToManyField(Tamanho, related_name='produto')
    essencia = models.ForeignKey(Essencia, on_delete=models.PROTECT, related_name='vela_esencia')
    valor = models.DecimalField(max_digits=10 ,decimal_places=2)
    descricao = models.TextField(max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to='velas/', blank=True, null=True)

    def __str__(self):
        return f'{self.categoria} - { self.essencia} - {self.descricao} - {self.foto}'


class Estoque(models.Model):
    quant_velas = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
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