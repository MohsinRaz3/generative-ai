import requests

# post body
body = {"who" : "mohsin"}
res = requests.post("http://localhost:8000/hi", json=body)
result = res.json()
print(result)