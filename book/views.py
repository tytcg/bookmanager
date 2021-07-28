from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import BookInfo


def index(request):

    obj = BookInfo.objects.all()
    print(obj)
    return HttpResponse("ok")