from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField("Title", max_length=255, unique=True)
    description = models.TextField("Description")
    views = models.IntegerField(default=0)
    rate = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Title: {self.title}"
    
    class Meta:
        db_table = "books"