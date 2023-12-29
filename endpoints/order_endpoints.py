import requests
from urls import Urls


class OrderAPI:
    def create_order(self, order_data):
        response = requests.post(Urls.service_url + Urls.order_create_url, data=order_data,
                                 headers={'Content-Type': 'text/plain'})
        return response

    def get_order_list(self):
        response = requests.get(Urls.service_url + Urls.order_list_url, headers={'Content-Type': 'text/plain'})
        return response