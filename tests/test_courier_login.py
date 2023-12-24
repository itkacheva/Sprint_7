import allure
import pytest

from data import CourierLoginData
from services.gen_courier_data import *
from services.register_new_courier import *
from urls import Urls


class TestCourierLogin:
    @allure.title(' Проверяем, что курьер может авторизоваться.')
    def test_courier_login_successfull(self):
        courier_data = {}
        courier_data["login"], courier_data["password"], courier_data["firstName"] = register_new_courier_and_return_login_password()
        response = requests.post(Urls.login_courier_url, data={"login": courier_data["login"], "password": courier_data["password"]})
        assert response.status_code == 200

    @allure.title(' Проверяем, что система вернёт ошибку, если неправильно указать логин или пароль.')
    @pytest.mark.parametrize('courier_login, message', CourierLoginData.value_and_message)
    def test_courier_login_wrong_error_message(self, courier_login, message):
        courier_data = {}
        courier_data["login"], courier_data["password"], courier_data["firstName"] = register_new_courier_and_return_login_password()
        response = requests.post(Urls.login_courier_url, data={"login": courier_login, "password": courier_data["password"]})
        r = response.json()
        assert r["message"] == message

    @allure.title(' Проверяем, что если в поле "пароль" некорректное значение, запрос возвращает ошибку.')
    @pytest.mark.parametrize('courier_password, message', CourierLoginData.value_and_message)
    def test_courier_password_wrong_error_message(self, courier_password, message):
        courier_data = {}
        courier_data["login"], courier_data["password"], courier_data["firstName"] = register_new_courier_and_return_login_password()
        response = requests.post(Urls.login_courier_url, data={"login": courier_data["login"], "password": courier_password})
        r=response.json()
        assert r["message"] == message

    @allure.title(' Проверяем, что если нет поля "логин", запрос возвращает ошибку.')
    def test_courier_login_without_login_error_message(self):
        courier_data = {}
        courier_data["login"], courier_data["password"], courier_data["firstName"] = register_new_courier_and_return_login_password()
        response = requests.post(Urls.login_courier_url, data={"login": "", "password": courier_data["password"]})
        r = response.json()
        assert response.status_code == 400 and r["message"] == 'Недостаточно данных для входа'


    @allure.title(' Проверяем, что если нет поля "пароль", запрос возвращает ошибку.')
    def test_courier_login_without_password_error_message(self):
        courier_data = {}
        courier_data["login"], courier_data["password"], courier_data["firstName"] = register_new_courier_and_return_login_password()
        response = requests.post(Urls.login_courier_url, data={"login": courier_data["login"], "password": ""})
        r = response.json()
        assert response.status_code == 400 and r["message"] == 'Недостаточно данных для входа'


    @allure.title(' Проверяем, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку.')
    def test_non_exist_courier_login__error_message(self):
        courier_data = gen_courier_data_and_return_login_password()
        response = requests.post(Urls.login_courier_url, data={"login": courier_data["login"]+'_1', "password": courier_data["password"]})
        r = response.json()
        assert r["message"] == 'Учетная запись не найдена'

    @allure.title(' Проверяем, что успешный запрос возвращает id.')
    def test_courier_login_successfull_return_id(self):
        courier_data = {}
        courier_data["login"], courier_data["password"], courier_data["firstName"] = register_new_courier_and_return_login_password()
        response = requests.post(Urls.login_courier_url, data={"login": courier_data["login"], "password": courier_data["password"]})
        r = response.json()
        assert len(str(r["id"])) > 0