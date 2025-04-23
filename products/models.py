from django.db import models

class Author(models.Model):
    name = models.CharField(verbose_name="Полное имя автора", max_length=80)
    bio = models.TextField(verbose_name="Краткая биография автора")

class Book(models.Model):
    title = models.CharField(verbose_name="Название", max_length=120)
    desc = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    publication_date = models.DateField(verbose_name="Дата публикации")

    date_create = models.DateTimeField(verbose_name="Дата добавления", auto_now_add=True)
    date_edit = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    authors = models.ManyToManyField(Author, related_name="books", verbose_name="Автор(ы)")

