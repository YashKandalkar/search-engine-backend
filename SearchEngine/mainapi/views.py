from django.shortcuts import render

from django.http import JsonResponse
from urllib.parse import unquote, urlparse, parse_qs
import pymongo

# MongoDB client
client = pymongo.MongoClient("mongodb+srv://adminuser:adminuserpassword@cluster0.tilcf.mongodb.net/myDB2?retryWrites=true&w=majority")

# Database Name
db = client["myDB"]

# Collection
col = db.myCollection

col.create_index([
    ("url", "text"), ("text", "text")
])

def displaySearch(input_string):

    s = col.find(
        {"$text": {"$search": 'i want some help"'}},
        {'score': {'$meta': 'textScore'}, '_id' : 0 }
    )
    s.sort([('score', {'$meta': 'textScore'})])
    s = list(s)
    s = s[:15]
    return s

def search(request):
    s = request.get_raw_uri()
    text = parse_qs(urlparse(s).query)["text"][0]
    text = unquote(text)

    responseData = {
        'result' : displaySearch(text)
    }

    return JsonResponse(responseData)