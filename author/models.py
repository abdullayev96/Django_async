from django.db import models

# Create your models here.


class Author(models.Model):
    full_name = models.CharField(max_length=300, verbose_name="Yozuvchi F.I.SH")
    bio = models.TextField(verbose_name="Yozuvchi  haqida ")
    image = models.ImageField(upload_to="img/", verbose_name="Yozuvchi  rasmi ", null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Author_"
