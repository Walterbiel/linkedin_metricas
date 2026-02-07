from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pandas as pandas
import sqlalchemy
from dotenv import load_dotenv
import os
import shutil

# Configuração do Selenium
options = Options()
options.add_argument("--headless")  # Executa em segundo plano
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
print("Ambiente pronto")

#------------------------------------------------------------------------

load_dotenv()

email = os.getenv("LINKEDIN_EMAIL")
senha = os.getenv("LINKEDIN_PASSWORD")

#------------------------------------------------------------------------

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/in/walter-gonzaga/')

#------------------------------------------------------------------------

time.sleep(5)
driver.find_element(By.CSS_SELECTOR,'#main-content > div > form > p > button').click()

input_email = driver.find_element(By.ID,'session_key')
input_email.click()
input_email.send_keys(email)

input_senha = driver.find_element(By.ID,'session_password')
input_senha.click()
input_senha.send_keys(senha)

driver.find_element(By.CSS_SELECTOR,'#main-content > div > div.authwall-sign-in-form > form > div.flex.justify-between.sign-in-form__footer--full-width > button').click()

time.sleep(5)
driver.get('https://www.linkedin.com/analytics/creator/content/?timeRange=past_365_days')

#------------------------------------------------------------------------

time.sleep(5)
lista_links = []
links = driver.find_elements(By.CSS_SELECTOR, "a.member-analytics-addon__cta-item-with-secondary-anchor")

for a in links:
    if "impressões" in a.get_attribute("aria-label").lower():
        link = a.get_attribute("href")
        print(link)
        lista_links.append(link)
        
#------------------------------------------------------------------------

time.sleep(2)

for link in lista_links:
    driver.get(link)
    time.sleep(3)
    wait = WebDriverWait(driver, 5)

    botao_exportar = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[.//span[text()='Exportar']]")
        )
    )

    botao_exportar.click()
    time.sleep(3)

#------------------------------------------------------------------------

# PREFIXO dos arquivos
prefixo = "PostAnalytics_WalterGonzaga"

# Pasta Downloads (Windows padrão)
downloads = os.path.join(os.environ["USERPROFILE"], "Downloads")

# Pasta destino
destino = r"C:\Users\Walter\Documents\Comunidados\scraper_linkedin_base_metricas_p_analytics_e_ML\arquivos"

# Garante que a pasta existe
os.makedirs(destino, exist_ok=True)

movidos = 0

for arquivo in os.listdir(downloads):
    if arquivo.startswith(prefixo):
        origem_arquivo = os.path.join(downloads, arquivo)
        destino_arquivo = os.path.join(destino, arquivo)

        shutil.move(origem_arquivo, destino_arquivo)
        print(f"Movido: {arquivo}")
        movidos += 1

print(f"\nTotal movidos: {movidos}")
