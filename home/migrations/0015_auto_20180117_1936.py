# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-17 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='propic',
            field=models.FileField(default=b'/static/home/images/default.png', upload_to=b''),
        ),
    ]