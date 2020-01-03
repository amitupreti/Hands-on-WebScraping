# -*- coding: utf-8 -*-
import scrapy


class HashtagSpider(scrapy.Spider):
    name = 'hashtag'
    allowed_domains = ['twiter.com']
    start_urls = ['http://twiter.com/']

    def parse(self, response):
        pass
