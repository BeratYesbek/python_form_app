from django.shortcuts import render
from django.http import HttpResponse

from djangoProject2.Business.UserManager import UserManager


def index(request):
    return render(request, "pages/home.html")
