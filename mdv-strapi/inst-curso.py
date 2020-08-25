
import requests
import pandas as pd

# Read CSV data
df = pd.read_csv("./Relacao_de_Cursos1.csv")

cursos = df["Curso"]

df = df.drop_duplicates(subset=["Unidade"], ignore_index=True)
unidades = df["Unidade"]
siglas = df["Sigla"]

# Send POST requests

CURSO_URL = "https://api.manualdovestibulando.com.br/cursos"
for i in range(cursos.shape[0]):
    c_data = {"nome": cursos[i]}
    requests.post(url=CURSO_URL, data=c_data)

INSTITUTO_URL = "https://api.manualdovestibulando.com.br/institutos"
for j in range(unidades.shape[0]):
    u_data = {"nome": unidades[j], "sigla": siglas[j]}
    requests.post(url=INSTITUTO_URL, data=u_data)