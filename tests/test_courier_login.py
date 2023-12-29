import allure
import pytest
from data import CourierLoginData
from endpoints.courier_endpoints import CourierAPI
from services.gen_courier_data import *


class TestCourierLogin:
    @allure.title('Проверяем, что курьер может авторизоваться.')
    @allure.description('Авторизуемся под ранее созданным пользователем , проверяем код ответа')
    def test_courier_login_successfull(self, courier):
        c = CourierAPI()
        response = c.create_login({"login": courier["login"], "password": courier["password"]})
        assert response.status_code == 200

    @allure.title('Проверяем, что система вернёт ошибку, если неправильно указать логин или пароль.')
    @allure.description('Авторизуемся под пользователем, указав неверный логин. Проверяем текст ответа')
    @pytest.mark.parametrize('courier_login, message', CourierLoginData.value_and_message)
    def test_courier_login_wrong_error_message(self, courier, courier_login, message):
        c = CourierAPI()
        response = c.create_login({"login": courier_login, "password": courier["password"]})
        r = response.json()
        assert r["message"] == message

    @allure.title('Проверяем, что если в поле "пароль" некорректное значение, запрос возвращает ошибку.')
    @allure.description('Авторизуемся под пользователем, указав неверный пароль. Проверяем текст ответа')
    @pytest.mark.parametrize('courier_password, message', CourierLoginData.value_and_message)
    def test_courier_password_wrong_error_message(self, courier, courier_password, message):
        c = CourierAPI()
        response = c.create_login({"login": courier["login"], "password": courier_password})
        r = response.json()
        assert r["message"] == message

    @allure.title(' Проверяем, что если нет поля "логин", запрос возвращает ошибку.')
    @allure.description('Авторизуемся под пользователем с пустым логином. Проверяем текст ответа')
    def test_courier_login_without_login_error_message(self, courier):
        c = CourierAPI()
        response = c.create_login({"login": "", "password": courier["password"]})
        r = response.json()
        assert response.status_code == 400 and r["message"] == 'Недостаточно данных для входа'


    @allure.title('Проверяем, что если нет поля "пароль", запрос возвращает ошибку.')
    @allure.description('Авторизуемся под пользователем с пустым паролем. Проверяем текст ответа')
    def test_courier_login_without_password_error_message(self, courier):
        c = CourierAPI()
        response = c.create_login({"login": courier["login"], "password": ""})
        r = response.json()
        assert response.status_code == 400 and r["message"] == 'Недостаточно данных для входа'


    @allure.title( 'Проверяем, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку.')
    @allure.description('Авторизуемся под несуществующим пользователем. Проверяем текст ответа')
    def test_non_exist_courier_login__error_message(self):
        courier_data = gen_courier_data()
        c = CourierAPI()
        response = c.create_login({"login": courier_data["login"]+'_1', "password": courier_data["password"]})
        r = response.json()
        assert r["message"] == 'Учетная запись не найдена'

    @allure.title('Проверяем, что успешный запрос возвращает id.')
    @allure.description('Авторизуемся и проверяем, что возвращается id')
    def test_courier_login_successfull_return_id(self, courier):
        c = CourierAPI()
        response = c.create_login({"login": courier["login"], "password": courier["password"]})
        r = response.json()
        assert len(str(r["id"])) > 0