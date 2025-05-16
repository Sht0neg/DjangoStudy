from django.urls import path
from products.views import *

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("catalog/", catalog, name="catalog"),
    path("all-authors/", api_get_all_author, name="api_all_authors"),
    path("<int:pk>/", book_card, name="book"),
    path("author/<int:pk>", author_card, name="author"),
]