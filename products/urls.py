from django.urls import path
from products.views import IndexListView, catalog

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("catalog/", catalog, name="catalog"),
]