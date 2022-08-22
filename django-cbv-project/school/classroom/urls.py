from django.urls import path

from .views import (
    ContactFormView,
    HomeView,
    TeacherCreateView,
    TeacherDeleteView,
    TeacherDetailView,
    TeacherListView,
    TeacherUpdateView,
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
    path(
        'view_teacher/<int:pk>',
        TeacherDetailView.as_view(),
        name='view_teacher'
    ),
    path(
        'update_teacher/<int:pk>',
        TeacherUpdateView.as_view(),
        name='update_teacher'
    ),
    path(
        'delete_teacher/<int:pk>',
        TeacherDeleteView.as_view(),
        name='delete_teacher'
    ),
]
