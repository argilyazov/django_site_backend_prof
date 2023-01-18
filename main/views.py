from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .models import Statistic_by_year
from .models import Statistic_by_city_salary
from .models import Statistic_by_city_count
from .models import Article


def index(request):
    art = Article.objects.all()[0]
    return render(request, 'main/index.html', {"article": art})


def demand(request):
    statistics_by_year = Statistic_by_year.objects.all()
    statistics_by_city_salary = Statistic_by_city_salary.objects.all()
    statistics_by_city_count = Statistic_by_city_count.objects.all()

    return render(request, 'main/demand.html',
                  {"statistics_by_year": statistics_by_year, "statistics_by_city_salary": statistics_by_city_salary,
                   "statistics_by_city_count": statistics_by_city_count})


def geography(request):
    statistics_by_city_salary = Statistic_by_city_salary.objects.all()
    statistics_by_city_count = Statistic_by_city_count.objects.all()

    return render(request, 'main/geography.html',
                  {"statistics_by_city_salary": statistics_by_city_salary,
                   "statistics_by_city_count": statistics_by_city_count})


def skills(request):
    return render(request, 'main/skills.html')


def last_vac(request):
    return render(request, 'main/last_vac.html')
