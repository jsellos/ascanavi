# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_contribuiritem'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribuiritem',
            name='titulo',
            field=models.CharField(default=':-) Comprar o livro', max_length=200, verbose_name='título'),
            preserve_default=False,
        ),
    ]
