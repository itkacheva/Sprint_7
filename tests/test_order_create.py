import allure
import pytest

from data import OrderData
from services.order_data import *
from services.register_new_courier import *
from urls import Urls


class TestOrderCreate:

    @allure.title(' Проверяем, различные варианты в поле "цвет".')
    @pytest.mark.parametrize('order_color', OrderData.order_color)
    def test_order_create_color_black_successfull(self, order_color):
        order_data = gen_order_data_and_return_it()
        order_data["color"] = order_color
        response = requests.post(Urls.order_create_url, data=order_data, headers={'Content-Type': 'text/plain'})
        assert response.status_code == 201

    @allure.title(' Проверяем, что тело ответа содержит track.')
    def test_order_create_successfull_respons_has_track(self):
        order_data = gen_order_data_and_return_it()
        response = requests.post(Urls.order_create_url, data=order_data, headers={'Content-Type': 'text/plain'})
        r = response.json()
        assert len(str(r["track"])) > 0