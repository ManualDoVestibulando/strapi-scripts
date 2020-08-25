# Run script manually for each year's folder
# Filenames should follow the model:
#   comp1-comp2-comp3-comp4-comp5_id

import requests
import glob

ano = 2016

names = []
names.extend(glob.glob("*.png"))

RED_URL = "https://api.manualdovestibulando.digital/redacao-enems"
for name in names:
    notas = name.split("_")[0]
    geral =  int( notas.split("-")[0] )
    comp_1 = int( notas.split("-")[1] ) 
    comp_2 = int( notas.split("-")[2] ) 
    comp_3 = int( notas.split("-")[3] ) 
    comp_4 = int( notas.split("-")[4] ) 
    comp_5 = int( notas.split("-")[5] ) 
    data = {"competencia_1": comp_1, "competencia_2": comp_2, "competencia_3": comp_3, "competencia_4": comp_4, "competencia_5": comp_5, "ano": ano, "foto": name, "nota_total": geral}
    requests.post(url=RED_URL, data=data)
