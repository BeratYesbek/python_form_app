import firebase
from django.shortcuts import render, redirect
from django.http import HttpResponse

from djangoProject2.Business.UserManager import UserManager
from djangoProject2.Entity.User import User
from firebase_admin import auth


def index(request):
    return render(request, "pages/signIn.html")


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if email != "" and password != "":
            userManager = UserManager()
            result = userManager.login(email, password)
            return redirect('form')

    return render(request, "pages/signIn.html")
