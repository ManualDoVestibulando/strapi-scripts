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

df = pd.read_csv("./enem_forms_df3.csv")

ling = df["LC"]
mat = df["MAT"]
nat = df["CN"]
hum = df["CH"]
red = df["Redacao"]
cota = df["Modalidade"]
medias = df["Media"]
curso = df["Curso"]

entradas = curso.shape[0]

##
## Access Strapi API
##

URL = "https://api.manualdovestibulando.com.br/admin/"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(URL)

# Log in
WebDriverWait(browser, 1000).until(EC.element_to_be_clickable((By.NAME , "email"))).send_keys("EMAIL") 
browser.find_element(By.NAME , "password").send_keys("PASSWORD")
browser.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/section[2]/div/div/form/div[4]/button").click()
# Go to Notas-enems
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/a[6]"))).click()

for i in range(entradas) :
    # Add new Nota
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/button"))).click()
    # Fill fields
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "linguagens"))).send_keys( str(ling[i]) )
    browser.find_element_by_id("matematica").send_keys( str(mat[i]) )
    browser.find_element_by_id("ciencias_natureza").send_keys( str(nat[i]) )
    browser.find_element_by_id("ciencias_humanas").send_keys( str(hum[i]) )
    browser.find_element_by_id("redacao").send_keys( str(red[i]) )
    browser.find_element_by_id("Media").send_keys( str(medias[i]) )
    # Select Cota in dropdown menu
    select = Select(browser.find_element_by_id("cota"))
    select.select_by_visible_text( str(cota[i]).strip() )
    # Select Curso
    for c in range( len(str(curso[i])) ):
        if c < 5:
            time.sleep(0.2)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "react-select-"+str(2+i)+"-input"))).send_keys( str(curso[i])[c] )
    time.sleep(4)
    browser.find_element_by_id("react-select-"+str(2+i)+"-input").send_keys(Keys.TAB)
    # Submit
    browser.find_element_by_id("react-select-"+str(2+i)+"-input").send_keys(Keys.ENTER)
    print(i)
