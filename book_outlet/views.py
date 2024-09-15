from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import Avg

# Create your views here.
def index(request):
    books=Book.objects.all().order_by("rating") #order_by("-rating") make decinding order
    num_books=books.count()
    avg=books.aggregate(Avg("rating"))
    return render(request,"book_outlet/index.html",{
        "books":books,
        "total_no_of_books":num_books,
        "avg_rating":avg,
    })
def book_detail(request,slug):
    # try:
    #     book=Book.objects.get(pk=id)
    # except:
    #     raise Http404() 
    book= get_object_or_404(Book, slug=slug)  # same as upper 4 line of code
    return render(request,"book_outlet/book_detail.html",{
    "title": book.title,
    "rating": book.rating,
    "author": book.author,
    "is_bestseller": book.is_bestselling,
    })

