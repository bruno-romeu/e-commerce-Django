# Generated by Django 5.0.8 on 2024-12-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velas', '0024_alter_tamanho_altura_alter_tamanho_comprimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamanho',
            name='altura',
            field=models.CharField(blank=True, default='altura padrao', null=True),
        ),
        migrations.AlterField(
            model_name='tamanho',
            name='comprimento',
            field=models.CharField(blank=True, default='comprimento padrao', null=True),
        ),
        migrations.AlterField(
            model_name='tamanho',
            name='largura',
            field=models.CharField(blank=True, default='largura padrao', null=True),
        ),
        migrations.AlterField(
            model_name='tamanho',
            name='peso',
            field=models.CharField(blank=True, default='peso padrao', null=True),
        ),
    ]
