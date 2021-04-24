from django.db import models
import pymongo

class mongoClass(models.Model):
    pass

# MongoDB client
client = pymongo.MongoClient("mongodb+srv://adminuser:adminuserpassword@cluster0.tilcf.mongodb.net/myDB2?retryWrites=true&w=majority")

# Database Name
db = client["myDB2"]

# Collection
col4 = db.collection4

def displaySearch(input_string):
    s = col4.find({"$text": {"$search": 'i want some help"'}},
              {'score': {'$meta': 'textScore'}})
    s.sort([('score', {'$meta': 'textScore'})])

    return list(s)