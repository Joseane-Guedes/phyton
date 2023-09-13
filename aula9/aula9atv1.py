# PARTE 1

# Crie um DataFrame com os seguintes dados:

# Nome, idade e cidade. Sendo 3 pessoas moradoras de Recife, 2 de Salvador, 1 de são paulo e 1 de Manaus

# Depois, filtre os dados para exibir na tela apenas os moradores do Recife.

# stock-image.jpg
# Tempo de Realização

# import pandas as pd

# data = {
#     'Nome': ['Marta', 'Marcela', 'Carlos', 'Patricia', 'Pedro', 'Julia', 'Lucas'],
#     'Idade': [20, 30, 40, 50, 25, 35, 45],
#     'Cidade': [ 'Recife', 'Recife', 'Recife', 'Salvador', 'Salvador', 'São Paulo'],
# }

# df = pd.DataFrame(data)

# # Filtrar apenas os moradores do Recife
# recife_residents = df.loc[df['Cidade'] == 'Recife']

# print(recife_residents)

import pandas as pd

data = {
    'Nome': ["João", "Marta", "Ary", "Ester", "Josie", "Renato", "Katie",],
    'Idade': [51, 37, 23, 24, 33, 15, 23],
    'Cidade': ["Recife", "Recife", "Recife", "Salvador", "Salvador", "São Paulo", "Manaus"]
}

df = pd.DataFrame(data)

# print(df)

recife_residents = df.loc[df['Cidade'] == 'Recife']

print(recife_residents)
