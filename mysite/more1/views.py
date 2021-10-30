from django.shortcuts import render


def more1(request):
    return render(request, 'more1/more1.html')