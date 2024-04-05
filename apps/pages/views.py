from django.shortcuts import render
from .models import *
# Create your views here.


def start():
    context = dict()
    infos = Address.objects.all()
    # owner informations
    if len(infos) > 0:
        context['address'] = infos[0]
    # services
    context['services'] = Service.objects.all()
    # menus
    context['menus'] = Menu.objects.all()
    # links
    context['links'] = Link.objects.all()
    return context

def home(request):
    """" Home page."""    
    context = start()   
    return render(request, 'pages/index.html', {'context': context})

def services(request):
    context = start()
    return render(request, 'pages/index.html', {'context': context})

def about(request):
    context = start()
    set_context(context,'about')
    return render(request, 'pages/about.html', {'context': context})

def set_context(context, link:str):
    menu = Menu.objects.get(link=link)
    data = {'name': menu.link.capitalize(), 'title':  menu.title}
    context['page'] = data