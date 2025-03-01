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

    # Aguarda o botão de datas estar presente e clica nele para abrir o calendário
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='date-display-field-start']"))
    ).click()

    # Define a data desejada no formato YYYY-MM-DD
    data_checkin = "2025-03-15"
    data_checkout = "2025-03-20"

    # Aguarda e clica na data de check-in
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f"td[data-date='{data_checkin}']"))
    ).click()

    # Aguarda e clica na data de check-out
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f"td[data-date='{data_checkout}']"))
    ).click()

    time.sleep(3)


    '''

    # Aguarda o calendário aparecer e busca o mês correto
    while True:
        mes_atual = driver.find_element(By.CSS_SELECTOR, "div[data-testid='current-month']")
        
        if mes_ano_desejado in mes_atual.text:
            break  # Sai do loop se encontrar o mês certo
        else:
            # Avança para o próximo mês
            driver.find_element(By.CSS_SELECTOR, "button[aria-label='Next month']").click()

    # Aguarda e seleciona o dia desejado dentro do mês correto
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[@aria-label='{dia_desejado} {mes_ano_desejado}']"))
    ).click()

    # Fecha o navegador (caso necessário)
    # driver.quit()
    '''

    time.sleep(5)
    '''
    # Clicar no botão de pesquisa
    search_button = driver.find_element(By.CLASS_NAME, "e4adce92df")
    search_button.click()
    '''
    time.sleep(5)  # Espera os resultados carregarem

finally:
    driver.quit()  # Fecha o navegador