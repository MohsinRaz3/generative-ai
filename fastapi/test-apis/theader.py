import requests
header= {"who": "mohsin-Raz"}
res = requests.post("http://localhost:8000/headerr",headers=header)
result = res.json()
print(result)