import pytest
from urls import *
import requests
import random
import string


@pytest.fixture(scope="function")
def courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    data_courier = {}

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        data_courier["login"]=login
        data_courier["password"]=password
        data_courier["first_name"]=first_name

    return data_courier

