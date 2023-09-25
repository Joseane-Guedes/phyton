# Anotações de como gerar e utilizar o token no postman de forma eficiente
# var jsonData = pm.response.json();
# pm.globals.set("currentToken", jsonData.access);

# Script de testes para fazer no postman em nosso projeto finally
# pm.test("Deverá retornar o nome do gênero ", function () {
#     var jsonData = pm.response.json();
#     pm.expect(jsonData.name).to.eql("Suzano");
# });

# pm.test("Código de status é 201 - created", function () {
#     pm.response.to.have.status(201);

# });

# pm.test("Deverá retornar erro se o nome já criado ", function () {
#     pm.response.to.have.status(201)
# });

# pm.test("Código de status é 201 - created", function () {
#     pm.response.to.have.status(201);

# });

#  Automaçoes - Fazer umas 10

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

"""
Tarefa: 
Entrar no site do IJJ, trocar idioma e verificar se o texto foi alterado
"""

navegador = Firefox()

navegador.get("https://jogajuntoinstituto.org")

change_lang = navegador.find_element(By.XPATH, "/html/body/div[1]/div[1]/button").click()

lang_options = navegador.find_elements(By.TAG_NAME, "li")

for lang_opt in lang_options:
    valor = lang_opt.get_attribute('data-value')
    if valor is not None:
        print(valor)
        if valor == "en":
            lang_opt.click()

banner_title = navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[1]/div/div/div[2]/h1")

print(banner_title.text)

assert "Step into the Field" in banner_title.text

