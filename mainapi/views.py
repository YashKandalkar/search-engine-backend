from django.shortcuts import render

from django.http import JsonResponse
from urllib.parse import unquote, urlparse, parse_qs
import pymongo

# MongoDB client
client = pymongo.MongoClient(
    "mongodb+srv://adminuser:adminuserpassword@cluster0.tilcf.mongodb.net/myDB2?retryWrites=true&w=majority")

# Database Name
db = client["myDB3"]

# Collection
col = db.collection5

# col.create_index([
#     ("url", "text"), ("text", "text")
# ])

count = 1

def displaySearch(input_string, page=1):
    s = col.aggregate([
        {
            '$search': {
                'index': 'default',
                'text': {
                    'query': input_string,
                    'path': 'url'
                }
            }
        },
        {'$sort': {'score': {'$meta': "textScore"}}},
        {'$project': {'_id': 0}}
    ])
    s = list(s)

    global count
    count = len(s)

    if 15*page > len(list(s)) :
        s = s[ 15*(page-1) : 15*page ]
    elif len(list(s)) > 16:
        s = s[ : 15]

    return s


def search(request):
    s = request.get_raw_uri()

    text = parse_qs(urlparse(s).query)["text"][0]
    text = unquote(text)

    page = 1
    if "page" in parse_qs(urlparse(s).query) :
        page = int( parse_qs(urlparse(s).query)["page"][0] )

    result = displaySearch(text, page)

    responseData = {
        'result': result,
        'count' : count
    }

    return JsonResponse(responseData)
