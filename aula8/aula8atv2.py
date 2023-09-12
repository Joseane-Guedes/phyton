import aula8atv1

from aula8atv1 import verificar_paridade


def verificar_paridade(matricula):
    for numero in matricula:
        if numero % 2 == 0:
            print(f'O número {numero} é par.')
        else:
            print(f'O número {numero} é ímpar.')


matricula = []
while len(matricula) < 5:
    numero = int(input('Insira um número de matrícula: '))
    matricula.append(numero)

verificar_paridade(matricula)
