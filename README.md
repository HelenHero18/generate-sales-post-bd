h1 **Проект для курса Simulative Автоматизация и деплой**
---
h2 Описание
---
Скрипт generate_shops генерирует N (кол-во магазинов) выгрузок в формате csv в папку data/. Скрипт run считывает данные о продажах и заносит в базу данных.
---
h3 Содержание репозитория
---
Название файла   | Содержание файла
---------------- |----------------------
data             | Папка, куда сохраняются выгрузки
img              | Папка со скринами создания БД в dbeaver и автоматическом выполнении скрипта generate_shops планировщиком Windows
sql              | DDL-команды создания таблиц  в dbeaver
.gitignore       | лишние файлы для git
config.ini       |Файл с константными значениями
generate_shops.py|Скрипт, генерирующий выгрузки
pgdb.py          |Класс для создания БД
requirements.txt |Используемые библиотеки
run.py           |Скрип, считывает данные о продажах и заносит в базу данных
start.bat        |Файл для планировщика Windows
---
h3 Запуск проекта на новой машине
---
1. Скачать репозиторий
2. Открыть в среде программирования
3. В терминале активировать виртуальное окружение
4. Установить в окружение используемые библиотеки pip install -r requirements.txt
5. Запустить скрипт generate_shops.py
6. Запустить скрипт run.py  
