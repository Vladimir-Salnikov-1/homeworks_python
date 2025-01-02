import requests
from classes.Data_for_tests import Log


class Authtorization:

    def __init__(self):
        pass

    # Получть список компаний по логину и паролю
    def get_list_company_by_login(self, login, password):
        self.login = login
        self.password = password
        headers = {
            "Content-Type": "application/json"
            }
        payload = {
            "login": self.login,
            "password": self.password
            }
        respons = requests.post(Log.base_url + "auth/companies", headers=headers, json=payload)
        body_respons = respons.json()
        return body_respons

    # Получить список ключей
    def get_list_keys(self, login, password, id_company):
        self.login = login
        self.password = password
        self.id_company = id_company
        headers = {
            "Content-Type": "application/json"
            }
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": id_company
            }
        respons = requests.post(Log.base_url + "auth/keys/get", headers=headers, json=payload)
        body_respons = respons.json()
        return body_respons

    # Получить 2 ключ от первой компании (номер ключа менять в 9 строке метода)
    def get_key_of_company(self, login, password, serial_number_company):
        self.login = login
        self.password = password
        self.serial_number_company = serial_number_company - 1
        object = Authtorization()
        list_company = object.get_list_company_by_login(self.login, self.password)
        id_company1 = list_company['content'][self.serial_number_company]['id'] 
        list_keys = object.get_list_keys(self.login, self.password, id_company1)
        key = list_keys[1]["key"]
        return key

    # Создать новый ключ
    def create_new_key(self, login, password, id_company):
        self.login = login
        self.password = password
        self.id_company = id_company
        headers = {
            "Content-Type": "application/json"
            }
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": self.id_company
            }
        respons = requests.post(Log.base_url + "auth/keys", headers=headers, json=payload)
        body_respons = respons.json()
        return body_respons

    def delete_key(self, key):
        self.key = key
        headers = {
            "Content-Type": "application/json"
            }
        respons = requests.delete(Log.base_url + f"auth/keys/{self.key}", headers=headers)
        body_respons = respons.json()
        return body_respons
