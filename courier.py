import requests
import configuration
import data

def login_courier():
    return requests.post(configuration.URL_SERVICE + configuration.COURIER_LOGIN , data.courier_data)



def create_courier():
    return requests.post(configuration.URL_SERVICE + configuration.CURIER_CREATE , data.create_data)


response = login_courier()
print(response.json())