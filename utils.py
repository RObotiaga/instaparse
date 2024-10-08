import requests
from selenium_utils import parse_account_headers


def get_user_id(login, password, username):
    url = f"https://www.instagram.com/{username}/"
    payload = {}
    headers = parse_account_headers(login, password, username)
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.text.find('"props":')
    return ''.join(filter(str.isdigit, response.text[r:r + 30]))
