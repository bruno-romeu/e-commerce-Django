# Generated by Django 5.0.8 on 2024-12-27 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velas', '0019_remove_tamanho_altura_remove_tamanho_comprimento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tamanho',
            name='altura',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tamanho',
            name='comprimento',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tamanho',
            name='largura',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tamanho',
            name='peso',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
