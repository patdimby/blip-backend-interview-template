from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import *

context = dict()    
context['address'] = Address.objects.get(pk=2)



def home(request):
    """" Home page.""" 
    context['services'] = Service.objects.all()
    return render(request, 'pages/index.html', {'context': context})


def services(request):
    """ Services page. """
    context['services'] = Service.objects.all()
    return render(request, 'pages/services.html', {'context': context})


def about(request):
    """ About page. """
    context['services'] = Service.objects.all()
    return render(request, 'pages/about.html', {'context': context})


@csrf_exempt
def menus_list(request):
    """ List all menus. """
    if request.method == 'GET':
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def get_info(request):
    """ Get informations. """    
    if request.method == 'GET':
        infos = Address.objects.get(pk=2)
        serializer = AddressSerializer(infos)
        return JsonResponse(serializer.data, safe=False)
