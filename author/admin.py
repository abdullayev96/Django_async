from django.contrib import admin
from .models import Author


class AdminAuthor(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'bio')

    list_filter = ('id',)
    ordering = ('id',)


admin.site.register(Author, AdminAuthor)