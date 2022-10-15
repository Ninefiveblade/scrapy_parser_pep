# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PepParseItem(scrapy.Item):
    """Объявляем поля объектов, с которыми
    будет работать пайплайн."""

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
