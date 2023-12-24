import allure
from services.gen_courier_data import *
from services.register_new_courier import *
from urls import Urls


class TestCourierCreate:
    @allure.title(' Проверяем, что курьера можно создать.')
    def test_courier_create_successfull(self):
        courier_data = gen_courier_data_and_return_login_password()
        response = requests.post(Urls.create_courier_url, data=courier_data)
        print(courier_data)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title(' Проверяем, что нельзя создать двух одинаковых курьеров.')
    def test_create_two_identical_couriers_status_code_409(self):
        courier_data = {}
        courier_data["login"], courier_data["password"], courier_data["firstName"] = register_new_courier_and_return_login_password()
        response = requests.post(Urls.create_courier_url, data=courier_data)
        assert response.status_code == 409

    @allure.title(' Проверяем, создание курьера передав только обязательные поля.')
    def test_courier_create_only_required_fields_successfull(self):
        courier_data = gen_courier_data_and_return_login_password()
        response = requests.post(Urls.create_courier_url, data={"login": courier_data["login"], "password": courier_data["password"]})
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title(' Проверяем, что запрос возвращает правильный код ответа.')
    def test_courier_create_status_code_201(self):
        courier_data = gen_courier_data_and_return_login_password()
        response = requests.post(Urls.create_courier_url, data=courier_data)
        assert response.status_code == 201

    @allure.title(' Проверяем, что успешный запрос возвращает "ok":true.')
    def test_courier_create_response_ok_true(self):
        courier_data = gen_courier_data_and_return_login_password()
        response = requests.post(Urls.create_courier_url, data=courier_data)
        print (response.text)
        assert response.text == '{"ok":true}'

    @allure.title(' Проверяем, что если нет обязательного поля "логин", запрос возвращает ошибку.')
    def test_courier_create_without_login_error_message(self):
        courier_data = gen_courier_data_and_return_login_password()
        response = requests.post(Urls.create_courier_url, data={"password": courier_data["password"], "firstName": courier_data["firstName"]})
        r = response.json()
        assert r["message"] == 'Недостаточно данных для создания учетной записи'

    @allure.title(' Проверяем, что если нет обязательного поля "пароль", запрос возвращает ошибку.')
    def test_courier_create_without_password_error_message(self):
        courier_data = gen_courier_data_and_return_login_password()
        response = requests.post(Urls.create_courier_url, data={"login": courier_data["login"], "firstName": courier_data["firstName"]})
        r = response.json()
        assert r["message"] == 'Недостаточно данных для создания учетной записи'

    @allure.title(' Проверяем, что если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_create_two_identical_couriers_error_message(self):
        courier_data = {}
        courier_data["login"], courier_data["password"], courier_data["firstName"] = register_new_courier_and_return_login_password()
        response = requests.post(Urls.create_courier_url, data=courier_data)
        r = response.json()
        assert r["message"] == 'Этот логин уже используется. Попробуйте другой.'