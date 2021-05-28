"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from djangoProject2.pages import home, signIn, signUp, form, formDetail, profile, myQuestions
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path("admin", admin.site.urls, name="admin"),
                  path("", home.index, name=""),
                  path("home", home.index, name="home"),
                  path("signIn", signIn.index, name="signIn"),
                  path("signUp", signUp.index, name="signUp"),
                  path("form", form.index, name="form"),
                  path("login", signIn.login, name="login"),
                  path('formDetail/<str:id>', formDetail.index, name="formDetail"),
                  path('profile', profile.index, name="profile"),
                  path('myQuestions', myQuestions.index, name="myQuestions")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
