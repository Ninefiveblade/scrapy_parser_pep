# Define your item pipelines here
#
# Don"t forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from collections import defaultdict
from pathlib import Path
import csv
import datetime as dt

from .constants import DATETIME_FORMAT

BASE_DIR = Path(__file__).parent
FILENAME = "status_summary_{}.csv"
RESULT_DIR = BASE_DIR / "results"
RESULT_DIR.mkdir(exist_ok=True)


class PepParsePipeline:
    """Класс пайплайна, получает item
    и сохраняет его в файл директории results."""

    def open_spider(self, spider):
        """Инициализируем счетчик статусов."""

        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        """Записываем статус и количество в словарь."""

        self.status_counter[item["status"]] += 1
        return item

    def close_spider(self, spider):
        """Записываем результаты в файл."""

        now = dt.datetime.now()
        file_name = FILENAME.format(now.strftime(DATETIME_FORMAT))
        file_path = RESULT_DIR / file_name
        with open(file_path, "w", encoding="utf-8") as file:
            writer = csv.writer(
                file, csv.unix_dialect, quoting=csv.QUOTE_MINIMAL
            )
            writer.writerows([
                ("Статус", "Количество"),
                *self.status_counter.items(),
                ("Total", sum(self.status_counter.values()))
            ])
