# from django.http.response import HttpResponse, HttpResponseNotFound
# from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render  # noqa: F401
# from django.urls import reverse

# Create your views here.


'''
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


def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    # webpage = reverse('topic-page', args=[topic])
    # return HttpResponseRedirect(webpage)
    return HttpResponseRedirect(reverse('topic-page', args=[topic]))


def add_view(request, num1, num2):
    add_result = num1 + num2
    result = f'{num1} + {num2} = {add_result}'
    return HttpResponse(str(result))
'''


def simple_view(request):
    return render(request, 'first_app/example.html')
