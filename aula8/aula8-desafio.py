# INDIVIDUAL

# Leiam o case abaixo e resolvam.

# Uma escola está organizando sua primeira olimpíada do conhecimento e deseja separar os 100 alunos em dois grupos de 50. Além de testar os conhecimentos dos alunos, querem estimular a formação de novos laços sociais e, por isso, a divisão dos grupos de alunos será feita seguindo um critério:

# Alunos com número de matrícula par, ficarão no grupo azul.
# Alunos com número de matrícula ímpar, ficarão no grupo amarelo.
# Os alunos ainda não sabem dessa regra de separação dos grupos e, no dia do evento, quando digitarem o número da matrícula na catraca, deve aparecer no painel a cor do grupo que ele deve integrar.

# DESAFIO: Desenvolvam uma função para retornar se o número passado pelo usuario no console é par ou ímpar.

# Caso o número de matrícula do(a) aluno(a) seja par imprima:
# VOCÊ ESTÁ NO TIME AZUL

# Caso o número de matrícula do(a) aluno(a) seja impar imprima:
# VOCÊ ESTÁ NO TIME AMARELO


# Primeiro, criar uma função que determine se um número é par ou ímpar.
def verificar_paridade(numero):
    if numero % 2 == 0:
        return "VOCÊ ESTÁ NO TIME AZUL"
    else:
        return "VOCÊ ESTÁ NO TIME AMARELO"


# Segundo, solicita que o usuário insira o número da matrícula
numero_matricula = int(input("Digite o número da matrícula: "))

# Terceiro, chama a função para verificar a paridade e imprime a mensagem
mensagem = verificar_paridade(numero_matricula)
print(mensagem)
