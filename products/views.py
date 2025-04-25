from django.shortcuts import render
from products.models import Book
def index(req):
    books = Book.objects.all()
    return render(req, 'index.html', {"books" : books})
