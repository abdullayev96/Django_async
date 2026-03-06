from django.urls import path
from .views import CategoryListAPI


urlpatterns = [
    path("category", CategoryListAPI.as_view())
]