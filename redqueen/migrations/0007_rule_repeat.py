# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-26 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redqueen', '0006_rule'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='repeat',
            field=models.CharField(default='no', max_length=200),
        ),
    ]