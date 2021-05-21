from firebase_admin import firestore

from Constants import FirebaseCollection
from Database import RunFirebase
from firebase_admin import auth
from Constants.FirebaseCollection import FirebaseCollection


class UserDal:

    def __init__(self):
        RunFirebase

    def add(self, user):
        db = firestore.client()
        doc_ref = db.collection(FirebaseCollection.USER_COLLECTION).document(user.Id)
        doc_ref.set({
            u'FirstName': user.firstName,
            u'LastName': user.lastName,
            u'Email': user.email,
            u'Id': user.Id
        })

    def createUser(self, user):
        createdUser = auth.create_user(
            email=user.email,
            email_verified=False,
            password=user.password,
            disabled=False)
        if (createdUser.uid != ""):
            return createdUser.uid

        return False

    def update(self, user):
        db = firestore.client()
        db.collection(FirebaseCollection.USER_COLLECTION) \
            .document(user.Id).update({
            u'FirstName': user.firstName,
            u'LastName': user.lastName,
        })

    def delete(self, user):
        db = firestore.client()
        db.collection(FirebaseCollection.USER_COLLECTION) \
            .document(user.Id).delete()
        auth.delete_user(user.Id)

    def getById(self, id):
        db = firestore.client()
        docs = db.collection(FirebaseCollection.USER_COLLECTION).where(u'Id', u'==', id).stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')

    def getAll(self):
        db = firestore.client()
        docs = db.collection(FirebaseCollection.USER_COLLECTION).stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')