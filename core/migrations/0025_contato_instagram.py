# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_remove_contato_dicas_reciclagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='instagram',
            field=models.URLField(default='www.instagram.com/jsellos'),
            preserve_default=False,
        ),
    ]
