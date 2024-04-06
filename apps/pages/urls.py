from django.urls import path
from .views import *
from .apiviews import *

urlpatterns = [
    path("", home, name="home"),
    path("services/", ServicesView.as_view(), name="services"),
    path("links/", LinksView.as_view(), name="links"),
    path("about/", about, name="about"),
    path("menus/", menus_list, name="menus"),
    path("info/", get_info, name="info"),
]
