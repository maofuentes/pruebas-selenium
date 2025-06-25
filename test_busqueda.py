from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar el navegador
driver = webdriver.Firefox()
driver.get("https://www.mercadolibre.cl/")

# Esperar y cerrar el pop-up de ubicación o cookies si aparece
try:
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "onboarding-cp-button"))
    ).click()
except:
    pass  # Si no aparece, seguimos

# Esperar el campo de búsqueda
buscador = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "as_word"))
)
buscador.send_keys("nintendo")
buscador.send_keys(Keys.RETURN)

# Esperar que se carguen los resultados
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "li.ui-search-layout__item"))
)

# Extraer los títulos con un selector más robusto
resultados = driver.find_elements(By.XPATH, "//li[contains(@class,'ui-search-layout__item')]//h2")

# Validar y mostrar
if resultados:
    print("✅ Resultados encontrados:")
    for i, resultado in enumerate(resultados[:5], start=1):
        print(f"{i}. {resultado.text}")
else:
    print("❌ No se encontraron resultados en MercadoLibre.")

# Cerrar navegador
driver.quit()
