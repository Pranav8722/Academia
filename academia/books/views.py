from django.shortcuts import render
from .models import Book

def books_list(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'books/books_list.html', {'books': books})

def books_list(request):
    query = request.GET.get('q', '')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})