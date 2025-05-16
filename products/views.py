from django.shortcuts import render
from products.models import *
from django.views.generic import ListView
from django.http import HttpRequest, JsonResponse
from django.urls import reverse

class IndexListView(ListView):
    model = Book
    template_name = "index.html"
    context_object_name = "books"

def catalog(request: HttpRequest):
    author = request.GET.get("author")
    if (author):
        books = Book.objects.filter(authors=author)
    else:
        books = Book.objects.all()
    return render(request, "catalog.html", {"books":books})

def book_card(request: HttpRequest, pk: int):
    if (pk):
        book = Book.objects.get(id=pk)
        author = Author.objects.filter(books=book)[0]
        return render(request, "book_card.html", {"book":book, "author":author})
    return reverse("catalog")

def author_card(request: HttpRequest, pk: int):
    print(pk)
    if (pk):
        author = Author.objects.get(id=pk)
        books = Book.objects.filter(authors=author)
        return render(request, "author_card.html", {"author":author, "books":books})

def api_get_all_author(request):
    authors = Author.objects.all()
    dataList = [author.parse_object() for author in authors]
    return JsonResponse(dataList, safe=False)
