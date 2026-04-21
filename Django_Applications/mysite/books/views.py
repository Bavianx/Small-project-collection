from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  #Only grabs the LIST of books rather than individual books (Displays all content)
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)  #Grabs a SINGULAR book by the primary key identifier similar to ( self.stocks[ticker] where we take the ticker from the main body ) 
    return render(request, 'books/book_detail.html', {'book': book})
