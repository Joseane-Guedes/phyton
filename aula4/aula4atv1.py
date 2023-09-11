# Mini Case 1: Idade do Pet e Lucro do PETSHOP

# A dona de um PETSHOP quer criar um programa para calcular a idade dos cachorros de seus clientes em "anos de cachorro". Como os pets envelhecem de maneira diferente dos humanos - cada ano humano corresponde a 7 do Cachorro.

# Desafio: Crie um programa Python que calcule a idade de cachorro com base na idade humana.

# O que seu programa deve conter:

# Solicitar ao usuário a idade humana do pet (um número inteiro).
# Calcular a idade do pet, levando em consideração que cada ano da idade humana corresponde a 7.
# Exibir a idade do pet ao usuário.
# Além disso, ela deseja calcular, a cada 12 meses, o lucro obtido por banho e por cachorro.

# VALORES POR BANHO X CUSTO POR BANHO

# Cachorro de grande porte: BANHO: R$75,00 | CUSTO: R$20,00
# Cachorro de médio porte: BANHO: R$60,00 | CUSTO: 15,00
# Cachorro de médio porte: BANHO: R$50,00 | CUSTO: R$5,00
# Exemplo: Se um animal de grande porte tomar 10 banhos em 12 meses, no final, o programa deve imprimir a seguinte informação:

# Olá, Tuco tem 35 anos e nos últimos 12 meses o lucro com este animal foi de R$550,00


# Solicitar a idade humana do pet
idade_humana = int(input("Digite a idade humana do pet: "))

# Calcular a idade do pet em anos de cachorro
idade_pet = idade_humana * 7

# Imprimir a idade do pet
print(f"O pet tem {idade_pet} anos de cachorro.")

# Calcular o lucro por banho com base no porte do cachorro
porte = input("Digite o porte do cachorro (grande, médio ou pequeno): ")
quantidade_banhos = int(input("Digite a quantidade de banhos em 12 meses: "))

if porte == "grande":
    valor_banho = 75
    custo_banho = 20
elif porte == "médio":
    valor_banho = 60
    custo_banho = 15
elif porte == "pequeno":
    valor_banho = 50
    custo_banho = 5
else:
    print("Porte inválido, não é possível calcular o lucro.")
    exit()

lucro_total = valor_banho * quantidade_banhos - custo_banho * quantidade_banhos

# Imprimir o lucro obtido
print(
    f"Nos últimos 12 meses, o lucro com este animal foi de R${lucro_total:.2f}.")
