from django.urls import path
from .views import BookListAPI


urlpatterns = [
    path("book", BookListAPI.as_view())
]