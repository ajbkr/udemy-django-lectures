# from django.http.response import HttpResponse, HttpResponseNotFound
from django.http.response import Http404, HttpResponse
from django.shortcuts import render  # noqa: F401

# Create your views here.


articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}


def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except KeyError:
        # result = 'No page for that topic!'
        # return HttpResponseNotFound(result)
        raise Http404('404 GENERIC ERROR')


def add_view(request, num1, num2):
    add_result = num1 + num2
    result = f'{num1} + {num2} = {add_result}'
    return HttpResponse(str(result))
