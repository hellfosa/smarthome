# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-28 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('redqueen', '0009_auto_20170628_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
