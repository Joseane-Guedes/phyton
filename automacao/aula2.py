from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

navegador = Firefox()

link = "https://page-test-selenium.s3.sa-east-1.amazonaws.com/index.html"
#navegador.get("https://google.com")
navegador.get(link)

adicionar = navegador.find_element(By.ID, "addElement")

contador = 0
while contador <= 10:

    adicionar.click()
    contador += 1

checkboxes = navegador.find_elements(By.TAG_NAME, "input")


for checkbox in checkboxes:
    
    checkbox.click()

sleep(5)
import ipdb;ipdb.sset_trace()
navegador.quit()