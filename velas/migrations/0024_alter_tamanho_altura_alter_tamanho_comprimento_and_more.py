# Generated by Django 5.0.8 on 2024-12-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velas', '0023_alter_tamanho_altura_alter_tamanho_comprimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamanho',
            name='altura',
            field=models.CharField(default='altura padrao'),
        ),
        migrations.AlterField(
            model_name='tamanho',
            name='comprimento',
            field=models.CharField(default=' comprimento padrao'),
        ),
        migrations.AlterField(
            model_name='tamanho',
            name='largura',
            field=models.CharField(default='largura padrao'),
        ),
        migrations.AlterField(
            model_name='tamanho',
            name='peso',
            field=models.CharField(default='peso padrao'),
        ),
    ]
