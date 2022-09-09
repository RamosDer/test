from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola mundo. Usted se encuentra en el index de polls.")