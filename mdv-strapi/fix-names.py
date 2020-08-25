import requests

allowed_parenthesis = ["bach", "lic", "basico", "bach e lic", "energia e automacao"]

URL = "https://api.manualdovestibulando.com.br/cursos/"
info = list( requests.get(URL).json() )

# Loop through Cursos
for i in range(len(info)):
    identity = info[i]["_id"]
    name = info[i]["nome"]
    if "(" in name:
        name = name.split(" (")
        base = name[0]
        parenthesis = name[1].split(")")[0]

        if not parenthesis.lower() in allowed_parenthesis:
            data = {"nome": base}
            print(requests.put( url=URL+identity, data=data ))