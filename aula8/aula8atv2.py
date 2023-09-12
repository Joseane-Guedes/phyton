from aula8atv1 import verificar_paridade


def verificar_paridade(matricula):
    if matricula % 2 == 0:
        print(f'O número {matricula} é par.')
    else:
        print(f'O número {matricula} é ímpar.')


matriculas = []

while len(matriculas) < 5:
    matricula = int(input('Insira um número de matrícula: '))
    matriculas.append(matricula)

# Laço de repetição para verificar a paridade de cada número na lista
for matricula in matriculas:
    verificar_paridade(matricula)

print(matriculas)
