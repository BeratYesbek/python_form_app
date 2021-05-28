from django.core.files.storage import FileSystemStorage

from djangoProject2 import settings


def uploadFileLocalStorage(file):
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    path = str(settings.BASE_DIR) + "\\media\\" + filename
    return path
