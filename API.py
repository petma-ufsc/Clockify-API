import requests
import json

headers = {"content-type":"application/json","X-Api-Key":"XtlQUamKcGgmLvLD"} #parâmetros da requisição
                                                                             #(esse X-Api-Key é do meu perfil)
url = "https://api.clockify.me/api/v1/user" #url da base do clockify

r = requests.get(url,headers=headers)

data = r.json()

print(data['name'])