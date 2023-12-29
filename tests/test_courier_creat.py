import allure
from endpoints.courier_endpoints import CourierAPI
from services.gen_courier_data import *


class TestCourierCreate:
    @allure.title(' Проверяем, что курьера можно создать.')
    @allure.description('Создаем курьера, проверяем статус и текст ответа')
    def test_courier_create_successfull(self):
        courier_data = gen_courier_data()
        c = CourierAPI()
        response = c.create_courier(courier_data)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title(' Проверяем, что нельзя создать двух одинаковых курьеров.')
    @allure.description('Создаем курьера повторно, проверяем статус ответа')
    def test_create_two_identical_couriers_status_code_409(self, courier):
        c = CourierAPI()
        response = c.create_courier(courier)
        assert response.status_code == 409

    @allure.title('Проверяем, создание курьера передав только обязательные поля.')
    @allure.description('Создаем курьера, передав только логин и пароль.')
    def test_courier_create_only_required_fields_successfull(self):
        courier_data = gen_courier_data()
        c = CourierAPI()
        response = c.create_courier({"login": courier_data["login"], "password": courier_data["password"]})
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверяем, что запрос возвращает правильный код ответа.')
    @allure.description('Создаем курьера и проверяем код ответа')
    def test_courier_create_status_code_201(self):
        courier_data = gen_courier_data()
        c = CourierAPI()
        response = c.create_courier(courier_data)
        assert response.status_code == 201

    @allure.title('Проверяем, что успешный запрос возвращает "ok":true.')
    @allure.description('Создаем курьера и текст ответа')
    def test_courier_create_response_ok_true(self):
        courier_data = gen_courier_data()
        c = CourierAPI()
        response = c.create_courier(courier_data)
        assert response.text == '{"ok":true}'

    @allure.title('Проверяем, что если нет обязательного поля "логин", запрос возвращает ошибку.')
    @allure.description('Создаем курьера, не передав обязательное поле и проверяем текст ошибки')
    def test_courier_create_without_login_error_message(self):
        courier_data = gen_courier_data()
        c = CourierAPI()
        response = c.create_courier({"password": courier_data["password"], "firstName": courier_data["firstName"]})
        r = response.json()
        assert r["message"] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Проверяем, что если нет обязательного поля "пароль", запрос возвращает ошибку.')
    @allure.description('Создаем курьера, не передав обязательное поле и проверяем текст ошибки')
    def test_courier_create_without_password_error_message(self):
        courier_data = gen_courier_data()
        c = CourierAPI()
        response = c.create_courier({"login": courier_data["login"], "firstName": courier_data["firstName"]})
        r = response.json()
        assert r["message"] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Проверяем, что если создать пользователя с логином, который уже есть, возвращается ошибка.')
    @allure.description('Создаем курьера повторно и проеряем текст ошибки')
    def test_create_two_identical_couriers_error_message(self, courier):
        c = CourierAPI()
        response = c.create_courier(courier)
        r = response.json()
        assert r["message"] == 'Этот логин уже используется. Попробуйте другой.'