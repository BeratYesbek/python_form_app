import json

import firebase
import firebase_admin
import requests
from firebase_admin import firestore, credentials
from firebase_admin import auth
from firebase_admin import storage

from djangoProject2.Constants import FirebaseCollection, Constants
from djangoProject2.Database import RunFirebase
from djangoProject2.Entity.User import User


class UserDal:
    # firebase code

    def __init__(self):
        RunFirebase
        RunFirebase.runStorage()

    def add(self, user):
        db = firestore.client()
        doc_ref = db.collection(FirebaseCollection.FirebaseCollection.USER_COLLECTION).document(user.Id)
        doc_ref.set({
            u'FirstName': user.firstName,
            u'LastName': user.lastName,
            u'Email': user.email,
            u'Id': user.Id,
            u'UserType':user.userType
        })

    def createUser(self, user):
        createdUser = auth.create_user(
            email=user.email,
            email_verified=False,
            password=user.password,
            disabled=False)
        if (createdUser.uid != ""):
            Constants.Constants.user_uuid = createdUser.uid
            return createdUser.uid

        return False

    def signOut(self):
        Constants.Constants.user_uuid = ""

    def update(self, user):
        db = firestore.client()
        db.collection(FirebaseCollection.FirebaseCollection.USER_COLLECTION) \
            .document(user.Id).update({
            u'FirstName': user.firstName,
            u'LastName': user.lastName,
        })

    def login(self, email, password):
        request_ref = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={}".format(
            "AIzaSyC1ck_necHihU4E79W6UYucFhw27kSuH-s"
        )
        headers = {"content-type": "application/json; charset=UTF-8"}
        data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
        request_object = requests.post(request_ref, headers=headers, data=data)
        firebase.raise_detailed_error(request_object)
        current_user = request_object.json()
        Constants.Constants.user_uuid = current_user["localId"]
        return current_user

    # def delete(self, user):

    def getById(self, id):
        user = User
        db = firestore.client()
        docs = db.collection(FirebaseCollection.FirebaseCollection.USER_COLLECTION).where(u'Id', u'==', id).stream()
        for doc in docs:
            dict = doc.to_dict()
            id = dict["Id"]
            firstName = dict["FirstName"]
            lastName = dict["LastName"]
            email = dict["Email"]
            userImage = dict["UserImage"]
            userType = dict["UserType"]
            user = User(id, firstName, lastName, email, userImage, userType,"")

        return user

    def getAll(self):
        db = firestore.client()
        collection = FirebaseCollection.FirebaseCollection.USER_COLLECTION
        docs = db.collection(collection).stream()

        for doc in docs:
            dictionary = doc.to_dict()

    def uploadImage(self, userId, file):
        firebaseStorage = RunFirebase.runStorage().storage()
        path = "UserImages/" + str(userId) + "/userImage"
        firebaseStorage.child(path).put(file)
        self.downloadFile(path, userId)

    def downloadFile(self, path, userId):
        firebaseStorage = RunFirebase.runStorage().storage()
        uri = firebaseStorage.child(path).get_url(FirebaseCollection.FirebaseCollection.FIREBASE_TOKEN)
        self.setImageToFirestore(uri, userId)

    def setImageToFirestore(self, uri, userId):
        db = firestore.client()
        doc_ref = db.collection(FirebaseCollection.FirebaseCollection.USER_COLLECTION).document(userId)
        doc_ref.update({
            u'UserImage': str(uri),
        })
