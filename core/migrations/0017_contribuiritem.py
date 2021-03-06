# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 00:56
from __future__ import unicode_literals

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20171009_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContribuirItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='texto')),
                ('imagem', django_resized.forms.ResizedImageField(crop=None, keep_meta=False, quality=75, size=[1920, 790], upload_to='contribuir_itens')),
            ],
            options={
                'verbose_name': 'contribuir item',
                'verbose_name_plural': 'contribuir itens',
            },
        ),
    ]
