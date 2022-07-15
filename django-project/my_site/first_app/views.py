from django.http.response import HttpResponse
from django.shortcuts import render  # noqa: F401

# Create your views here.


articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}


def news_view(request, topic):
    return HttpResponse(articles[topic])


def add_view(request, num1, num2):
    add_result = num1 + num2
    result = f'{num1} + {num2} = {add_result}'
    return HttpResponse(str(result))
