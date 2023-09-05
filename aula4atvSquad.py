# Atividade em Squad
# Crie uma tupla com 5 dados
# São valores ordenados e imutáveis,  podem ser repetidos e estão contidos em dentro de um par de ():
minha_tupla = (1, 2, 3, 4, 5)
print(minha_tupla)

# Altere a tupla para uma lista
# São valores ordenados e mutáveis, que podem ser repetidos e estão contidos em dentro de um par de []
# A função list() em Python é usado para converter outro tipo de sequência ou coleção em uma lista.
minha_lista = list(minha_tupla)
print(minha_lista)

# Insira 2 dados extras a essa lista
# O método extend em Python é usado para estender uma lista existente adicionando elementos de outra sequência (geralmente outra lista) ao final da lista original. Isso permite combinar duas listas em uma única lista, mantendo a ordem dos elementos.
minha_lista.extend([6, 7])
print(minha_lista)

# Remova o primeiro dado da lista
# O del é uma instrução em Python usada para remover elementos ou objetos de uma lista, dicionário ou qualquer outra estrutura de dados mutável.
del minha_lista[0]

# Remova o último dado da lista
# O método pop() em Python é usado para remover e retornar o elemento de uma lista com base no índice fornecido como argumento.
minha_lista.pop()

# Faça um print com o primeiro dado da lista
print("Primeiro dado da lista:", minha_lista[0])

# Faça um print com a quantidade de dados da lista
# A função len() é comumente usada para determinar o número de elementos em uma lista ou a quantidade de caracteres em uma string, mas ela é aplicável a qualquer tipo de objeto iterável
print("Quantidade de dados na lista:", len(minha_lista))

# Crie um dicionário com os seguintes dados: Nome, Idade, Profissão
meu_dicionario = {"Nome": "Ana", "Idade": 30, "Profissão": "Engenheiro"}

# Imprima somente o valor contido na chave Nome do dicionário
print("Nome:", meu_dicionario["Nome"])
