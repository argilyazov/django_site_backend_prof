from django.shortcuts import render
from .models import Statistic_by_year
from .models import Statistic_by_city_salary
from .models import Statistic_by_city_count
from .models import Article
import requests
import json


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
    url = 'https://api.hh.ru/vacancies?text=backend+OR+%D0%B1%D1%8D%D0%BA%D0%B5%D0%BD%D0%B4+OR+%D0%B1%D1%8D%D0%BA%D1%8D%D0%BD%D0%B4+OR+%D0%B1%D0%B5%D0%BA%D0%B5%D0%BD%D0%B4+OR+%D0%B1%D0%B5%D0%BA%D1%8D%D0%BD%D0%B4+OR+back%20end+OR+%D0%B1%D1%8D%D0%BA%20%D1%8D%D0%BD%D0%B4+OR+%D0%B1%D1%8D%D0%BA%20%D0%B5%D0%BD%D0%B4+OR+django+OR+flask+OR+laravel+OR+yii+OR+symfony&date_from=2022-12-01&date_to=2022-12-31'
    response = requests.get(url).text
    vacancies = sorted(json.loads(response)["items"], key = lambda vac: int(vac['published_at'][8:10]), reverse=True)[:10]
    full_vac=[]
    for vacancy in vacancies:
        response= requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}').text
        full_vac.append(json.loads(response))
    return render(request, 'main/last_vac.html', {'vacancies':full_vac})
