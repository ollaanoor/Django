from django.urls import path
# from . import views
from .views import index, book_details, book_create, book_update, book_delete

# Define the app name for namespacing
# This allows you to refer to this app's URLs in templates and other places
# using the format 'todo:index' for the index view.
# This is useful for avoiding name clashes with other apps in the project.
app_name = 'bookstore'  

urlpatterns = [
    path('index', index, name='bookstore-index'),
    # path('books', books_list, name='books-list'),
    path('books/<int:pk>', book_details, name='book-details'),
    path('create', book_create, name="book-create"),
    path('delete/<int:pk>', book_delete, name="book-delete"),
    path('update/<int:pk>', book_update, name="book-update")
]