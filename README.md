# InstaParse / ИнстаПарс

InstaParse is a Python-based project designed for scraping Instagram followers of a given user. This tool helps you extract the followers list of any public Instagram account, leveraging both Selenium and Instagram's API.

InstaParse — это проект на Python, предназначенный для парсинга подписчиков Instagram указанного пользователя. Этот инструмент помогает извлекать список подписчиков любого публичного аккаунта Instagram, используя Selenium и API Instagram.

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
- `selenium`
- `selenium-wire`
- `python-dotenv`

To install the dependencies, run:

Чтобы установить зависимости, выполните:

```sh
pip install requests selenium selenium-wire python-dotenv
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

   Execute the `main.py` script to start extracting followers:

   Выполните скрипт `main.py`, чтобы начать извлечение подписчиков:

   ```sh
   python main.py
   ```

   The script will prompt you to enter the Instagram username of the target account and the number of followers you want to retrieve.

   Скрипт запросит у вас имя пользователя Instagram целевого аккаунта и количество подписчиков, которые вы хотите получить.

## Project Structure / Структура проекта

- `main.py` - The main script that coordinates the process of follower extraction.
- `selenium_utils.py` - Contains functions for Instagram login and follower header extraction using Selenium.
- `utils.py` - Contains helper functions for obtaining user IDs.

- `main.py` — основной скрипт, который координирует процесс извлечения подписчиков.
- `selenium_utils.py` — содержит функции для входа в Instagram и извлечения заголовков подписчиков с помощью Selenium.
- `utils.py` — содержит вспомогательные функции для получения ID пользователей.

## How It Works / Как это работает

1. **Authentication / Аутентификация**: The script uses Selenium to log in to Instagram. If cookies are available, it attempts to use them for authentication, avoiding repeated manual logins.

   Скрипт использует Selenium для входа в Instagram. Если cookies доступны, он пытается использовать их для аутентификации, избегая повторного ручного входа.

2. **Followers Extraction / Извлечение подписчиков**: After login, the script navigates to the specified user's followers list and extracts data using Instagram's API requests.

   После входа в систему скрипт переходит к списку подписчиков указанного пользователя и извлекает данные с помощью запросов к API Instagram.

## Note / Примечание

- This tool is for educational purposes only. Scraping or automating Instagram without permission may violate Instagram's terms of service.

- Этот инструмент предназначен только для образовательных целей. Парсинг или автоматизация Instagram без разрешения могут нарушать условия использования Instagram.

## License / Лицензия

This project is open-source and available under the [MIT License](LICENSE).

Этот проект с открытым исходным кодом и доступен под [лицензией MIT](LICENSE).

## Disclaimer / Отказ от ответственности

Use responsibly. The authors are not liable for any misuse of this tool.

Используйте ответственно. Авторы не несут ответственности за неправильное использование этого инструмента.
