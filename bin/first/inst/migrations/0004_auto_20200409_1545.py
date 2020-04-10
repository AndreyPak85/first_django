# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2020-04-09 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0003_inst_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='inst',
            name='course',
        ),
        migrations.AddField(
            model_name='inst',
            name='courses',
            field=models.ManyToManyField(to='inst.Course'),
        ),
    ]
