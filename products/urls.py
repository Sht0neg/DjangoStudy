from django.urls import path
from products.views import *

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("catalog/", catalog, name="catalog"),
    path("all-authors/", api_get_all_author, name="api_all_authors"),
    path("<int:pk>/", book_card, name="book"),
    path("author/<int:pk>", author_card, name="author"),
    path("about/", about, name="about"),
    path("review/", review, name="review"),
    path("dates/", api_get_all_dates, name="api_all_dates"),
    path("cart/<int:pk>", cart, name="cart"),
    path("catalog/add-book-to-cart/<int:book_id>", add_book_to_cart, name="add_book_to_cart"),
]