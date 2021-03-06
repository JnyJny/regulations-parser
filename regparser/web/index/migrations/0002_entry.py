# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 19:50
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('label', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='index.DependencyNode')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('contents', models.BinaryField()),
            ],
            options={
                'ordering': ['label'],
            },
        ),
    ]
