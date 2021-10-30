from django.urls import path

from . import views

urlpatterns = [
    path('', views.more2, name='more2'),
]
