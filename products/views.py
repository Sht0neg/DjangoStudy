from django.shortcuts import render, redirect
from products.models import *
from django.views.generic import ListView
from django.http import HttpRequest, JsonResponse
from django.urls import reverse
from datetime import *

class IndexListView(ListView):
    model = Book
    template_name = "index.html"
    context_object_name = "books"

def catalog(request: HttpRequest):
    author = request.GET.get("author")
    date = request.GET.get("date")
    if (author and date):
        books = Book.objects.filter(publication_date__gte=datetime.strptime(str(date), '%Y')) & Book.objects.filter(authors=author)
    elif(author):
        books = Book.objects.filter(authors=author)
    elif(date):
        books = Book.objects.filter(publication_date__gte=datetime.strptime(str(date), '%Y'))
    else:
        books = Book.objects.all()
    return render(request, "catalog.html", {"books":books})

def book_card(request: HttpRequest, pk: int):
    if (pk):
        book = Book.objects.get(id=pk)
        author = Author.objects.filter(books=book)[0]
        return render(request, "book_card.html", {"book":book, "author":author})
    return reverse("catalog")

def about(req):
    return render(req, "about.html")

def review(req):
    reviews = Review.objects.all()
    return render(req, "review.html", {"reviews":reviews})

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

def api_get_all_dates(request):
    books = Book.objects.all()
    dataList = list(set([book.publication_date.year for book in books]))
    return JsonResponse(dataList, safe=False)

def cart(reg):
    pass

def add_book_to_cart(req:HttpRequest, book_id:int):
    book = Book.objects.get(id=book_id)
    user = req.user
    cart = Cart(user=user)
    cart.save()
    cart.books.set([book,])
    return redirect(reverse("catalog"))