# TODO
# INDIVIDUAL

# PARTE 1

# USANDO IF: Construa um script para verificar se o usuário tem uma idade maior que 18 anos, se tiver, imprima na tela "Indivíduo possui idade mínima para dirigir"

# Solicite a idade do usuário

# USANDO ELIF: Complemente o script feito, imprimindo na tela "Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir"

idade = int(input("Digite sua idade: "))

# Verifique a idade
if idade >= 18:
    print("Indivíduo possui idade mínima para dirigir")
# elif 17 <= idade <= 18:
elif 17 <= idade and idade <= 18:
    print("Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir")
else:
    print("Indivíduo não possui idade mínima para dirigir")
