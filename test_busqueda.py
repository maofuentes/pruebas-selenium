from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador
driver = webdriver.Firefox()
driver.get("https://duckduckgo.com/")

# Buscar el campo de texto y enviar consulta
buscador = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
buscador.send_keys("inmuebles en Bogotá")
buscador.send_keys(Keys.RETURN)

# Esperar que aparezcan los resultados
resultados = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-testid='result-title-a']"))
)

assert len(resultados) > 0, "No se encontraron resultados."
print("✅ Prueba funcional completada con éxito")

# Cerrar el navegador
driver.quit()
