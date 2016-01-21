# -*- coding: utf-8 -*-
import scrapy


class RcplondonSpider(scrapy.Spider):
    name = 'rcplondon'
    allowed_domains = ['www.rcplondon.ac.uk']
    start_urls = ['https://www.rcplondon.ac.uk/events']

    def parse(self, response):
        for href in response.css('.view-content a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_source)

    def parse_source(self, response):
        yield {
            'title': response.css('.second-row .content-title h1::text').extract(),
            'excerpt': response.css('.content-content .field-name-body p::text').extract(),
            'body': response.css('.content-content .content .content p::text').extract(),
            'organizer': response.css('.view-content h4::text').extract(),
            'email': response.css('.view-content .content .field-name-field-address::text').extract()[1],
            'phone': response.css('.view-content .content .field-name-field-telephone::text').extract()[1],
            'tags': response.css('.content-content .group-tags a::text').extract(),
            'link': response.url,
        }
