from django.contrib import admin
from .models import Book


class AdminBook(admin.ModelAdmin):
    list_display = ('id', "name", "title", "price", "img", "author", "category", "created")

    list_filter = ('id', "price")
    ordering = ('id',)


admin.site.register(Book, AdminBook)
