from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from djangoProject2 import settings
from djangoProject2.Business.UserManager import UserManager
from djangoProject2.Constants.Constants import Constants
from djangoProject2.Entity.User import User
from djangoProject2.pages.profile import uploadImage
from localStorage import FileService


def index(request):
    if request.method == "POST":

        file = request.FILES["file"]
        firstName = request.POST.get("firstName", "")
        lastName = request.POST.get("lastName", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password")
        passwordAgain = request.POST.get("passwordAgain", "")

        if firstName != "" and lastName != "" and email != "" and password != "" and passwordAgain != "" and file != " ":
            if password == passwordAgain:
                result = addUser(User("", firstName, lastName, email, file, "user", password))
                if result:
                    uploadFileLocalStorage(file)
                    return HttpResponseRedirect("/form")
    return render(request, "pages/signUp.html")


def addUser(user):
    userManager = UserManager()
    return userManager.add(user)


def uploadFileLocalStorage(file):
    path = FileService.uploadFileLocalStorage(file)
    uploadImage(path)


def uploadImageToFirebase(path):
    userManager = UserManager()
    userManager.uploadImage(Constants.user_uuid, path)
    return True
