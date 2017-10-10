# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 00:01
from __future__ import unicode_literals

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170929_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuemSomos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitulo', models.TextField(max_length=200, verbose_name='subtítulo')),
                ('texto_destaque', models.TextField(max_length=500)),
                ('imagem', django_resized.forms.ResizedImageField(crop=None, keep_meta=False, quality=75, size=[1920, 790], upload_to='quem_somos')),
            ],
            options={
                'verbose_name_plural': 'quem somos',
            },
        ),
        migrations.AlterField(
            model_name='memoria',
            name='descricao',
            field=models.TextField(max_length=500, verbose_name='descrição'),
        ),
    ]