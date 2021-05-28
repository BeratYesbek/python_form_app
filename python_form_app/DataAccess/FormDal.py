import io
from os.path import join

from firebase_admin import firestore
from firebase_admin import auth

from djangoProject2.Business.UserManager import UserManager
from djangoProject2.Constants import FirebaseCollection
from djangoProject2.Database import RunFirebase
from djangoProject2.Entity.Dto.FormDto import FormDto


class FormDal:
    # firebase code

    def __init__(self):
        RunFirebase

    def add(self, form):
        db = firestore.client()
        doc_ref = db.collection(FirebaseCollection.FirebaseCollection.FORM_COLLECTION).document(form.FormId)
        doc_ref.set({
            u'FormId': form.FormId,
            u'SenderId': form.SenderId,
            u'FormTitle': form.FormTitle,
            u'FormDescription': form.FormDescription,
            u'Date': form.Date
        })

    def update(self, form):
        db = firestore.client()
        db.collection(FirebaseCollection.FORM_COLLECTION) \
            .document(form.FormId).update({
            u'FormShare': form.FormShare,
            u'Date': form.Date,
        })

    def delete(self, formId):
        db = firestore.client()
        db.collection(FirebaseCollection.FirebaseCollection.FORM_COLLECTION).document(formId).delete()

    def getById(self, id):
        formDto = FormDto
        db = firestore.client()
        docs = db.collection(FirebaseCollection.FirebaseCollection.FORM_COLLECTION).where(u'FormId', u'==', id).stream()
        for doc in docs:
            dictionary = doc.to_dict()
            documentId = doc.id
            formId = dictionary["FormId"]
            senderId = dictionary["SenderId"]
            formTitle = dictionary["FormTitle"]
            formDescription = dictionary["FormDescription"]
            date = dictionary["Date"]
            userData = self.getUserData(senderId)
            userImage = userData.userImage
            userName = userData.firstName + " " + userData.lastName
            userType = userData.userType

            formDto = FormDto(formId, documentId, str(senderId), formTitle, formDescription, date, userImage, userName,
                              userType)
        return formDto

    def getByUserId(self, id):
        formList = []
        db = firestore.client()
        docs = db.collection(FirebaseCollection.FirebaseCollection.FORM_COLLECTION).where(u'SenderId', u'==',
                                                                                          id).stream()
        for doc in docs:
            dictionary = doc.to_dict()
            documentId = doc.id
            formId = dictionary["FormId"]
            senderId = dictionary["SenderId"]
            formTitle = dictionary["FormTitle"]
            formDescription = dictionary["FormDescription"]
            date = dictionary["Date"]
            userData = self.getUserData(senderId)
            userImage = userData.userImage
            userName = userData.firstName + " " + userData.lastName
            userType = userData.userType

            formList.append(
                FormDto(formId, documentId, str(senderId), formTitle, formDescription, date, userImage, userName,
                        userType))

            return formList

    def getAll(self):
        formList = []
        db = firestore.client()
        docs = db.collection(FirebaseCollection.FirebaseCollection.FORM_COLLECTION).stream()
        for doc in docs:
            dictionary = doc.to_dict()
            documentId = doc.id
            formId = dictionary["FormId"]
            senderId = dictionary["SenderId"]
            formTitle = dictionary["FormTitle"]
            formDescription = dictionary["FormDescription"]
            date = dictionary["Date"]
            userData = self.getUserData(senderId)
            userImage = userData.userImage
            userName = userData.firstName + " " + userData.lastName
            userType = userData.userType
            formList.append(
                FormDto(formId, documentId, str(senderId), formTitle, formDescription, date, userImage, userName,
                        userType))

        return formList

    def getUserData(self, userId):
        userManager = UserManager()
        userData = userManager.getById(userId)
        return userData
