from DataAccess.UserDal import UserDal


class UserManager:
    userDal = UserDal()

    def add(self, user):
        result = self.userDal.createUser(user)
        if (result != "" and result != False):
            user.Id = result
            self.userDal.add(user)
            return True
        else:
            return False

    def update(self, user):
        self.userDal.update(user)

    def delete(self, user):
        self.userDal.delete(user)

    def getById(self, id):
        self.userDal.getById(id)

    def getAll(self):
        self.userDal.getAll()
