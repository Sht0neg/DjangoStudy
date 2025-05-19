from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(verbose_name="Полное имя автора", max_length=80)
    bio = models.TextField(verbose_name="Краткая биография автора")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
    def parse_object(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Book(models.Model):
    title = models.CharField(verbose_name="Название", max_length=120)
    desc = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    publication_date = models.DateField(verbose_name="Дата публикации")

    date_create = models.DateTimeField(verbose_name="Дата добавления", auto_now_add=True)
    date_edit = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    authors = models.ManyToManyField(Author, related_name="books", verbose_name="Автор(ы)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ("-date_create", )

class Review(models.Model):
    content = models.TextField(verbose_name="Содержимое отзыва")

    date_create = models.DateTimeField(verbose_name="Дата добавления", auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_query_name="reviews")

    def __str__(self):
        return self.user.username + " " + self.date_create.strftime('%Y-%m-%d')

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


