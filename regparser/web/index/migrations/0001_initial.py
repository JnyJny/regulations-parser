# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 23:01
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dependency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DependencyNode',
            fields=[
                ('label', models.CharField(max_length=512, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='dependency',
            name='depender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depends_on', to='index.DependencyNode'),
        ),
        migrations.AddField(
            model_name='dependency',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_of', to='index.DependencyNode'),
        ),
    ]