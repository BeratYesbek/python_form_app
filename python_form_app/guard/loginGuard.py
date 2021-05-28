from django.http import HttpResponseRedirect

from djangoProject2.Constants import Constants

#If you do not log in the system you can't go other URL
def loginGuard():
    if Constants.Constants.user_uuid == "":
        return False

    return True
