import sys
import os

# Добавляем корень проекта в путь
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.etl.export import export_table_to_csv

if __name__ == "__main__":
    print("Экспорт данных...")
    export_table_to_csv('cities', 'exports/cities.csv')
    export_table_to_csv('centers', 'exports/centers.csv')
    print("Завершено.")
