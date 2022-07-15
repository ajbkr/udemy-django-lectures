from django.http.response import HttpResponse
from django.shortcuts import render  # noqa: F401

# Create your views here.


def simple_view(request):
    return HttpResponse('SIMPLE VIEW')
