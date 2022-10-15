from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Объявляем паука и создаем атрибуты."""

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse_pep(self, response):
        """Собираем информацию с полученных страниц."""

        data = {
            'number': response.css('.page-title::text').get().split(' ')[1],
            'name': response.css('.page-title::text').get(),
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)

    def parse(self, response):
        """Собираем все ссылки на страницы."""

        all_hrefs = response.css('#numerical-index a::attr(href)').getall()
        for href in all_hrefs:
            yield response.follow(
                urljoin(self.start_urls[0], href),
                callback=self.parse_pep
            )
