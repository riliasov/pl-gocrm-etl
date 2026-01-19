import os
from dotenv import load_dotenv

load_dotenv()

GO_CRM_DOMAIN = os.getenv("GO_CRM_DOMAIN", "planetabb.go-crm.ru")
APP_TOKEN = os.getenv("APP_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/gocrm.db")

PUBLIC_API_URL = f"https://{GO_CRM_DOMAIN}/api/v3"
CLIENT_API_URL = f"https://{GO_CRM_DOMAIN}/api"
