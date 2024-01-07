import requests
from requests.models import Response
from requests.structures import CaseInsensitiveDict

#getBooks: Response = requests.get('https://simple-books-api.glitch.me/books')
#getBooks: Response = requests.get('https://requests.readthedocs.io/en/latest/')

#status_code : int = getBooks.status_code

#json_data = getBooks.json()


#username: str = input("enter your username")
#email: str = input("enter your email address")

data = {
    "clientName":"mrk",
    "clientEmail":"ahsssan@gmail.com"
}
#headers={'Authorization':'Bearer 5aeec4dd14c403332a71bb30160f00fd78c7ec071b92b8103e3b504df7e1fb76'}
postData:Response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=data)

# status_code: int = postData.status_code
# print(status_code)
