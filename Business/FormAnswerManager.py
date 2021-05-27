from djangoProject2.DataAccess.FormAnswerDal import FormAnswerDal

# this class is able to add update and delete the answer in form
class FormAnswerManager:
    formAnswerDal = FormAnswerDal()

    def add(self, answer, formId):
        return self.formAnswerDal.add(answer, formId)

    def delete(self, formId, answerId):
        return self.formAnswerDal.delete(formId, answerId)

    def getAll(self, formId):
        return self.formAnswerDal.getAll(formId)
