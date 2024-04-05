from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


# Create your views here.


class MenuListView(APIView):
    permission_classes = []
    authentication_classes = []
    renderer_classes = [JSONRenderer]

    def get(self, request):
        data = Menu.objects.values('id', 'title', 'link', 'slug')
        return Response(data)
