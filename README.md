# InstaParse / ИнстаПарс

InstaParse is a Python-based project designed for scraping Instagram followers of a given user. This tool helps you
extract the followers list of any public Instagram account, leveraging both Selenium and Instagram's API.

InstaParse — это проект на Python, предназначенный для парсинга подписчиков Instagram указанного пользователя. Этот
инструмент помогает извлекать список подписчиков любого публичного аккаунта Instagram, используя Selenium и API
Instagram.

## Features / Особенности

- Automated authentication to Instagram using Selenium.
- Extract followers of any public Instagram account.
- Use of saved cookies for seamless subsequent logins.

- Автоматическая аутентификация в Instagram с помощью Selenium.
- Извлечение подписчиков любого публичного аккаунта Instagram.
- Использование сохранённых cookie для упрощённого повторного входа.

## Prerequisites / Требования

Before using InstaParse, make sure you have installed the following:

Перед использованием InstaParse убедитесь, что у вас установлено следующее:

- Python 3.8+
- Google Chrome browser
- Google ChromeDriver

You also need the following Python packages:

Вам также понадобятся следующие Python-пакеты:

- `requests`
- `python-decouple`
- `instagrapi`

To install the dependencies, run:

Чтобы установить зависимости, выполните:

```sh
pip install requests instagrapi python-decouple
```

## Getting Started / Начало работы

1. **Clone the Repository / Клонируйте репозиторий**

   ```sh
   git clone https://github.com/RObotiaga/instaparse.git
   cd instaparse
   ```

2. **Set Up Environment Variables / Настройте переменные окружения**

   Create a `.env` file in the root directory of the project and provide your Instagram credentials:

   Создайте файл `.env` в корневом каталоге проекта и укажите ваши данные для входа в Instagram:

   ```env
   LOGIN=your_instagram_username
   PASSWORD=your_instagram_password
   ```

3. **Run the Script / Запустите скрипт**

   Execute the `test.py` script to start extracting followers:

   Выполните скрипт `test.py`, чтобы начать извлечение подписчиков:

   ```sh
   python test.py
   ```

   The script will prompt you to enter the Instagram username of the target account and the number of followers you want
   to retrieve.

   Скрипт запросит у вас имя пользователя Instagram целевого аккаунта и количество подписчиков, которые вы хотите
   получить.

