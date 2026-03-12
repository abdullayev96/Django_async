from django.db import models
from author.models import Author
from category.models import Category


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name="Kitob nomi")
    title = models.TextField(verbose_name="Kitob haqida")
    price = models.FloatField(verbose_name="Kitob narxi")
    img = models.ImageField(upload_to="book/", verbose_name="Kitob rasmi")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kitoblar_"
