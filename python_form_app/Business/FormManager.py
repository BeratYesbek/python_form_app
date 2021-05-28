from djangoProject2.DataAccess.FormDal import FormDal


class FormManager:
    formDal = FormDal()

    def add(self, form):
        self.formDal.add(form)

    def update(self, form):
        self.formDal.update(form)

    def delete(self, formId):
        self.formDal.delete(formId)

    def getById(self, id):
        return self.formDal.getById(id)

    def getAll(self):
        return self.formDal.getAll()

    def getFormAnswersById(self, id):
        return self.formDal.getFormAnswersById(id)

    def getByUserId(self,id):
        return self.formDal.getByUserId(id)
