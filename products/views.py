from django.shortcuts import render
from products.models import *
from django.views.generic import ListView
from django.http import HttpRequest, JsonResponse

class IndexListView(ListView):
    model = Book
    template_name = "index.html"
    context_object_name = "books"

def catalog(request: HttpRequest):
    author = request.GET.get("author")
    if (author):
        books = Book.objects.filter(author=author)
    else:
        books = Book.objects.all()
    return render(request, "catalog.html", {"books":books})

def api_get_all_author(request):
    authors = Author.objects.all()
    dataList = [author.parse_object() for author in authors]
    return JsonResponse(dataList, safe=False)
