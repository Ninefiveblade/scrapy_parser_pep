from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem

PEP_DOMAIN = 'peps.python.org'
PEP_URL = 'https://{}/'


class PepSpider(scrapy.Spider):
    """Объявляем паука и создаем атрибуты."""

    name = 'pep'
    allowed_domains = [PEP_DOMAIN]
    start_urls = [PEP_URL.format(PEP_DOMAIN)]

    def parse_pep(self, response):
        """Собираем информацию с полученных страниц."""
        page_title = response.css('.page-title::text')
        data = {
            'number': page_title.get().split(' ')[1],
            'name': page_title.get(),
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)

    def parse(self, response):
        """Собираем все ссылки на страницы."""

        all_hrefs = response.css('#numerical-index a::attr(href)').getall()
        for href in all_hrefs:
            yield response.follow(
                urljoin(PEP_URL.format(PEP_DOMAIN), href),
                callback=self.parse_pep
            )
