# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-17 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20180117_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='firstname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lastname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profession',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]