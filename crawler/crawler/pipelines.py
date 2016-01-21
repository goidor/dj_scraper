# -*- coding: utf-8 -*-


class NhsPipeline(object):

    def process_item(self, item, spider):
        item.save()
        return item
