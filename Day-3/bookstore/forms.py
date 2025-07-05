from django.forms import forms, ModelForm
from .models import Book, Category

class BookForm(ModelForm):
    class Meta:
        model = Book
        # fields = "__all__"
        fields = ['title', 'description', 'rate', 'categories']
    
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if not (10 <= len(title) <= 50):
    #         raise forms.ValidationError("Book title must be between 10 and 50 characters.")
    #     return title

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) < 2:
    #         raise forms.ValidationError("Category name too short.")
    #     return name
