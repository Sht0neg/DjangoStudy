from django.contrib import admin
from products.models import Author, Book, Review, Cart

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Cart)


