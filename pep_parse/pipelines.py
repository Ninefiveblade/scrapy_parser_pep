# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from collections import defaultdict
from pathlib import Path
import csv
import datetime as dt

from .constants import DATETIME_FORMAT

BASE_DIR = Path(__file__).parent


class PepParsePipeline:
    """Класс пайплайна, получает item
    и сохраняет его в файл директории results."""

    def __init__(self):
        """Инициализируем словарь, куда будут
        сохранятся PEP и количество статусов."""

        self.cnt_status = defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        """Записываем статус и количество в словарь."""

        if item['status'] is not None:
            self.cnt_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        """Записываем результаты в файл."""

        results_dir = BASE_DIR / "results"
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f"status_summary_{now_formatted}.csv"
        file_path = results_dir / file_name
        with open(file_path, "w", encoding="utf-8") as file:
            writer = csv.writer(file, csv.unix_dialect)
            file.write('Статус,Количество\n')
            writer.writerows(self.cnt_status.items())
            file.write(f'Total,{sum(self.cnt_status.values())}\n')
