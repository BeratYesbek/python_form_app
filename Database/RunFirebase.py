import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#this py file is running firebase database
#firebase code


cred = credentials.Certificate('python-djongo-firebase-adminsdk-qziyo-e6d292e1fc.json')
firebase_admin.initialize_app(cred)

def runStorage():
    import pyrebase

    config = {
        "apiKey": "AIzaSyC1ck_necHihU4E79W6UYucFhw27kSuH",
        "authDomain": "python-djongo.firebaseapp.com",
        "databaseURL": "https://python-djongo.firebaseio.com",
        "storageBucket": "python-djongo.appspot.com",
        "serviceAccount": "python-djongo-firebase-adminsdk-qziyo-e6d292e1fc.json"
    }

    return pyrebase.initialize_app(config)
