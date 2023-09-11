import requests


response = requests.get('https://viacep.com.br/ws/01001000/json/')
data = response.json()

print(data)
