from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .permissions import *


from drf_spectacular.utils import extend_schema, extend_schema_view

# Create your views here.
@extend_schema_view(
    list=extend_schema(request=None, 
        description="Return the list of users."
    ),
    create=extend_schema(
        description="Create an user."
    ),
    retrieve=extend_schema(
        description="The retrieve action that returns a user selected by `id`."
    ),
    update=extend_schema(
        description="Delete a specified user identified by `id`"
    ),
    destroy=extend_schema(
        description="Delete an user."
    ),
    partial_update=extend_schema(
        description="""The retrieve action returns a user selected by `id`."""
    ),
)
class UserViewSet(viewsets.ViewSet):
   
    serializer_class = UserSerializer

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, format=None):        
        data = JSONParser().parse(request)        
        serializer = UserSerializer(data=data)       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
   
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        if pk:
            user=get_object_or_404(queryset, id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(f'User unknown: {pk}', status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        data = JSONParser().parse(request)
        user = User.objects.get(id=pk)
        print(user)
        serializer = UserSerializer(user, data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, id=None):
        pass

    def destroy(self, request, pk=None):
        queryset = User.objects.all()
        if id:
            user=get_object_or_404(queryset, id=pk)
            serializer = UserSerializer(user)
            if serializer.is_valid():
                user.delete()
                return Response(f'User deleted: {pk}', status=status.HTTP_202_ACCEPTED)
            return Response(f'User unknown: {pk}', status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
class PermissionView(APIView):
    serializer_class = UserSerializer
    
    @extend_schema(request=None, 
        description="Test permissions of user."
    )
    def get(self, request):
        queryset = User.objects.all()
        if request.user.is_staff:
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            content = {"message":"You don't have permission to access that ressource"}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        # raise PermissionDenied(content)
    
