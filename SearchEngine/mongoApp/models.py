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

def displayData():
    client = pymongo.MongoClient("mongodb+srv://adminuser:<password>@cluster0.tilcf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    # Database Name
    db = client["myDB2"]

    # Collection Name
    col = db["collection3"]

    x = col.find_one()

    return x