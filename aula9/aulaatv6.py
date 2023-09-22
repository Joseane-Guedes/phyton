# from faker import Faker
# import pandas as pd

# faker = Faker('pt_br')


# def gerar_massa(quantidade):
#     personas = []

#     for i in range(quantidade):
#         data = {
#             "Nome": faker.name(),
#             "Cidade": faker.city()
#         }
#         personas.append(data)

#     df = pd.DataFrame(personas)
#     return df


# resultado = gerar_massa(120)
# print(resultado)

# resultado.to_csv("segundo_personas.csv")

# from faker import Faker
# import csv

# def create_and_save_personas(filename, num_personas=100):
#     fake = Faker("pt_br")
#     fieldnames = ['Nome', 'Idade', 'Cidade']

#     with open(filename, 'w', newline='') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()

#         for _ in range(num_personas):
#             persona = {
#                 'Nome': fake.name(),
#                 'Idade': fake.random_int(min=18, max=90, step=1),
#                 'Cidade': fake.city()
#             }
#             writer.writerow(persona)

# # Criação e salvamento de personas em um arquivo CSV
# create_and_save_personas('personas.csv')


while True:
    resposta = input("Pediu desculpas pela merda que fez? (S/N): ")
    mensagem = "Teve humildade de assumir o erro, siga em frente!" if resposta.lower() == "s" else ("Não se arrependeu, volte para o início e tente novamente!" if resposta.lower()
                                                                                                    == "n" else "Resposta inválida. Por favor, responda com 's' para 'sim' ou 'n' para 'não'.")
    print(mensagem)
    if resposta.lower() in ["s", "n"]:
        break
