from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError(_("Users must have a username."))

        if email is None:
            raise TypeError(_("Users must have an email address."))

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """Create and return a `User` with superuser (admin) permissions."""
        if password is None:
            raise TypeError(_("Superusers must have a password."))
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(username, email, password, **extra_fields)
