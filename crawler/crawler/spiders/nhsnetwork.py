# -*- coding: utf-8 -*-
import scrapy


class NhsnetworkSpider(scrapy.Spider):
    name = 'nhsnetwork'
    allowed_domains = ['networks.nhs.uk']
    start_urls = ['https://www.networks.nhs.uk/events']

    def parse(self, response):
        for href in response.css('.sl a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_source)

    def parse_source(self, response):
        yield {
            'title': response.css('.vevent h1 span::text').extract(),
            'dtstart': response.css('.vevent .eventDetails tr td .dtstart').xpath('@title').extract(),
            'dtend': response.css('.vevent .eventDetails tr td .dtend').xpath('@title').extract(),
            'body': response.xpath('//div[contains(@id, "parent-fieldname-text")]//p/text()').extract(),
            'link': response.url,
            'link_source': response.css('.vevent p a.url::attr(href)').extract(),
        }
