from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from .models import Author, Book, BookInstance, Genre, Language  # noqa: F401


def index(request):
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()

    num_instances_avail = BookInstance.objects.filter(
        status__exact='a'
    ).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_avail': num_instances_avail,
    }

    return render(request, 'catalog/index.html', context=context)


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'


class BookDetailView(DetailView):
    model = Book


@login_required
def my_view(request):
    return render(request, 'catalog/my_view.html')
