# TODO Individualmente

# Crie uma persona com a biblioteca Faker com nome, idade e cidade. Criando o atributo random.int para gerar valores aleatórios para idade.

from faker import Faker
import pandas as pd

faker = Faker('pt_br')

data = {
    "Nome": [faker.name(), faker.name()],
    "Cidade": [faker.address(), faker.name()],
}

# print(data)

df = pd.DataFrame(data)
print(df)

df.to_csv("novaplaniha.csv")
