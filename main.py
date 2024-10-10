import requests
from utils import get_user_id
from selenium_utils import parse_followers_headers
from decouple import config

account_name = input('Введите ник пользователя инстаграм ')


def parse_followers(followers_count):
    payload = {}
    account_id = get_user_id(config("LOGIN"), config("PASSWORD"), account_name, )
    headers = parse_followers_headers(config("LOGIN"), config("PASSWORD"), account_name,
                                      account_id)
    user_list = ''
    max_id = '0%7CQVFBbUM5VktpRTM2aXZodzJ5ZktPTlBoeklvdVoxYWhVSDdaZ0lMckZkZ3N3cS1HNG8zd1ZFN3NMZWtGcjRicmctUXlsT1BCdTFFOWRFOHQtaXNZeVd4MA%3D%3D'
    try:
        while True:
            url = f"https://www.instagram.com/api/v1/friendships/{account_id}/followers/?search_surface=follow_list_page&count=25&max_id={max_id}"
            response = requests.request("GET", url, headers=headers, data=payload)
            print(response.text)
            for i in response.json()["users"]:
                user_list = user_list + f"{i['username']}:{i['full_name']};"
            max_id = response.json()["next_max_id"]
            if len(user_list) > int(followers_count):
                break
    except KeyboardInterrupt:
        return user_list
    return user_list


result = parse_followers(input('Введите количество подписчиков '))
print(result)
