# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nhsnetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('dtstart', models.DateTimeField(null=True)),
                ('dtend', models.DateTimeField(null=True)),
                ('body', models.TextField()),
                ('link', models.URLField()),
                ('link_source', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rcplondon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('organizer', models.CharField(max_length=255, null=True)),
                ('excerpt', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='rcplondon',
            name='tags',
            field=models.ManyToManyField(to='scraper.Tag'),
        ),
    ]
