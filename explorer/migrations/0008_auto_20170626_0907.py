# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 09:07


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0007_query_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
