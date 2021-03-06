# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_contribuiritem_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='coleta',
            new_name='id_dica_coleta',
        ),
        migrations.RenameField(
            model_name='dica',
            old_name='dthora',
            new_name='dt_hora',
        ),
        migrations.RenameField(
            model_name='dica',
            old_name='idCat',
            new_name='id_cat',
        ),
        migrations.RenameField(
            model_name='noticia',
            old_name='dthora',
            new_name='dt_hora',
        ),
        migrations.RenameField(
            model_name='noticia',
            old_name='idCat',
            new_name='id_cat',
        ),
        migrations.AddField(
            model_name='dica',
            name='texto_destaque',
            field=models.TextField(default='texto de destaque', max_length=200, verbose_name='texto de destaque'),
            preserve_default=False,
        ),
    ]
