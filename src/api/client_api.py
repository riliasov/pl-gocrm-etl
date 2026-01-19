import requests
from typing import Dict, Any, Optional
from src.config import CLIENT_API_URL, APP_TOKEN

class GoCRMAuthClient:
    def __init__(self, app_token: str = APP_TOKEN, base_url: str = CLIENT_API_URL):
        self.base_url = base_url
        self.app_token = app_token
        self.session = requests.Session()
        if self.app_token:
            self.session.headers.update({"APP_TOKEN": self.app_token})

    def set_access_token(self, access_token: str):
        """Установка Bearer токена вручную"""
        self.session.headers.update({"Authorization": f"Bearer {access_token}"})

    def login(self, phone: str, code: str = None, person: str = "client") -> Dict[str, Any]:
        """Авторизация пользователя (клиент или сотрудник)"""
        url = f"{self.base_url}/auth/login"
        payload = {
            "person": person,
            "login": phone
        }
        if code:
            payload["password"] = code
            
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        
        # Если авторизация успешна, сохраняем токен
        if data.get("status") == "success":
            token = data.get("data", {}).get("accessToken")
            if token:
                self.set_access_token(token)
        return data

    def get_profile(self) -> Dict[str, Any]:
        """Получение профиля текущего пользователя"""
        url = f"{self.base_url}/profile"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_clients(self, page: int = 1) -> Dict[str, Any]:
        """Получение списка клиентов (детей)"""
        url = f"{self.base_url}/clients"
        params = {"page": page}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
