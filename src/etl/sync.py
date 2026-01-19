from src.api.public_client import GoCRMPublicClient
from src.db.connection import SessionLocal, init_db
from src.db.models import City, Center, Lead, SyncLog
import datetime

class GoCRMDataSync:
    def __init__(self):
        self.public_client = GoCRMPublicClient()
        init_db()

    def sync_cities(self):
        """Синхронизация списка городов"""
        session = SessionLocal()
        try:
            cities_data = self.public_client.get_cities()
            for city_dict in cities_data:
                city = session.query(City).filter_by(id=city_dict['id']).first()
                if not city:
                    city = City(id=city_dict['id'])
                city.name = city_dict.get('name')
                city.alias = city_dict.get('alias')
                session.add(city)
            session.commit()
            print(f"Синхронизировано {len(cities_data)} городов")
        except Exception as e:
            session.rollback()
            print(f"Ошибка синхронизации городов: {e}")
        finally:
            session.close()

    def sync_centers(self, city_id: int):
        """Синхронизация центров для конкретного города"""
        session = SessionLocal()
        try:
            centers_data = self.public_client.get_centers(city_id)
            for center_dict in centers_data:
                center = session.query(Center).filter_by(id=center_dict['id']).first()
                if not center:
                    center = Center(id=center_dict['id'])
                center.name = center_dict.get('name') or center_dict.get('address')
                center.address = center_dict.get('address')
                center.city_id = city_id
                session.add(center)
            session.commit()
            print(f"Синхронизировано {len(centers_data)} центров")
        except Exception as e:
            session.rollback()
            print(f"Ошибка синхронизации центров: {e}")
        finally:
            session.close()

    def run_full_public_sync(self):
        """Полная синхронизация публичных данных"""
        print("Начало синхронизации...")
        self.sync_cities()
        
        # Получаем все города из БД и синхронизируем центры
        session = SessionLocal()
        cities = session.query(City).all()
        for city in cities:
            self.sync_centers(city.id)
        session.close()
        print("Синхронизация завершена.")

if __name__ == "__main__":
    syncer = GoCRMDataSync()
    syncer.run_full_public_sync()
