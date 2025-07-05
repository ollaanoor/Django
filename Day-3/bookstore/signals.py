from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, ISBN
import uuid

@receiver(post_save, sender=Book)
def create_isbn_for_book(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'isbn'):
        ISBN.objects.create(
            book=instance,
            book_title=instance.title,
            author_title=instance.owner.get_full_name() or instance.owner.username,
            isbn_number=str(uuid.uuid4())[:13],
        )