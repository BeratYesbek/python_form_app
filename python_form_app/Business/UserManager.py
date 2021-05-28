from djangoProject2.DataAccess.UserDal import UserDal


class UserManager:
    userDal = UserDal()

    def add(self, user):
        result = self.userDal.createUser(user)
        if (result != "" and result != False):
            user.Id = result
            self.userDal.add(user)
            return True

        return False

    def login(self, email, password):
        result = self.userDal.login(email, password)
        return result
    def createUser(self,user):
        return self.userDal.createUser(user)

    def update(self, user):
        self.userDal.update(user)

    def delete(self, user):
        self.userDal.delete(user)

    def getById(self, id):
        return self.userDal.getById(id)

    def getAll(self):
        return self.userDal.getAll()

    def uploadImage(self, userId, file):
        return self.userDal.uploadImage(userId, file)
