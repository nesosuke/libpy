#｢Google BooksでAPIを叩く｣のモジュール化試行
import requests

if __name__ == "__main__":
    def info(Isbn):
        response = requests.get(
        'https://www.googleapis.com/books/v1/volumes',
        params={
            "q": "isbn=" + str(Isbn)
        }
        )
        BookInfo = dict(response.json()).get("items")[0]["volumeInfo"]

BookTitle = BookInfo["title"]
BookAuthors = BookInfo["authors"][0]

def info(Isbn):
    return BookInfo

def title(Isbn):
    return BookTitle

def authors(Isbn):
    return BookAuthors
