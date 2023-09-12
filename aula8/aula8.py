# def ola_mundo():
#     print('Olá, mundo!')


# # Agora você chama a função uma vez para que ela seja executada.
# ola_mundo()


# Definindo funções fictícias
def misturar_ingredientes():
    print('Misturando os ingredientes...')


def assar_no_forno():
    print('Assando no forno...')


def decorar_bolo():
    print('Decorando o bolo...')

# Definindo a função fazer_bolo


def fazer_bolo():
    misturar_ingredientes()
    assar_no_forno()
    decorar_bolo()
    return "Bolo pronto!"


# Chamando a função fazer_bolo
resultado = fazer_bolo()

# Imprimindo o resultado
print(resultado)
