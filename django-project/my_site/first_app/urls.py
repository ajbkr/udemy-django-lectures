from django.urls import path

from . import views


urlpatterns = [
    path('', views.simple_view)
    # path('simple_view', views.simple_view)
]
