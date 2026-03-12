from django.urls import path
from .views import AuthorListAPI

urlpatterns = [
    path("authors", AuthorListAPI.as_view())
]