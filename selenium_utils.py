import os
import pickle

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


def auth_instagram(driver, login, password):
    url = 'https://www.instagram.com'
    driver.get(url)

    wait = WebDriverWait(driver, 20)
    username_input = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    username_input.send_keys(login)

    password_input = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    password_input.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
    login_button.click()

    try:
        save_data_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]')))
        save_data_button.click()
    except:
        print("Кнопка сохранения данных не найдена, продолжаем без неё.")

    return driver


def parse_followers_headers(login, password, account_name, account_id):
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)

    if os.path.exists("cookies.pkl"):
        print("Загружаем куки из файла...")
        with open("cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)

        # Перезагружаем страницу с загруженными куки
        driver.refresh()

        # Проверяем, залогинен ли пользователь
        driver.get('https://www.instagram.com/')
        if "login" in driver.current_url:
            print("Куки устарели или некорректны. Выполняем аутентификацию вручную.")
            driver = auth_instagram(driver, login, password)
        else:
            print("Куки успешно восстановлены, пользователь залогинен.")
    else:
        print("Файл с куки не найден, проводим аутентификацию...")
        driver = auth_instagram(driver, login, password)
    # Переходим на страницу пользователя
    driver.get(f"https://www.instagram.com/{account_name}/")

    # Дожидаемся кнопки с количеством подписчиков и кликаем на нее
    follower_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             '//a[contains(@href,"/followers/")]')))
    follower_button.click()

    # Ожидаем запрос API на получение подписчиков
    try:
        request = driver.wait_for_request(
            f'/api/v1/friendships/{account_id}/followers/',
            100)
        return request.headers
    except Exception as e:
        print(f"Не удалось перехватить запрос на получение подписчиков: {e}")
    driver.quit()


def parse_account_headers(login, password, account_name):
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)
    if os.path.exists("cookies.pkl"):
        print("Загружаем куки из файла...")
        with open("cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)

        driver.refresh()

        # Проверяем, залогинен ли пользователь
        driver.get('https://www.instagram.com/')
        if "login" in driver.current_url:
            print("Куки устарели или некорректны. Выполняем аутентификацию вручную.")
            driver = auth_instagram(driver, login, password)
        else:
            print("Куки успешно восстановлены, пользователь залогинен.")
    else:
        print("Файл с куки не найден, проводим аутентификацию...")
        driver = auth_instagram(driver, login, password)

    # Сохраняем куки после успешной аутентификации
    # with open("cookies.pkl", "wb") as f:
    #     pickle.dump(driver.get_cookies(), f)

    driver.get(f"https://www.instagram.com/{account_name}/")

    try:
        request = driver.wait_for_request(f'/{account_name}/', 100)
        return request.headers
    except Exception as e:
        print(f"Не удалось перехватить запрос на получение подписчиков: {e}")
    driver.quit()
