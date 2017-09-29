# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class ExampleSpider(scrapy.Spider):
    name = 'example'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']

    def start_requests(self):
        a = [
            'https://www.costco.com/SleepBetter-Beyond-Down%C2%AE-Fiber-Bed.product.100227357.html?catalogId=10701&langId=-1&storeId=10301&krypto=6pJXw%2B8iqYuuNvKaJ4Rx9JEWW6EIlFkmy7%2BbQ5CgaDXDDDcPKkbjXCjiKXVHPs41AsaJUfScVMupZb6E0rq5MpicenwuIRp1aL4xacEiW0o%3D'

        ]
        for url in a:
            yield SplashRequest(
                url=url,
                # headers={
                #     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
                #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                #     'Accept-Language': 'en-US,en;q=0.5',
                #     'Accept-Encoding': 'gzip, deflate, br',
                #
                #
                #     'Upgrade-Insecure-Requests': '1',
                #     'Cache-Control': 'max-age=0',
                # },
                endpoint='render.html',
                args={
                    'proxy': 'https://35.185.80.76:3128',
                    'iframes': 1, 'wait': 5, 'html': 1, 'script': 1},
                callback=self.parse_item
            )

    def parse_item(self, response):
        print(response.xpath('//select[@class="varis form-control valid"]').extract())
        print(response.body)