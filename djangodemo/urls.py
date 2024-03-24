
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path("", include("apps.spectacular.urls")),
    path("users/", include("apps.users.urls")),
    path("admin/", admin.site.urls),
]
