import allure
from endpoints.order_endpoints import OrderAPI


class TestOrderList:
    @allure.title('Проверяем, что в тело ответа возвращается список заказов.')
    @allure.description('Запрашиваем список заказов')
    def test_get_order_list_successfull(self):
        order = OrderAPI()
        response = order.get_order_list()
        assert response.status_code == 200 and response.json()["orders"] != []
