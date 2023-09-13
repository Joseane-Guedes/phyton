# # Para desenvolver um programa que analisa o CEP inserido pelo usuário e determina se ele é elegível para frete grátis, precisamos considerar os seguintes pontos:

# *Fluxo e requisitos necessários:*
# 1. *Entrada do usuário:* O programa deve solicitar ao usuário que insira o CEP.
# 2. *Validação do CEP:* O programa deve validar se o CEP inserido pelo usuário é válido. Isso pode ser feito verificando se o CEP tem o número correto de dígitos e se contém apenas números.
# 3. *Determinação da região:* O programa deve determinar a região do CEP inserido. Isso pode ser feito usando uma API de CEP, que retorna a cidade e o estado do CEP.
# 4. *Verificação da elegibilidade para frete grátis:* Se o estado estiver nas regiões Norte ou Nordeste, o programa deve informar ao usuário que ele é elegível para frete grátis.

# *Desenvolvimento do programa:*
# Aqui está um exemplo de como o código poderia ser escrito em Python:

import requests


def verifica_frete_gratis(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    data = response.json()
    if 'erro' in data:
        return "CEP inválido"
    else:
        estado = data['uf']
        if estado in ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO', 'AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']:
            return "Frete grátis disponível para seu estado!"
        else:
            return "Frete grátis não disponível para seu estado."


cep = input("Insira seu CEP: ")
print(verifica_frete_gratis(cep))


# *Casos de teste:*
# 1. Teste com um CEP válido da região Norte ou Nordeste. O programa deve retornar que o frete grátis está disponível.
# 2. Teste com um CEP válido de outra região. O programa deve retornar que o frete grátis não está disponível.
# 3. Teste com um CEP inválido. O programa deve retornar que o CEP é inválido.

# *Documentação de bugs:*
# Se você encontrar algum bug no código, documente-o detalhadamente, incluindo a descrição do bug, os passos para reproduzi-lo, a entrada que causou o bug e a saída esperada versus a saída real.

# Por fim, insira todas as informações no Bitrix para documentação e rastreamento adequados.
