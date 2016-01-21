# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Nhsnetwork(models.Model):
    title = models.CharField(max_length=255)
    dtstart = models.DateTimeField(null=True)
    dtend = models.DateTimeField(null=True)
    body = models.TextField()
    link = models.URLField()
    link_source = models.URLField(null=True)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Rcplondon(models.Model):
    title = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255, null=True)
    excerpt = models.TextField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100, null=True)
    tags = models.ManyToManyField(Tag)
    link = models.URLField()
