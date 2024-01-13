# TEST Method 1
import requests

res = requests.get("http://localhost:8000/")
result = res.json()
print(result)

# TEST Method 2

# http -b localhost:8000/