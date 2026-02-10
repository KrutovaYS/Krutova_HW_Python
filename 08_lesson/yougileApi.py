import requests


class YougileApi():
    def __init__(self):
        self.base_url = "https://yougile.com/api-v2"
        # ЗДЕСЬ НУЖНО ВСТАВИТЬ КЛЮЧ -->ДЛЯ НАСТАВНИКА<--
        self.key = "Вставить ключ"

    def my_headers(self):
        # Заголовки для всех запросов
        return {
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        # Создание проекта
        data = {"title": title}
        resp = requests.post(
            self.base_url+'/projects', headers=self.my_headers(), json=data
        )
        return resp

    def get_project_list(self):
        # Получение списка проектов
        resp = requests.get(
            self.base_url+'/projects', headers=self.my_headers()
        )
        return resp

    def edit_project(self, id, new_title):
        # Изменение проекта
        project = {
            "title": new_title
        }
        resp = requests.put(
            self.base_url+'/projects/' + str(id),
            headers=self.my_headers(), json=project
        )
        return resp

    def get_project_by_id(self, id):
        resp = requests.get(
            self.base_url+'/projects/' + str(id), headers=self.my_headers()
        )
        return resp
