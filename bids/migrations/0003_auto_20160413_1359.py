# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0002_auto_20160413_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='zip_code',
            field=models.IntegerField(null=True),
        ),
    ]
