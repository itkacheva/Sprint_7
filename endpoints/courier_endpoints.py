import requests
from urls import Urls


class CourierAPI:
    def create_courier(self, courier_data):
        response = requests.post(Urls.service_url + Urls.create_courier_url, data=courier_data)
        return response

    def create_login(self, courier_data):
        response = requests.post(Urls.service_url + Urls.login_courier_url, data=courier_data)
        return response