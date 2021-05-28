from django.http import HttpResponseRedirect
from django.shortcuts import render

from djangoProject2.Business.FormManager import FormManager
from djangoProject2.Business.UserManager import UserManager
from djangoProject2.Constants.Constants import Constants
from djangoProject2.DataAccess.FormDal import FormDal
from djangoProject2.guard.loginGuard import loginGuard


def index(request):
    if not loginGuard():
        return HttpResponseRedirect("/home")

    forms = getFormData()
    user = userGetData()
    context = {
        'user': user,
        'forms': forms,
    }
    return render(request, "pages/myQuestions.html", context)


def getFormData():
    formManager = FormManager()
    return formManager.getByUserId(Constants.user_uuid)


def userGetData():
    userManager = UserManager()
    user = userManager.getById(Constants.user_uuid)
    return user
