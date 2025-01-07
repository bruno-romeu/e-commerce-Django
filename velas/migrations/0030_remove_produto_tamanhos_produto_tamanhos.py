# Generated by Django 5.0.8 on 2025-01-07 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velas', '0029_auto_20250106_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='tamanhos',
        ),
        migrations.AddField(
            model_name='produto',
            name='tamanhos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='produto', to='velas.tamanho'),
            preserve_default=False,
        ),
    ]
