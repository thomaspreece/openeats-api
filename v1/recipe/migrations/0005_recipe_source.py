# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-28 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20161126_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='source',
            field=models.CharField(blank=True, max_length=200, verbose_name='course'),
        ),
    ]
