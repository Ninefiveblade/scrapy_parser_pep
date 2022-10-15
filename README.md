# scrapy_parser_pep
Парсинг PEP страниц.
Парсит страницы python, имеет возможность сохранять в файл
выводить Pretty Table

# Технологии
Scrapy.

# Подготовка к запуску проекта:
Необходимо установить виртуальное окружение:
```python3.9 -m venv venv```
Установить зависимости:
```source venv/bin/activate```
```(venv) $ pip install -r requirements```

# Запуск парсера:
## pep-psrse
Выполните 
``` (venv) scrapy crawl 'имя паука' ```
# Запуск тестов:
## Из корневой директории проекта:
```(venv) $ pytest```

# Лицензия:
[LICENSE MIT](LICENSE)