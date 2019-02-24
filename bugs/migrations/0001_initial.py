# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-24 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('completed_date', models.DateTimeField()),
                ('upvotes', models.IntegerField(default=0)),
                ('status', models.CharField(default='To do', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contents', models.TextField()),
                ('user', models.TextField(default='unknown')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('bug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bug', to='bugs.Bug')),
            ],
        ),
    ]
