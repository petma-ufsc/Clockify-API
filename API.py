import requests
import json
import numpy
import pandas as pd
from pandas import json_normalize
from orator import DatabaseManager
import MySQLdb

headers = {"content-type":"application/json","X-Api-Key":"XtlQUamKcGgmLvLD"} #parâmetros da requisição
                                                                             #(esse X-Api-Key é do meu perfil)
url = "https://api.clockify.me/api/v1/workspaces/5f68e99a69bb052125eda928/user/5ed53cc88092f06db0220ac9/time-entries" #url da base do clockify

r = requests.get(url,headers=headers)

data = r.json()
data = json_normalize(data)



config = {
    'mysql': {
        'driver': 'mysql',
        'host': '138.118.165.12',
        'database': 'petma_clokify',
        'user': 'petma_clockify',
        'password': 'PET-MAmadruGa!10',
        'prefix': ''
    }
}

db = DatabaseManager(config)