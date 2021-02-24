from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author
# Create your views here.

def index(request):
    context = {
        "books_DB": Book.objects.all()
    }
    return render(request, "index.html", context)

def authors(request):
    context = {
        "authors_DB": Author.objects.all()
    }
    return render(request, "authors.html", context)