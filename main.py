from DataAccess.UserDal import UserDal
from Entity.User import User
from Business.UserManager import UserManager

user = User("","Berat", "Yesbek", "beratyesbek@gmail.com", "123456")
manage = UserManager()
manage.getAll()
