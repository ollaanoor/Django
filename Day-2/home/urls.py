from django.urls import path
# from . import views
from .views import index

urlpatterns = [
    path('', index, name='home-index'),  # Home page URL
]