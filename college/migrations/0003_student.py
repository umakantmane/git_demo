# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-15 04:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_auto_20180215_0437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pincode', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
