from django.db import models
from django.conf import settings
import os
from django.core.exceptions import ValidationError
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver


def validate_files(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('You must enter .png, .jpg  format !!!')


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=200, verbose_name="To'liq ismi:", blank=True, null=True)
    number = models.CharField(max_length=20, verbose_name="Telefon nomer:", blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} profili"

    class Meta:
        verbose_name = "Profile_"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
