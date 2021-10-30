from django.urls import path

from . import views

urlpatterns = [
    path('', views.more1, name='more1'),
]
