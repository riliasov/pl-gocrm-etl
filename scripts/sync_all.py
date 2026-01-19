import sys
import os

# Добавляем корень проекта в путь
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.etl.sync import GoCRMDataSync

if __name__ == "__main__":
    syncer = GoCRMDataSync()
    syncer.run_full_public_sync()
