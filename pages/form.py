import datetime
import uuid

from django.shortcuts import render
from django.http import HttpResponseRedirect

from djangoProject2.Business.FormManager import FormManager
from djangoProject2.Business.UserManager import UserManager
from djangoProject2.Constants import Constants
from djangoProject2.Entity.Form import Form

from djangoProject2.guard.loginGuard import loginGuard


def index(request):
    if not loginGuard():
        return HttpResponseRedirect("/home")
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        formId = str(uuid.uuid4())
        senderId = Constants.Constants.user_uuid
        formManager = FormManager()
        formManager.add(Form(formId, senderId, title, description, datetime.datetime.now()))

    forms = getFormData()
    user = userGetData()
    context = {
        'user': user,
        'forms': forms,
    }
    return render(request, "pages/form.html", context)




def getFormData():
    formManager = FormManager()
    return formManager.getAll()


def userGetData():
    userManager = UserManager()
    user = userManager.getById(Constants.Constants.user_uuid)
    return user
