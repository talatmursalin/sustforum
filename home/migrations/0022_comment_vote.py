# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-24 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20180118_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
