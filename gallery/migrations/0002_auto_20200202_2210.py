# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-02 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gallery.Category'),
            preserve_default=False,
        ),
    ]
