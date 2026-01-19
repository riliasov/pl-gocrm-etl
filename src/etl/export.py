import pandas as pd
from src.db.connection import engine
import os

def export_table_to_csv(table_name: str, export_path: str):
    """Экспорт таблицы в CSV файл"""
    try:
        df = pd.read_sql_table(table_name, engine)
        os.makedirs(os.path.dirname(export_path), exist_ok=True)
        df.to_csv(export_path, index=False)
        print(f"Данные из {table_name} экспортированы в {export_path}")
    except Exception as e:
        print(f"Ошибка экспорта {table_name}: {e}")

if __name__ == "__main__":
    # Пример использования
    export_table_to_csv('cities', 'exports/cities.csv')
    export_table_to_csv('centers', 'exports/centers.csv')
