from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices, CharField, EmailField, BooleanField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    """
    Default custom user model.
    """

    # ROLES
    class Types(TextChoices):
        ADMIN = "ADMIN", "Admin"
        OWNER = "OWNER", "Owner"
        EMPLOYEE = "EMPLOYEE", "Employee"
        CUSTOMER = "CUSTOMER", "Customer"

    role =CharField(
        max_length=20, choices=Types.choices, default=Types.ADMIN
    )

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(max_length=200, default='', blank=True)  # type: ignore
    last_name = CharField(max_length=200, default="", blank=True)  # type: ignore
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore
    activated = BooleanField(blank=True, default=True)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})

    def __str__(self):
        """For returning full names."""
        return f"{self.first_name} {self.last_name}"

