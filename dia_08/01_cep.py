#%%

# import requests

# url = "https://viacep.com.br/ws/14300140/json/"

# resposta = requests.get(url)

# dados = resposta.json()

# dados

# #%%
# type(dados)

import requests #para realizar requisiçoes na web
import json # para tratar de listas/dicionarios para arquivos json
from tqdm import tqdm #tqdm mede o progresso
import pandas as pd

ceps = [
    "14302140", 
       "14300023", 
       "14300033", 
       "14300001", 
       "14300005", 
       "14300025"
       ]

url = "https://viacep.com.br/ws/{cep}/json/"
dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados
#%%
dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

#%%
with open("ceps.json", "w", encoding = 'utf-8') as open_file:
    json.dump(dados, open_file,ensure_ascii=False, indent=4)

 # %%
