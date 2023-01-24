from django.contrib import admin
from .models import Statistic_by_year
from .models import Statistic_by_city_salary
from .models import Statistic_by_city_count
from .models import Article
from .models import Skill_statistics
from .models import Years

# Register your models here.
admin.site.register(Article)
admin.site.register(Statistic_by_year)
admin.site.register(Statistic_by_city_salary)
admin.site.register(Statistic_by_city_count)
admin.site.register(Skill_statistics)
admin.site.register(Years)
