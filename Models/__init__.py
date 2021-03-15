from orator import DatabaseManager, Model
import os


V1_API_URL = "https://api.clockify.me/api/v1"
WORKSPACE_ID = os.getenv("CLOCKIFY_WORKSPACE_ID") #colocar id do workspace (5f68e99a69bb052125eda928)
HEADERS = {
    "X-Api-Key": os.getenv("CLOCKIFY_API_KEY"), #colocar a chave da conta do PET no clockify
    "content-type": "application/json",
}

DB_HOSTNAME = '138.118.165.12' #ip do cpanel
DB_NAME = 'petma_clokify' #nome do banco de dados
DB_USERNAME = 'petma_clockify' #nome do usuario com acesso
DB_PASSWORD = os.getenv("DB_PASSWORD") #colocar senha

CONFIG = {
    "mysql": {
        "driver": "mysql",
        "host": DB_HOSTNAME,
        "database": DB_NAME,
        "user": DB_USERNAME,
        "password": DB_PASSWORD,
        "prefix": "",
    }
}

db = DatabaseManager(CONFIG)
Model.set_connection_resolver(db)

from .project import Project