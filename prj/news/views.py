from django.shortcuts import render
from .models import New


def index(request):
    news = New.objects.all()
    return render(request, 'index.html', context={'news': news})


def details(request, slug):
    new = New.objects.get(slug__iexact=slug)
    return render(request, 'details.html', context={'new': new})
