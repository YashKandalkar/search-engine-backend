from django.shortcuts import render
import pyrebase

'''  
config={
    "apiKey" : "AIzaSyCbGS8Hmq3u2xcxv0EwDjrepFJj1oAG0UA",
    "authDomain" : "devsearch-9ed5d.firebaseapp.com",
    "projectId" : "devsearch-9ed5d",
    "storageBucket" : "devsearch-9ed5d.appspot.com",
    "messagingSenderId" : "828300138401",
    "appId" : "1:828300138401:web:97873f521dfc31eddedde0",
    "databaseURL" : "https://devsearch-9ed5d-default-rtdb.firebaseio.com/",
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
  
def firebaseView(request):
    day = database.child('Data').child('Day').get().val()
    id = database.child('Data').child('Id').get().val()
    projectname = database.child('Data').child('Projectname').get().val()
    return render(request,"firebaseTemplate.html",{"day":day,"id":id,"projectname":projectname })

###############
#firestore part
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('path/to/serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
'''