# Run script manually for each year's folder
# Filenames should follow the model:
#   grade_id

import requests
import glob

ano = 2020

names = []
names.extend(glob.glob("*.png"))

RED_URL = "https://api.manualdovestibulando.digital/redacaos"
for name in names:
    nota = float( name.split("-")[0].split("_")[0].replace(",", ".") )
    data = {"foto": name, "nota": nota, "ano": ano}
    requests.post(url=RED_URL, data=data)
