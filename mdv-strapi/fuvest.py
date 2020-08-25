import time

import pandas as pd

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

##
## Read CSV
##

df = pd.read_csv("./fuvs_forms_df4.csv")

fase1 = df["Fase1"]
fase2dia1 = df["Dia1"]
fase2dia2 = df["Dia2"]
redacao = df["Red_Fuvest"]
classificacao = df["Classificacao"]
cota = df["Modalidade"]
curso = df["Curso"]

entradas = fase1.shape[0]

##
## Access Strapi API
##

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://api.manualdovestibulando.digital/admin/")

# Log in
WebDriverWait(browser, 1000).until(EC.element_to_be_clickable((By.NAME , "email"))).send_keys("EMAIL")
browser.find_element(By.NAME , "password").send_keys("PASSWORD")
browser.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/section[2]/div/div/form/div[4]/button").click()
# Go to Nota-enems
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/a[6]"))).click()

for i in range(entradas) :
    # Add new Nota
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/button"))).click()
    # Fill fields
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "fase1"))).send_keys( str(fase1[i]) )
    browser.find_element_by_id("fase2dia1").send_keys( str(fase2dia1[i]) )
    browser.find_element_by_id("fase2dia2").send_keys( str(fase2dia2[i]) )
    browser.find_element_by_id("redacao").send_keys( str(redacao[i]) )
    browser.find_element_by_id("classificacao").send_keys( str(classificacao[i]) )
    # Select Cota in dropdown menu
    select = Select(browser.find_element_by_id("cota"))
    select.select_by_visible_text( str(cota[i]).strip() )
    # Select Curso
    for c in range( len(str(curso[i])) ):
        time.sleep(0.2)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "react-select-"+str(2+i)+"-input"))).send_keys( str(curso[i])[c] )
    time.sleep(3)
    browser.find_element_by_id("react-select-"+str(2+i)+"-input").send_keys(Keys.TAB)
    # Submit
    browser.find_element_by_id("react-select-"+str(2+i)+"-input").send_keys(Keys.ENTER)
    print(i)
