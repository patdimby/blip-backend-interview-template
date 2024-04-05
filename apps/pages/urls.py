from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("services/", services, name="services"),
    path("about/", about, name="about"),
    path("menus/", menus_list, name="menus"),
]
