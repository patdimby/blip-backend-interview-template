from django.urls import path, include
from rest_framework import routers
from . import views

# from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('', views.UserViewSet, basename='user')

urlpatterns = [
    path('list/', views.PermissionView.as_view(), name='list'),
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
