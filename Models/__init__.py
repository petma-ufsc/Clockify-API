from orator import DatabaseManager, Model


V1_API_URL = "https://api.clockify.me/api/v1"
WORKSPACE_ID = "5f68e99a69bb052125eda928" #id do workspace
HEADERS = {
    "X-Api-Key": "OGM5YTU4MzItNjU0NC00ODJiLThjYzAtM2RiNDQxNjE0YzBj", #colocar a chave da conta do PET no clockify
    "content-type": "application/json",
}

DB_HOSTNAME = '138.118.165.12' #ip do cpanel
DB_NAME = 'petma_clokify' #nome do banco de dados
DB_USERNAME = 'petma_clockify' #nome do usuario com acesso
DB_PASSWORD = "PET-MAmadruGa!10" #colocar senha

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


from models.member import Member
from models.category import Category
from models.project import Project
from models.activity import Activity
from models.time_entry import TimeEntry