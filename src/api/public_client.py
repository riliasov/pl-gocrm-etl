import requests
from typing import Dict, Any, List, Optional
from src.config import PUBLIC_API_URL

class GoCRMPublicClient:
    def __init__(self, base_url: str = PUBLIC_API_URL):
        self.base_url = base_url

    def send_lead(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Отправка новой заявки в ЦРМ"""
        url = f"{self.base_url}/leads"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def send_via_webhook(self, webhook_url: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Отправка заявки через вебхук плагина"""
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        return response.json()

    def get_cities(self) -> List[Dict[str, Any]]:
        """Получение списка городов"""
        url = f"{self.base_url}/cities"
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("data", [])

    def get_centers(self, city_id: int) -> List[Dict[str, Any]]:
        """Получение списка центров для города"""
        url = f"{self.base_url}/cities/{city_id}/centers"
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("data", [])

    def get_users(self, center_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Получение списка сотрудников"""
        url = f"{self.base_url}/users"
        params = {}
        if center_id:
            params["centerId"] = center_id
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get("data", [])
