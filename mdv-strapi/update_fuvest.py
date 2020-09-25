
import requests
import pandas as pd

def to_str(entry):
    return [str(i) for i in entry]

df = pd.read_csv("/home/tomaz/Desktop/fuvs_forms_df6.csv")

BASE_URL = "https://api.manualdovestibulando.com.br/notas/"

cota = df["Modalidade"]
anos = df["Ano"]

f1 = to_str( df["Fase1"] )
f2d1 = to_str( df["Dia1"] )
f2d2 = to_str( df["Dia2"] )

for i in range(len(cota)):

    GET_URL = BASE_URL + "?fase1="+f1[i] + "&fase2dia1="+f2d1[i] + "&fase2dia2="+f2d2[i]
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