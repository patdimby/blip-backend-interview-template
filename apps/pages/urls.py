from django.urls import path
from .views import home, services, about


urlpatterns = [
    path("", home, name="home"),
    path("services/", services, name="services"),
    path("about/", about, name="about"),
]