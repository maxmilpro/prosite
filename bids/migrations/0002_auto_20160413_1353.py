# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zip_code',
            field=models.IntegerField(blank=True),
        ),
    ]
