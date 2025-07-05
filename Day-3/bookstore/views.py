from django.contrib.auth.decorators import login_required, permission_required
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

@login_required
@permission_required('bookstore.add_book', raise_exception=True)
def book_create(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            form.save_m2m()
            return redirect("bookstore:bookstore-index")
    return render(request, "bookstore/book_create.html", context={"form": form}) 

@login_required
@permission_required('bookstore.change_book')
def book_update(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("bookstore:book-details", pk=book.id)
    return render(request, "bookstore/book_update.html", context={"form": form, 'book': book})

@login_required
@permission_required('bookstore.delete_book')
def book_delete(request, pk):
    Book.objects.get(id=pk).delete()
    return redirect("bookstore:bookstore-index")
