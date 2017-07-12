import os

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.templatetags.static import static
from django.conf import settings

def index(request):
    estado = 'apagado'
    file_server = open(os.path.join(settings.BASE_DIR, 'static/status/server.txt'))
    file_mcserver = open(os.path.join(settings.BASE_DIR, 'static/status/mcserver.txt'))
    return render(request, 'monitor/index.html', {'estado': estado})

def encender(request):    
    if request.method == 'GET':
                print('encender')
    response = 'ok'
    return HttpResponse(response)