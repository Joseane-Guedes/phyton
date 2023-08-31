# Capturar informações do usuário

# Objetivo da atividade: Praticar os conceitos vistos até aqui.

# Como: Faça um programa que capture o nome do usuário, altura em metros, idade e imprima


# nome = input("Digite seu nome: ")
# sobrenome = input("Digite seu sobrenome: ")
# altura = float(input("Digite sua altura em metros: "))
# idade = int(input("Digite sua idade: "))
# nota1 = int(input("Digite sua nota1: "))
# nota2 = int(input("Digite sua nota2: "))
# Imprimir as informações capturadas
# print("Nome:", nome)
# print("Sobrenome:", sobrenome)
# print("Altura:", altura, "metros")
# print("Idade:", idade, "anos")


# print(
#     f" O nome é: {nome} {sobrenome} e a sua altura é {altura} metros e sua idade é {idade} sua altura é {altura} metros e sua nota1 é {nota1} e sua nota2 é {nota2}")

nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
mes = 'JANEIRO'
n1 = int(input('Digite o sua 1 nota: '))
n2 = int(input('Digite o sua 2 nota: '))
# desconto = int('10')
# cupom = nome + "É" + desconto
# tipo_nome = type(desconto)
# print(tipo_nome)
soma = n1 + n2

print(
    f" O nome é: {nome} {sobrenome} a primeira nota é {n1} e a segunda é {n2} a minha nota geral é {soma}")
