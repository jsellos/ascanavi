# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 01:13
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_contribuir'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contribuir',
            options={'verbose_name': 'contribuir', 'verbose_name_plural': 'contribuir'},
        ),
        migrations.AlterField(
            model_name='contribuir',
            name='imagem',
            field=django_resized.forms.ResizedImageField(crop=None, keep_meta=False, quality=75, size=[1920, 790], upload_to='contribuir'),
        ),
        migrations.AlterField(
            model_name='nossahistoria',
            name='imagem',
            field=django_resized.forms.ResizedImageField(crop=None, keep_meta=False, quality=75, size=[1920, 790], upload_to='nossa_historia'),
        ),
        migrations.AlterField(
            model_name='quemsomos',
            name='imagem',
            field=django_resized.forms.ResizedImageField(crop=None, keep_meta=False, quality=75, size=[1920, 790], upload_to='C:\\Users\\jonat\\OneDrive\\Sellos Sistemas\\Sistemas\\ascanavi.org.br\\ascanavi\\mediaquem_somos'),
        ),
    ]