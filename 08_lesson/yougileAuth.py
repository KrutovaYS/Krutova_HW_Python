import requests
import os
from dotenv import load_dotenv

load_dotenv()


class YougileAuth:
    # Только для получения company_id и создания ключа API
    def __init__(self):
        self.base_url = "https://yougile.com"
        self.login = os.getenv("YOUGILE_LOGIN")
        self.password = os.getenv("YOUGILE_PASSWORD")

    def get_company_id(self):
        # Получение ID компании по логину/паролю
        path = '/api-v2/auth/companies'
        auth_data = {
            "login": self.login,
            "password": self.password
        }

        resp = requests.post(
            f"{self.base_url}{path}",
            json=auth_data
        )

        if resp.status_code not in [200, 201]:
            raise Exception(f"Ошибка получения компаний: {resp.status_code}")
        return resp.json()["content"][0]["id"]

    def create_token(self):
        # Создание нового ключа API
        path = '/api-v2/auth/keys'
        company_id = self.get_company_id()

        key_data = {
            "login": self.login,
            "password": self.password,
            "companyId": company_id
        }

        resp = requests.post(
            f"{self.base_url}{path}", json=key_data
        )

        if resp.status_code not in [200, 201]:
            raise Exception(f"Ошибка создания ключа: {resp.status_code}")

        return resp.json()["key"]
