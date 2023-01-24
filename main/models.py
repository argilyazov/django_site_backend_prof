from django.db import models


class Article(models.Model):
    title = models.CharField("Название", max_length=255)
    text = models.TextField("Статья")

    def __str__(self):
        return self.title


class Statistic_by_year(models.Model):
    year = models.CharField("Год", max_length=255)
    average_salary = models.CharField("Средняя зарплата", max_length=255)
    average_salary_prof = models.CharField("Средняя зарплата - Backend-программист", max_length=255)
    count_salary = models.CharField("Количество вакансий", max_length=255)
    count_salary_prof = models.CharField("Количество вакансий - Backend-программист", max_length=255)

    def __str__(self):
        return f"Статистика за {self.year} год"


class Statistic_by_city_salary(models.Model):
    city = models.CharField("Город", max_length=255)
    salary_level = models.CharField("Уровень зарплат", max_length=255)

    def __str__(self):
        return f"Статистика по городу {self.city}"


class Statistic_by_city_count(models.Model):
    city = models.CharField("Город", max_length=255)
    salary_count = models.CharField("Доля вакансий", max_length=255)

    def __str__(self):
        return f"Статистика по городу {self.city}"


class Years(models.Model):
    year = models.CharField("Год", max_length=4)

    def __str__(self):
        return self.year


class Skill_statistics(models.Model):
    year = models.ForeignKey(Years, on_delete=models.CASCADE)
    skill = models.CharField("Навык", max_length=255)
    count = models.CharField("Количество упоминаний", max_length=6)

    def __str__(self):
        return f"{self.year.year} - {self.skill}"
