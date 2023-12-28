# Python проект - "Вычислитель отличий"
### Hexlet tests and linter status:
[![Actions Status](https://github.com/mkolotovich/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mkolotovich/python-project-50/actions)
[![Actions Status](https://github.com/mkolotovich/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/mkolotovich/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/32707a692daf0a9b9af2/maintainability)](https://codeclimate.com/github/mkolotovich/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/32707a692daf0a9b9af2/test_coverage)](https://codeclimate.com/github/mkolotovich/python-project-50/test_coverage)

## Описание
Вычислитель отличий – программа, определяющая разницу между двумя структурами данных. Это популярная задача, для решения которой существует множество онлайн сервисов, например http://www.jsondiff.com/. Подобный механизм используется при выводе тестов или при автоматическом отслеживании изменении в конфигурационных файлах.

Возможности утилиты:

* Поддержка разных входных форматов: yaml, json
* Генерация отчета в виде plain text, stylish и json

## Установка и запуск приложения 
1. Убедитесь, что у вас установлен Python версии 3.10 или выше. В противном случае установите Python версии 3.10 или выше.
2. Соберите пакет командой make build. Установите пакет в систему с помощью make package-install и убедитесь в том, что он работает, запустив gendiff -h в терминале. Команды make build и make package-install необходимо запускать из корневой директории проекта.
3. Пример использования:
    * формат plain - $ gendiff --format plain path/to/file.yml another/path/file.json
    * формат stylish - $ gendiff filepath1.json filepath2.json
    
[![asciicast](https://asciinema.org/a/GhSCrX2YvQRZIQlJr9mMJWL4n.svg)](https://asciinema.org/a/GhSCrX2YvQRZIQlJr9mMJWL4n)
[![asciicast](https://asciinema.org/a/Ru97Hh4P4squxSVi6JEboxXjc.svg)](https://asciinema.org/a/Ru97Hh4P4squxSVi6JEboxXjc)
[![asciicast](https://asciinema.org/a/pbmx0bv2FwEHefvNov0PN8CGa.svg)](https://asciinema.org/a/pbmx0bv2FwEHefvNov0PN8CGa)
[![asciicast](https://asciinema.org/a/0JJEciU9AAot4okTcTUI4k7cy.svg)](https://asciinema.org/a/0JJEciU9AAot4okTcTUI4k7cy)
[![asciicast](https://asciinema.org/a/UKvQmtF0TpT2MVlKcob1tfNfk.svg)](https://asciinema.org/a/UKvQmtF0TpT2MVlKcob1tfNfk)