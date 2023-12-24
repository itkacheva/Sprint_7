import allure
from services.register_new_courier import *
from urls import Urls


class TestOrderList:
    @allure.title(' Проверяем, что в тело ответа возвращается список заказов.')
    def test_get_order_list_successfull(self):
        response = requests.get(Urls.order_list_url, headers={'Content-Type': 'text/plain'})
        r = response.json()
        assert response.status_code == 200 and r["orders"] != []
