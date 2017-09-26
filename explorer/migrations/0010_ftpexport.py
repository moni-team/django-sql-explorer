# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-21 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0009_auto_20170628_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='FTPExport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=30)),
                ('folder_path', models.CharField(max_length=200)),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explorer.Query')),
            ],
        ),
    ]