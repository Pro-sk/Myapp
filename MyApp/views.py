from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return HttpResponse(request.is_secure())
    # return HttpResponse(request.get_port())
    # request.headers['user-agent'] 7039638931