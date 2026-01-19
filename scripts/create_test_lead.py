import sys
import os

# Добавляем корень проекта в путь
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.api.public_client import GoCRMPublicClient

def create_test_lead():
    client = GoCRMPublicClient()
    
    # Данные для тестового лида
    # center_id = 1 (Планета - Давлеткильдеева 16, как мы выяснили ранее)
    lead_data = {
        "fio": "Тестовый Родитель",
        "name": "Тестовый Ребенок",
        "phone": "+79001112233",
        "center_id": 1,
        "birthday": "01.01.2015",
        "comment": "Тестовая заявка из скрипта ETL"
    }
    
    try:
        print(f"Отправка тестового лида: {lead_data['name']}...")
        result = client.send_lead(lead_data)
        print("Успех!")
        print(f"ID лида в системе: {result.get('data', {}).get('id')}")
        print(f"Статус: {result.get('data', {}).get('status')}")
    except Exception as e:
        print(f"Ошибка при создании лида: {e}")

if __name__ == "__main__":
    create_test_lead()
