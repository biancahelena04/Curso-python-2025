import requests

cep = input("entre com um cep: ")

url = "https://viacep.com.br/ws/{cep}/json/"
 
resposta = requests.get(url.format(cep=cep))

if resposta.status_code == 200:
    print(resposta.json())
    