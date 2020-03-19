#Google BooksでAPIを叩く
import requests as req
import json 
ISBN = 9784873117386
response = req.get(
    'https://www.googleapis.com/books/v1/volumes',
    params={
        "q": "isbn=" + str(ISBN)
    })
response = dict(response.json()).get("items")
#response = json.loads(response)

print(response)