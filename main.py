from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializa Chrome
driver = webdriver.Chrome()

# Pagina de prueba con formulario
driver.get("https://www.w3schools.com/html/html_forms.asp")

# Llenar campos de texto
driver.find_element(By.ID, "fname").clear()
driver.find_element(By.ID, "fname").send_keys("Juan")
driver.find_element(By.ID, "lname").clear()
driver.find_element(By.ID, "lname").send_keys("Franco")
time.sleep(3)
# Simular envio
driver.find_element(By.XPATH, "//input[@type='submit']").click()


time.sleep(3)

driver.quit()