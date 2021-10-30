from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'about_us/about_us.html')