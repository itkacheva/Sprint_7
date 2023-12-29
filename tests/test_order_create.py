import allure
import pytest
from data import OrderData
from endpoints.order_endpoints import OrderAPI
from services.order_data import *


class TestOrderCreate:
    @allure.title('Проверяем, различные варианты в поле "цвет".')
    @allure.description('Авторизуемся и проверяем, что возвращается id')
    @pytest.mark.parametrize('order_color', OrderData.order_color)
    def test_order_create_color_black_successfull(self, order_color):
        order_data = gen_order_data_and_return_it()
        order_data["color"] = order_color
        order = OrderAPI()
        response = order.create_order(order_data)
        assert response.status_code == 201

    @allure.title(' Проверяем, что тело ответа содержит track.')
    @allure.description('Авторизуемся и проверяем тело ответа')
    def test_order_create_successfull_respons_has_track(self):
        order_data = gen_order_data_and_return_it()
        order = OrderAPI()
        response = order.create_order(order_data)
        assert len(str(response.json()["track"])) > 0