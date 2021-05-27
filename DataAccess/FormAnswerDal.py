from firebase_admin import firestore

from djangoProject2.Business.UserManager import UserManager
from djangoProject2.Constants import FirebaseCollection
from djangoProject2.Entity.Dto.AnswerDto import AnswerDto


class FormAnswerDal:

#firebase code
    def getAll(self, formId):
        answerList = []
        db = firestore.client()
        print(formId)
        docs = db.collection(FirebaseCollection.FirebaseCollection.FORM_ANSWER_COLLECTION).document(
            str(formId)).collection(str(formId)).stream()
        for doc in docs:
            dictionary = doc.to_dict()
            documentId = doc.id
            answerId = dictionary["AnswerId"]
            senderId = dictionary["SenderId"]
            answerText = dictionary["AnswerText"]
            date = dictionary["Date"]
            userData = self.getUserData(senderId)
            userImage = userData.userImage
            userName = userData.firstName + " " + userData.lastName
            userType = userData.userType
            answerList.append(
                AnswerDto(answerId, documentId, str(senderId), answerText, date, userImage, userName,userType))
        return answerList

    def add(self, answer, formId):
        db = firestore.client()
        doc_ref = db.collection(FirebaseCollection.FirebaseCollection.FORM_ANSWER_COLLECTION).document(
            str(formId)).collection(
            str(formId)).document(answer.AnswerId)
        doc_ref.set({
            'AnswerId': answer.AnswerId,
            'SenderId': answer.SenderId,
            'AnswerText': answer.AnswerText,
            'Date': answer.Date,
        })

    def delete(self,formId,answerId):
        db = firestore.client()
        doc_ref = db.collection(FirebaseCollection.FirebaseCollection.FORM_ANSWER_COLLECTION).document(
            str(formId)).collection(
            str(formId)).document(answerId)

        doc_ref.delete()


    def getUserData(self, userId):
        userManager = UserManager()
        userData = userManager.getById(userId)
        return userData
