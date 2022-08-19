from django.urls import path

from .views import (
    ContactFormView,
    HomeView,
    TeacherCreateView,
    TeacherListView,
    ThankYouView,
)


app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path(
        'create_teacher/',
        TeacherCreateView.as_view(),
        name='create_teacher'
    ),
    path(
        'list_teachers/',
        TeacherListView.as_view(),
        name='list_teachers'
    ),
]
