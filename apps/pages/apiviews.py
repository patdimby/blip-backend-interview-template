from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


# Create your views here.


class LinksView(APIView):
    """ List links to display."""
    permission_classes = []
    authentication_classes = []
    renderer_classes = [JSONRenderer]

    def get(self, request):
        data = Link.objects.values('title', 'url',)
        return Response(data)
    
class ServicesView(APIView):
    """ List services to display."""
    permission_classes = []
    authentication_classes = []
    renderer_classes = [JSONRenderer]

    def get(self, request):
        data = Service.objects.values('title', 'url',)
        return Response(data)
