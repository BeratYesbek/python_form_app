import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Database import RunFirebase


cred = credentials.Certificate('python-djongo-firebase-adminsdk-qziyo-e6d292e1fc.json')
firebase_admin.initialize_app(cred)
