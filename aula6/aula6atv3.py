# # Crie uma lista de frutas
# frutas = ["maçã", "banana", "laranja", "uva", "pera"]

# # Crie uma lista de alergias
# alergias = []

# # Insira uma fruta da lista de frutas na lista de alergias
# alergias.append("uva")

# # Use um loop for para verificar cada fruta na lista de frutas
# for fruta in frutas:
#     # Verifique se a fruta está na lista de alergias
#     if fruta in alergias:
#         # Se a fruta estiver na lista de alergias, imprima o nome dela
#         print(f"Você é alérgico(a) a {fruta}!")

# Agora crie um script para com uma lista de frutas,
# Outra lista com o nome alergias.

# Insira uma fruta da lista de frutas na lista de alergias.
# Depois crie um for para cada item da lista passar por uma
# verificação em uma estrutura condicional para verificar se está essa fruta está contida na lista de alergias.
# Caso a fruta esteja na lista, imprima na tela o nome dela.

frutas = ["maçã", "uva", "tangerina", "laranja", "morango"]
alergias = []

# #Insersão da fruta na lista de alergias
alergias.append(frutas[1])

for frutas in frutas:
    if frutas in alergias:
        print(frutas)
