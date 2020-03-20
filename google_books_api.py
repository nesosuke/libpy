#Google BooksでAPIを叩く
import requests as req
 
ISBN = 9784873117386
response = req.get(
    'https://www.googleapis.com/books/v1/volumes',
    params={
        "q": "isbn=" + str(ISBN)
    })
BookInfo = dict(response.json()).get("items")[0]["volumeInfo"]
BookTitle = BookInfo["title"]
BookAuthor = BookInfo["authors"][0]
print("Title: " + BookTitle)
print("Author: " + BookAuthor)