import requests
from dotenv import load_dotenv

load_dotenv()  # читает .env


class YougileApi():
    def __init__(self, token):
        self.base_url = "https://yougile.com"
        self.token = token

    def my_headers(self):
        # Заголовки для всех запросов
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        # Создание проекта
        path = '/api-v2/projects'
        data = {"title": title}
        resp = requests.post(
            self.base_url+path, headers=self.my_headers(), json=data
        )
        return resp

    def get_project_list(self):
        # Получение списка проектов
        path = '/api-v2/projects'
        resp = requests.get(
            self.base_url+path, headers=self.my_headers()
        )
        return resp

    def edit_project(self, id, new_title):
        # Изменение проекта
        path = '/api-v2/projects/'
        project = {
            "title": new_title
        }
        resp = requests.put(
            self.base_url+path + str(id),
            headers=self.my_headers(), json=project
        )
        return resp

    def get_project_by_id(self, id):
        path = '/api-v2/projects/'
        resp = requests.get(
            self.base_url+path + str(id), headers=self.my_headers()
        )
        return resp
