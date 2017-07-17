import os

from django.shortcuts import render
from django.conf import settings


def index(request):
    
    estado_server = 'apagado'
    estado_mc = 'apagado'
    file_server = open(os.path.join(settings.BASE_DIR, 'static/status/server.txt')).read()
    file_mc = open(os.path.join(settings.BASE_DIR, 'static/status/mc.txt')).read()
    if 'encendido' in file_server:
        estado_server = 'encendido'
    if 'encendido' in file_mc:
        estado_mc = 'encendido'
    return render(request, 'home/index.html', {'estado_mc': estado_mc, 
                                                  'estado_server': estado_server, 
                                                  })
