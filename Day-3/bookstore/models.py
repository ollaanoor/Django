from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# import uuid

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def clean(self):
        if len(self.name) < 2:
            raise ValidationError('Category name must be at least 2 characters.')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField("Title", max_length=100, unique=True)
    description = models.TextField("Description")
    views = models.IntegerField(default=0)
    rate = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    categories = models.ManyToManyField(Category, related_name='books')
    # isbn = models.OneToOneField(ISBN, on_delete=models.CASCADE, related_name='book')

    def clean(self):
        if not (10 <= len(self.title) <= 50):
            raise ValidationError('Book title must be between 10 and 50 characters.')
        
    def __str__(self):
        return f"Title: {self.title}"
    
    class Meta:
        db_table = "books"

class ISBN(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='isbn')
    author_title = models.CharField(max_length=200)
    book_title = models.CharField(max_length=200)
    isbn_number = models.CharField(max_length=13, unique=True)
    # number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.book_title} by {self.author_title}"