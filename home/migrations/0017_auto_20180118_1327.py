# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-18 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20180117_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='color',
            field=models.CharField(default=b'#fff', max_length=255),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='firstname',
            field=models.CharField(default=b'not set', max_length=255),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lastname',
            field=models.CharField(default=b'not set', max_length=255),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='propic',
            field=models.FileField(default=b'/static/home/images/default.jpg', upload_to=b''),
        ),
    ]