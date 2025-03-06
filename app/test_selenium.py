from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Caminho do ChromeDriver
chrome_driver_path = "E:\\Projetos\\chromedriver-win64\\chromedriver.exe"

# Configuração do WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Acessar o Booking.com
    driver.get("https://www.booking.com/")

    time.sleep(3)  # Espera a página carregar

    # Preencher o destino
    local_box = driver.find_element(By.ID, ":rh:")
    local_box.clear()
    local_box.send_keys("São Paulo")
    time.sleep(1)
    local_box.send_keys(Keys.ENTER)

    time.sleep(2)

    #######################################################

    # Esperar até que o botão do calendário esteja visível e clicar
    calendar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="date-display-field-start"]'))
    )
    calendar_button.click()

    time.sleep(2)  # Pequeno delay para garantir que o calendário carregou

    # Define a data desejada no formato YYYY-MM-DD
    data_checkin = "2025-03-15"
    data_checkout = "2025-03-20"

    # Localizar e clicar no botão de seleção de data
    date_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="date-display-field-start"]')
    date_button.click()

    # Aguardar um tempo para visualizar a ação (opcional)
    time.sleep(2)

    date_checkin = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, f'span[data-date="{data_checkin}"]')
        )
    )
    date_checkin.click()
    time.sleep(2)

    date_checkout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, f'span[data-date="{data_checkout}"]')
        )
    )
    date_checkout.click()
    time.sleep(2)
    

    time.sleep(5)
    
    # Clicar no botão de pesquisa
    search_button = driver.find_element(By.CLASS_NAME, "e4adce92df")
    search_button.click()
    
    time.sleep(5)  # Espera os resultados carregarem

finally:
    driver.quit()  # Fecha o navegador