
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from .views import home

urlpatterns = [
    path("schema/", include("apps.spectacular.urls")),
    path("users/", include("apps.users.urls")),
    path("", home, name="home"),
    path("admin/", admin.site.urls),
]
