from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializa Chrome
driver = webdriver.Chrome()

# Abre una página de prueba con formulario
driver.get("https://www.w3schools.com/html/html_forms.asp")

# Llenar campos de texto
driver.find_element(By.ID, "fname").send_keys("Juan")
driver.find_element(By.ID, "lname").send_keys("Franco")

# Simular envío (el botón no envía nada real, pero sirve de ejemplo)
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Espera unos segundos para ver el resultado
time.sleep(3)

driver.quit()