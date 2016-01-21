# -*- coding: utf-8 -*-

import scrapy

from scrapy_djangoitem import DjangoItem

from scraper.models import Nhsnetwork


class NhsItem(DjangoItem):
    django_model = Nhsnetwork
    # name = scrapy.Field()
