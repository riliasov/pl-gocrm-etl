import requests
from typing import Optional, Dict, Any, List

class GoCRMPublicClient:
    """
    Клиент для Public API (v3).
    Используется для отправки заявок с сайта.
    """
    def __init__(self, base_url: str = "https://planetabb.go-crm.ru/api/v3"):
        self.base_url = base_url.rstrip("/")

    def send_via_webhook(self, webhook_url: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Отправка заявки через Webhook (Integration Plugin).
        Полезно, если вы хотите использовать готовые интеграции (инструкции из CRM).
        
        Args:
            webhook_url: Полный URL вебхука (например, .../api/v1/plugins/5/lead)
            data: Данные формы
        """
        try:
            # Вебхуки могут ожидать form-data или json. Пробуем json по умолчанию.
            response = requests.post(webhook_url, data=data) # Часто вебхуки любят form-data
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def send_lead(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Отправка новой заявки (POST /leads).
        
        Args:
            data: Словарь с данными заявки.
                  Обязательные поля (обычно): name, phone, center_id, birthday.
        
        Returns:
            Ответ от API в виде словаря.
        """
        url = f"{self.base_url}/leads"
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            # Возвращаем тело ошибки, если оно есть, чтобы видеть validation_errors
            try:
                return e.response.json()
            except ValueError:
                raise e

    def get_cities(self) -> List[Dict[str, Any]]:
        """Получение списка городов (GET /cities)."""
        url = f"{self.base_url}/cities"
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('data', [])

    def get_centers(self, city_id: int) -> List[Dict[str, Any]]:
        """Получение центров в городе (GET /cities/{id}/centers)."""
        url = f"{self.base_url}/cities/{city_id}/centers"
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('data', [])

    def get_users(self, center_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """Получение списка сотрудников (GET /users)."""
        url = f"{self.base_url}/users"
        params = {}
        if center_id:
            params["centerId"] = center_id
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get('data', [])

class GoCRMAuthClient:
    """
    Клиент для Client API.
    Используется для авторизации пользователей и доступа к личному кабинету.
    """
    def __init__(self, app_token: str, base_url: str = "https://planetabb.go-crm.ru/api"):
        self.base_url = base_url.rstrip("/")
        self.app_token = app_token
        self.session = requests.Session()
        # APP_TOKEN передается в заголовке для всех запросов
        self.session.headers.update({"APP_TOKEN": self.app_token})

    def login(self, phone: str, code: str = None) -> Dict[str, Any]:
        """
        Авторизация пользователя (POST /auth/login).
        
        Если передать только phone - придет SMS.
        Если передать phone + code - произойдет вход (получение токенов).
        """
        url = f"{self.base_url}/auth/login"
        payload = {
            "person": "client", # или 'user' для сотрудников
            "login": phone
        }
        if code:
            payload["password"] = code
            
        response = requests.post(url, json=payload, headers=self.session.headers)
        # Обратите внимание: API может возвращать 422 при неверном коде, 
        # но мы хотим видеть тело ответа
        if response.status_code not in [200, 201]:
             # Логируем или просто возвращаем json для отладки
             pass
             
        return response.json()

    def set_access_token(self, access_token: str):
        """
        Установка Bearer токена для авторизованных запросов.
        Вызывается после успешного login.
        """
        self.session.headers.update({"Authorization": f"Bearer {access_token}"})

    def get_profile(self) -> Dict[str, Any]:
        """
        Получение профиля текущего пользователя (GET /profile).
        Требует установленного access_token.
        """
        url = f"{self.base_url}/profile"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_clients(self) -> Dict[str, Any]:
        """
        Получение списка клиентов, привязанных к аккаунту (GET /clients).
        Полезно для родителей, у которых несколько детей.
        """
        url = f"{self.base_url}/clients"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

# --- ПРИМЕР ИСПОЛЬЗОВАНИЯ ---
if __name__ == "__main__":
    import json
    
    print("--- 1. TEST PUBLIC API (Leads & Info) ---")
    public_client = GoCRMPublicClient()
    
    # 1.1 Получение списка городов и центров (чтобы узнать center_id)
    # cities = public_client.get_cities()
    # print("Cities:", json.dumps(cities, indent=2, ensure_ascii=False))
    
    # Если известен ID города (например, из списка выше), получаем центры
    # CITY_ID = 1 
    # centers = public_client.get_centers(CITY_ID)
    # print(f"Centers in city {CITY_ID}:", json.dumps(centers, indent=2, ensure_ascii=False))

    # 1.2 Получение списка сотрудников
    users = public_client.get_users()
    print("Users (Employees):", json.dumps(users, indent=2, ensure_ascii=False))

    # 1.3 Пример данных заявки
    lead_data = {
        "name": "Тестовый Ребенок",
        "phone": "+79990000000",
        "center_id": 1,         # ВАЖНО: Укажите реальный ID центра
        "birthday": "2015-01-01",
        "comment": "Проверка интеграции"
    }
    
    # Раскомментируйте для отправки:
    # res = public_client.send_lead(lead_data)
    # print("Lead sending result:", json.dumps(res, indent=2, ensure_ascii=False))


    print("\n--- 2. TEST CLIENT API (Auth & Profile) ---")
    # ВАЖНО: Этот токен нужно получить у администратора CRM
    YOUR_APP_TOKEN = "INSERT_YOUR_APP_TOKEN_HERE" 
    
    auth_client = GoCRMAuthClient(app_token=YOUR_APP_TOKEN)
    
    # Шаг 1: Запрос SMS
    PHONE = "79998887766" # Номер телефона клиента
    # login_res = auth_client.login(phone=PHONE)
    # print("Login Step 1 (SMS req):", login_res)
    
    # Шаг 2: Ввод кода (полученного по СМС)
    # CODE = "1234" 
    # login_res_2 = auth_client.login(phone=PHONE, code=CODE)
    # print("Login Step 2 (Tokens):", login_res_2)
    
    # Если вход успешен, берем токен и делаем запросы
    # if login_res_2.get("status") == "success":
    #     tokens = login_res_2["data"]
    #     access_token = tokens["accessToken"]
    #     print("Access Token received:", access_token[:10] + "...")
        
    #     auth_client.set_access_token(access_token)
        
    #     # Получаем профиль
    #     profile = auth_client.get_profile()
    #     print("Profile:", json.dumps(profile, indent=2, ensure_ascii=False))
