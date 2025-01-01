import requests
from classes.Data_for_tests import Log


class Project:
    def __init__(self):
        pass

    def create_project(self, title, key):
        self.key = key
        self.title = title
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}"
            }
        payload = {
            "title": self.title
            }
        respons = requests.post(Log.base_url + "projects", headers=headers, json=payload)
        respons_body = respons.json()
        return respons_body

    def delete_project(self, id_project, key):
        self.id_project = id_project
        self.key = key
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}"
            }
        payload = {
            "deleted": True
        }
        respons = requests.put(Log.base_url + "projects/" + self.id_project, headers=headers, json=payload)
        body_respons = respons.json()
        return body_respons

    def get_list_projects(self, key):
        self.key = key
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}"
            }
        respons = requests.get(Log.base_url + "projects", headers=headers)
        body_respons = respons.json()
        return body_respons

    def get_project_by_id(self, id_project, key):
        self.key = key
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}"
            }
        respons = requests.get(Log.base_url + "projects/" + id_project, headers=headers)
        body_respons = respons.json()
        return body_respons

    def change_title_project(self, id_project, new_title, key):
        self.id_project = id_project
        self.key = key
        self.new_title = new_title
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}"
            }
        payload = {
            "title": self.new_title
        }
        respons = requests.put(Log.base_url + "projects/" + self.id_project, headers=headers, json=payload)
        body_respons = respons.json()
        return body_respons
