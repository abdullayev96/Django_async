from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, email, password=None, **extra_fields):
        """Email va parolni saqlashning asosiy logikasi."""
        if not email:
            raise ValueError('Email kiritilishi shart')

        # EMAILNI NORMALLASHTIRISH (MUHIM!)
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        # is_active odatda True bo'lishi kerak
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuserda is_staff=True bo‘lishi shart.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuserda is_superuser=True bo‘lishi shart.')

        return self._create_user(email, password, **extra_fields)