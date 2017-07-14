import os
import subprocess

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.templatetags.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

def index(request):
    estado_server = 'apagado'
    estado_mc = 'apagado'
    file_server = open(os.path.join(settings.BASE_DIR, 'static/status/server.txt')).read()
    file_mc = open(os.path.join(settings.BASE_DIR, 'static/status/mc.txt')).read()
    if 'encendido' in file_server:
        estado_server = 'encendido'
    if 'encendido' in file_mc:
        estado_mc = 'encendido'
    return render(request, 'monitor/index.html', {'estado_mc': estado_mc, 
                                                  'estado_server': estado_server, 
                                                  })

@login_required
def encender(request):
    script = os.path.join(settings.BASE_DIR, 'static/scripts/wakeonlan.sh')    
    output = subprocess.call([script], shell = True)
    print(output)
    if request.method == 'GET':
                print('encender')
    response = 'ok'
    return HttpResponse(response)

@login_required
def encender_minecraft(request):
    script = os.path.join(settings.BASE_DIR, 'static/scripts/runmcserver.sh')    
    output = subprocess.call([script], shell = True)
    print(output)
    if request.method == 'GET':
                print('encender_minecraft')
    response = 'ok'
    return HttpResponse(response)