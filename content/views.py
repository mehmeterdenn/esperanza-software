from django.http import HttpResponse


def index(request):
    return HttpResponse("Content Sayfası")
