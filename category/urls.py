from django.urls import path
from .views import AuthorListAPI


urlpatterns = [
    path("category", AuthorListAPI.as_view())
]