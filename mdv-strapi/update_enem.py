
import requests
import pandas as pd

def to_str(entry):
    return [str(i) for i in entry]

df = pd.read_csv("/home/tomaz/Desktop/enem_forms_df3.csv")

BASE_URL = "https://api.manualdovestibulando.com.br/notas-enems/"

cota = df["Modalidade"]
anos = df["Ano"]

cn = to_str( df["CN"] )
mat = to_str( df["MAT"] )
lc = to_str( df["LC"] )
ch = to_str( df["CH"] )

for i in range(len(cota)):

    GET_URL = BASE_URL + "?cota="+cota[i] + "&linguagens="+lc[i] + "&matematica="+mat[i] + "&ciencias_natureza="+cn[i] + "&ciencias_humanas="+ch[i]
    try:
        data = dict( list( requests.get(GET_URL).json() )[0] )
        ano = int( anos[i] )
        if 2000 < ano < 2020:
            print(ano)
            PUT_URL = BASE_URL + data["_id"]
            data = {"ano": ano}
            print( requests.put(url=PUT_URL, data=data) )
    except:
        continue