import requests

squad = {
    "Ester": "03881170",
    "Renato": "40325390",
    "Katie": "54310250",
    "Josie": "58078375"
}

for nome, cidade in squad.items():
    print(f'{nome} e {cidade}')

    # Make an API request for each city's postal code
    response = requests.get(f'https://viacep.com.br/ws/{cidade}/json/')
    data = response.json()

    # Print the data for the current city
    print(data)
