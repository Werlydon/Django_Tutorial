from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. Take a seat, have some popcorn, we'll be here for a while...")
# Create your views here.
