import django.contrib.auth.models
import django.db.models
import django.urls
import django.utils.translation

from .managers import UserManager


class User(django.contrib.auth.models.AbstractUser):
    """
    Default custom user model.
    """

    # ROLES
    class Types(django.db.models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        OWNER = "OWNER", "Owner"
        EMPLOYEE = "EMPLOYEE", "Employee"
        CUSTOMER = "CUSTOMER", "Customer"

    role = django.db.models.CharField(
        max_length=20, choices=Types.choices, default=Types.ADMIN
    )

    # First and last name do not cover name patterns around the globe
    name = django.db.models.CharField(django.utils.translation.gettext_lazy("Name of User"), blank=True, max_length=255)
    first_name = django.db.models.CharField(max_length=200, default='', blank=True)  # type: ignore
    last_name = django.db.models.CharField(max_length=200, default="", blank=True)  # type: ignore
    email = django.db.models.EmailField(django.utils.translation.gettext_lazy("email address"), unique=True)
    username = None  # type: ignore
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return django.urls.reverse("users:detail", kwargs={"pk": self.id})

    def __str__(self):
        """For returning full names."""
        return f"{self.first_name} {self.last_name}"

