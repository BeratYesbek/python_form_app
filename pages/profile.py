from django.http import HttpResponseRedirect
from django.shortcuts import render

from djangoProject2.Business.UserManager import UserManager
from djangoProject2.Constants.Constants import Constants
from django.core.files.storage import FileSystemStorage
from djangoProject2 import settings
from djangoProject2.Entity.User import User
from djangoProject2.guard.loginGuard import loginGuard
from localStorage import FileService


def index(request):
    if not loginGuard():
        return HttpResponseRedirect("/home")

    if request.method == "POST":
        imageFile = request.FILES['file']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        updateUser(firstName, lastName)
        uploadFileLocalStorage(imageFile)
    user = userGetData()

    context = {
        'user': user,
    }
    return render(request, "pages/profile.html", context)




def uploadFileLocalStorage(file):
    path = FileService.uploadFileLocalStorage(file)
    uploadImage(path)

def updateUser(firstName, lastName):
    if firstName != "" and lastName != "":
        userManager = UserManager()
        userManager.update(User(Constants.user_uuid, firstName, lastName, "", "", ""))


def uploadImage(uploaded_file_url):
    userManager = UserManager()
    userManager.uploadImage(Constants.user_uuid, uploaded_file_url)


def userGetData():
    userManager = UserManager()
    user = userManager.getById(Constants.user_uuid)
    return user
