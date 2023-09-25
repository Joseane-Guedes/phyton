from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep


def abrir_navegador(url):
    navegador = Firefox()
    navegador.get(url)
    return navegador


def encontrar_elemento(navegador, by, value):
    return navegador.find_element(by, value)


def preencher_campo(elemento, texto):
    elemento.clear()
    elemento.send_keys(texto)


def clicar_elemento(elemento):
    elemento.click()


def selecionar_opcao_por_valor(elemento, valor):
    select = Select(elemento)
    select.select_by_value(valor)


def main():
    url = "https://www.google.com/"
    navegador = abrir_navegador(url)

    barra_de_pesquisa = encontrar_elemento(navegador, By.NAME, "q")
    preencher_campo(barra_de_pesquisa, "Instituto Joga Junto")
    barra_de_pesquisa.send_keys(Keys.RETURN)

    sleep(5)

    elemento = encontrar_elemento(
        navegador, By.XPATH, "//h3[text()='Instituto Joga Junto']")
    clicar_elemento(elemento)

    sleep(5)

    elemento_contato = encontrar_elemento(
        navegador, By.XPATH, "//a[@href='/#Contato']")
    clicar_elemento(elemento_contato)

    sleep(5)

    elemento_nome = encontrar_elemento(navegador, By.ID, "nome")
    preencher_campo(elemento_nome, "Josie")

    elemento_email = encontrar_elemento(navegador, By.ID, "email")
    preencher_campo(elemento_email, "joseaneguedes34@gmail.com")

    elemento_assunto = navegador.find_element(By.ID, "assunto")
    selecionar = Select(elemento_assunto)
    selecionar.select_by_value("Ser mentora")

    elemento_nome = navegador.find_element(By.ID, "mensagem")
    elemento_nome.send_keys(
        "Squad Orion - Teste de automação com phyton e selenium sendo testado mais uma vez!")

    sleep(5)

    botao_enviar = encontrar_elemento(
        navegador, By.XPATH, "//button[@type='submit']/p[text()='Enviar']")
    clicar_elemento(botao_enviar)

    sleep(5)

    navegador.quit()


if __name__ == "__main__":
    main()
