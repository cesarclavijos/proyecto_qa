import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


BASE_URL = os.getenv("APP_BASE_URL", "https://spendwise-igs.eastus2.cloudapp.azure.com:4430")
EMAIL = os.getenv("ADMIN_EMAIL", "")
PASSWORD = os.getenv("ADMIN_PASSWORD", "")
API_BASE_URL = os.getenv("API_APP_BASE_URL", "https://spendwise-igs.eastus2.cloudapp.azure.com:4530/api/v1/")


TOKEN_URL = os.getenv("SPENDWISE_GATE_COOKIE", "")


# Compuerta HTTP Basic Auth delante del sitio y del endpoint de token
GATE_USER = os.getenv("SPENDWISE_GATE_USER", "")
GATE_PASSWORD = os.getenv("SPENDWISE_GATE_PASS", "")
