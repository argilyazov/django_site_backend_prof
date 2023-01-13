from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    art= Article.objects.all()[0]
    return render(request,'main/index.html',{"article":art.text})


def demand(request):
    return render(request,'main/demand.html')


def geography(request):
    return render(request,'main/geography.html')


def skills(request):
    return render(request,'main/skills.html')


def last_vac(request):
    return render(request,'main/last_vac.html')

