from rest_framework import serializers
from .models import *


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('title', 'link',)


class MenuSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True) 
    class Meta:
        model = Menu
        fields = ('title', 'link', 'hasChild','items',)
