from django.db import models
import pymongo

# Create your models here.
class mongoClass(models.Model):
    pass

z=0
def counter():
    global z
    z+=1
    return z

client = pymongo.MongoClient("mongodb+srv://adminuser:adminuserpassword@cluster0.tilcf.mongodb.net/myDB2?retryWrites=true&w=majority")

# Database Name
db = client["myDB2"]

# Collection Name
# col = db["collection3"]
col = db.collection3
col4 = db.collection4

#creating index
# col4.create_index([
#   {
#     "mappings": {
#       "dynamic": true
#     }
#   }
# ])

def displaySearch():
    s = col4.find({"$text": {"$search": 'malloc'}})
    s3 = col.aggregate(
      [
          {
              '$search': {
                  'index': 'index1', 
                  'text': {
                      'query': 'integer', 
                      'path': 'URLS'
                  }
              }
          }
      ]
    )
    # s4 = col.aggregate(
    #   [
    #       {
    #           '$search': {
    #               'text': {
    #                   'query': 'operator', 
    #                   'path': 'text'
    #               }
    #           }
    #       }
    #   ]
    # )
    return list(s3)