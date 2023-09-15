# # Faça requisições GET em todos os livros e veja se os cadastrados por você estão disponíveis. - Feito

# import requests
# import json

# # URL da API
# url = "http://apilivro.jogajuntoinstituto.org/"
# url1 = "http://apilivro.jogajuntoinstituto.org/authors/"
# url2 = "http://apilivro.jogajuntoinstituto.org/genders/"
# url3 = "http://apilivro.jogajuntoinstituto.org/books/"

# # Dados dos livros para cadastro
# livros = [
#     {
#         "title": "A Culpa é das Estrelas.",
#         "description": "Inspirador, corajoso, irreverente e brutal, A culpa é das estrelas é a obra mais ambiciosa e emocionante de John Green, sobre a alegria e a tragédia que é viver e amar.",
#         "author": 7,
#         "gender": 2,
#         "edition": "1ª Edição"
#     },

#     {
#         "title": "Indentação: A Saga do Espaço em Branco.",
#         "description": "Uma aventura épica no mundo da programação, onde o herói deve navegar pelos perigosos labirintos de código Python, armado apenas com sua confiável régua de indentação. Cada espaço em branco pode ser a diferença entre a vitória e um erro de sintaxe.",
#         "author": 7,
#         "gender": 2,
#         "edition": "1ª Edição"
#     },

#     {
#         "title": "Python: A Lenda da Serpente Encantada",
#         "description": "Este livro conta a história mítica da linguagem de programação Python, desde sua criação por Guido van Rossum até se tornar uma das linguagens mais populares do mundo. Acompanhe a jornada da Serpente Encantada enquanto ela encanta desenvolvedores com sua sintaxe clara e legibilidade.",
#         "author": 7,
#         "gender": 2,
#         "edition": "1ª Edição"
#     },

#     {
#         "title": "Django Desencadeado: A Revolução do Framework",
#         "description": "Uma análise profunda do framework Django, que revolucionou o desenvolvimento web em Python. Este livro explora como Django desencadeou uma nova era de aplicações web rápidas, seguras e escaláveis.",
#         "author": 7,
#         "gender": 2,
#         "edition": "1ª Edição"
#     },

#     {
#         "title": "Corram que o Python vem aí!",
#         "description": "Este livro é uma jornada emocionante através do mundo da programação Python. Ele captura a adrenalina de resolver problemas complexos e a satisfação de ver seu código ganhar vida. Desde os fundamentos da linguagem até os conceitos avançados, este livro é um guia indispensável para qualquer um que queira dominar Python. Prepare-se para mergulhar de cabeça no mundo do Python e descubra por que tantos desenvolvedores estão correndo para aprender esta linguagem poderosa e versátil.",
#         "author": 7,
#         "gender": 2,
#         "edition": "1ª Edição"
#     },
# ]

# # Cadastrando os livros
# for livro in livros:
#     response = requests.post(url3, data=json.dumps(livro), headers={
#                              'Content-Type': 'application/json'})
#     if response.status_code == 201:
#         print(f"Livro {livro['title']} cadastrado com sucesso!")
#     else:
#         print(
#             f"Erro ao cadastrar o livro {livro['title']}. Resposta: {response.text}")

# # Fazendo uma requisição GET para verificar os livros cadastrados
# response = requests.get(url3)
# if response.status_code == 200:
#     livros_cadastrados = response.text
#     print(f"Resposta: {livros_cadastrados}")
#     if isinstance(livros_cadastrados, str):
#         print("A resposta é uma string. Tentando converter para JSON.")
#         try:
#             livros_cadastrados = json.loads(livros_cadastrados)
#         except json.JSONDecodeError:
#             print("Erro ao decodificar a resposta em JSON.")
#     if isinstance(livros_cadastrados, list):
#         for livro in livros_cadastrados:
#             print(
#                 f"Título: {livro['title']}, Autor: {livro['author']}, Gênero: {livro['gender']}")
#             # print(f"Título: {livro['title']}, Autor: {livro['author']}, Gênero: {livro['gender']}, Edição: {livro['edition']}")
#     else:
#         print("A resposta não é uma lista.")
# else:
#     print(f"Erro ao buscar os livros cadastrados. Resposta: {response.text}")


import requests
import json

# URL da API
url1 = "http://apilivro.jogajuntoinstituto.org/authors/"
url2 = "http://apilivro.jogajuntoinstituto.org/genders/"
url3 = "http://apilivro.jogajuntoinstituto.org/books/"

# Dados dos autores para cadastro
autores = [
    {"name": "Renato Fabricio"},
    {"name": "Josie Fortuna"},
    {"name": "Kate Batista"},
    {"name": "Ester Carvalho"}
]

# Dados dos gêneros para cadastro
generos = [
    {"name": "Ficção"},
    {"name": "Aventura"},
    {"name": "Romance"},
    {"name": "Comédia"}
]

# Dados dos livros para cadastro
livros = [
    {"title": "QAme of Thrones"},
    {"title": "Indiana Python"},
    {"title": "O python é das estrelas"},
    {"title": "Corram que o Python vem aí"}
]


# Cadastrando os autores
for authors in autores:
    response = requests.post(f'{url1}', data=authors)
    if response.status_code == 201:
        print(f"Autor {authors} cadastrado com sucesso!")
    else:
        print(
            f"Erro ao cadastrar o autor {authors}. Resposta: {response.text}")

# Cadastrando os gêneros
for genders in generos:
    response = requests.post(f'{url2}', data=genders)
    if response.status_code == 201:
        print(f"Gênero {genders} cadastrado com sucesso!")
    else:
        print(
            f"Erro ao cadastrar o gênero {genders}. Resposta: {response.text}")


# Cadastrando os livros
for books in livros:
    response = requests.post(f'{url3}', data=books)
    if response.status_code == 201:
        print(f"Livro {books['title']} cadastrado com sucesso!")
    else:
        print(
            f"Erro ao cadastrar o livro {books['title']}. Resposta: {response.text}")

#

# Fazendo uma requisição GET para verificar os livros cadastrados
response = requests.get(f'{url3}')
if response.status_code == 200:
    livros_cadastrados = response.text
    print(f"Resposta: {livros_cadastrados}")
    if livros_cadastrados:
        try:
            livros_cadastrados = json.loads(livros_cadastrados)
            for livro in livros_cadastrados:
                response2 = requests.get(f'{url1}' + str(livro['author']))
                print(
                    f"Título: {livro['title']}, Autor: {response2.json()['name']}, Gênero: {livro['gender']}")
        except json.JSONDecodeError:
            print("Erro ao decodificar a resposta em JSON.")
    else:
        print("A resposta está vazia.")
else:
    print(f"Erro ao buscar os livros cadastrados. Resposta: {response.text}")
