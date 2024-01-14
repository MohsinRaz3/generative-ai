# TEST Method 1
import requests

#URL Path
res = requests.get("http://localhost:8000/hi?who=mohsins")
PathUrl = res.json()
#print(PathUrl)

# TEST Method 2
# http -b localhost:8000/user/

