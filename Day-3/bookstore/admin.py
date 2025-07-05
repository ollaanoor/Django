from django.contrib import admin
from .models import Book, Category, ISBN

# Register your models here.
class ISBNInline(admin.StackedInline):  # stacked inline usage
    model = ISBN
    extra = 1

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']
    list_filter = ['categories']
    inlines = [ISBNInline]

admin.site.register(Category)