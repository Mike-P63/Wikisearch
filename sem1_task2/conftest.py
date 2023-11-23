import pytest
import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

Session = requests.Session()

@pytest.fixture()
def user_login():
    result = Session.post(url=data['url'], data={'username': data['login'], 'password': data['pswd']})
    response_json = result.json()
    token = response_json.get('token')
    return token


@pytest.fixture()
def get_description():
    return 'New_blog_for_HW_1'

@pytest.fixture()
def post_title():
    return 'TestTitle' 






# url = "https://test-stand.gb.ru/gateway/login"
# login = "AlenaK"
# password = "d02d48181c"


# result = requests.post(url=url, data={"username": login, "password": password})
# token = result.json()["token"]

# res_get = requests.get(url=" https://test-stand.gb.ru/api/posts", headers={"X-Auth-Token": token}, params={"owner":"notMe"})
# print(res_get)
# print(res_get.json())