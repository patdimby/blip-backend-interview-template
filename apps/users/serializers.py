
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import *
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'name', 'role')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 6}}

        def create(self, validated_data):
            user = User.objects.create_user('name',validated_data['email'],
                validated_data['password'],)
            return user

class AuthTokenSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField(
        style = {'input_type':'password'},
        trim_whitespace = False
    )

    def validate(self, attrs):

        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password
        )

        if not user:

            msg = 'Unable to authenticate with provided crendetial.'
            raise serializers.ValidationError(msg, code = 'authorization')

        attrs['user'] = user

        return attrs