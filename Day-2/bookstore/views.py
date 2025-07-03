from django.shortcuts import render, redirect
from bookstore.models import Book
from bookstore.forms import BookForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, "bookstore/book_index.html", context={"books": books})

def book_details(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, "bookstore/book_details.html", context={"book": book})

def book_create(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bookstore:bookstore-index")
    return render(request, "bookstore/book_create.html", context={"form": form}) 

def book_update(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("bookstore:book-details", pk=book.id)
    return render(request, "bookstore/book_update.html", context={"form": form, 'book': book})

def book_delete(request, pk):
    Book.objects.get(id=pk).delete()
    return redirect("bookstore:bookstore-index")