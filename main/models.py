from django.db import models

class Article(models.Model):
    title = models.CharField("Название", max_length=255)
    text = models.TextField("Статья")

    def __str__(self):
        return self.title