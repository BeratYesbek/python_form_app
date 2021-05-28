import datetime
import uuid

from django.http import HttpResponseRedirect
from django.shortcuts import render

from djangoProject2.Business.FormAnswerManager import FormAnswerManager
from djangoProject2.Business.FormManager import FormManager
from djangoProject2.Business.UserManager import UserManager
from djangoProject2.Constants import Constants
from djangoProject2.Entity.Answer import Answer
from djangoProject2.guard.loginGuard import loginGuard


def index(request, id):
    if not loginGuard():
        return HttpResponseRedirect("/home")

    if request.method == "POST":
        answerText = request.POST.get('answerText', "")
        answerId = request.POST.get("answerId", "")
        formId = request.POST.get("formId", "")
        editAnswerText = request.POST.get("editAnswerText", "")

        if answerId != "" and editAnswerText == "":
            deleteAnswer(id, answerId)
        elif formId != "" and editAnswerText == "":
            deleteForm(formId)
            return HttpResponseRedirect("/form")
        elif editAnswerText != "":
            updateAnswer(editAnswerText, answerId, id)
        else:
            sendAnswer(answerText, id)

    formDto = getFormData(id)
    answerDto = getFormAnswersData(id)
    user = userGetData()
    context = {
        'formDto': formDto,
        'user': user,
        'answerDto': answerDto,
    }
    return render(request, "pages/formDetail.html", context)


def updateAnswer(newAnswerText, answerId, formId):
    formAnswerManager = FormAnswerManager()
    formAnswerManager.update(Answer(answerId, Constants.Constants.user_uuid, newAnswerText, datetime.datetime.now()),
                             formId)


def deleteForm(formId):
    formManager = FormManager()
    formManager.delete(formId)


def deleteAnswer(formId, answerId):
    formAnswerManager = FormAnswerManager()
    formAnswerManager.delete(formId, answerId)


def sendAnswer(answerText, id):
    formAnswerManager = FormAnswerManager()
    answerId = str(uuid.uuid4())
    senderId = Constants.Constants.user_uuid
    formAnswerManager.add(Answer(answerId, senderId, answerText, datetime.datetime.now()), id)


def getFormAnswersData(formId):
    formAnswerManager = FormAnswerManager()
    return formAnswerManager.getAll(formId)


def getFormData(id):
    formManager = FormManager()
    return formManager.getById(id)


def userGetData():
    userManager = UserManager()
    user = userManager.getById(Constants.Constants.user_uuid)
    return user
