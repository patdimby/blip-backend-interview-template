from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import *

def start():
    context = dict()
    infos = Address.objects.all()
    # owner informations
    if len(infos) > 0:
        context['address'] = infos[0]
    # services
    context['services'] = Service.objects.all()   
    # links
    context['links'] = Link.objects.all()
    return context


def home(request):
    """" Home page."""
    context = start()
    return render(request, 'pages/index.html', {'context': context})


def services(request):
    """ Services page. """
    context = start()
    return render(request, 'pages/services.html', {'context': context})


def about(request):
    """ About page. """
    context = start()
    set_context(context, 'about')
    return render(request, 'pages/about.html', {'context': context})


def set_context(context, link: str):
    menu = Menu.objects.get(link=link)
    data = {'name': menu.link.capitalize(), 'title': menu.title}
    context['page'] = data


@csrf_exempt
def menus_list(request):
    """ List all menus. """
    if request.method == 'GET':
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return JsonResponse(serializer.data, safe=False)
