
import pandas as pd
import requests

URL = "https://api.manualdovestibulando.com.br/depoimentos"

df = pd.read_csv("./deopimentos.csv")

link = df["link"]
titulo = df["titulo"]

for i in range(1, len(link)):
    data = {"link": link[i], "titulo": titulo[i]}
    print(requests.post(url=URL, data=data))