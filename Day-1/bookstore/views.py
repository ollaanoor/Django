from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'main/base_layout.html')

books = [
    {'id': 1, 'title': 'Book 1', 'description': 'Description for Book 1', 'author': 'Author1'},
    {'id': 2, 'title': 'Book 2', 'description': 'Description for Book 2', 'author': 'Author2'},
    {'id': 3, 'title': 'Book 3', 'description': 'Description for Book 3', 'author': 'Author3'},
]

def books_list(request):
    my_context = {
        'books_list': books,
    }
    return render(request, 'bookstore/books_list.html', context=my_context)

def _get_book_by_id(book_id):
    for book in books:
        if 'id' in book and book['id'] == book_id:
            return book
    return None

def book_details(request, *args, **kwargs):
    book_id = kwargs.get('book_id')
    book_obj = _get_book_by_id(book_id)
    my_context = {
        'book_id': book_obj.get('id'),
        'book_title': book_obj.get('title'),
        'book_description': book_obj.get('description'),
        'book_author': book_obj.get('author'),
    }
    
    if book_obj is None:
        return HttpResponse("Book not found", status=404)
    
    return render(request, 'bookstore/book_details.html', context=my_context)

def book_create(request):
    new_book = {
        'id': len(books) + 1,
        'title': f'Book {len(books) + 1}',
        'description': f'Description for Book {len(books) + 1}',
        'author': f'Author{len(books) + 1}'
    }
    books.append(new_book)
    return redirect('bookstore:books-list')  

def book_update(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_obj = _get_book_by_id(book_id)
    for book in books:
        if book == book_obj:
            book['title'] = f"Updated {book_obj['title']}"
            
    return redirect('bookstore:books-list')  

def book_delete(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_obj = _get_book_by_id(book_id)
    if books:
        books.remove(book_obj)
    return redirect('bookstore:books-list')  