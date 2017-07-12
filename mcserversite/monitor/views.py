from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def index(request):
    estado = 'apagado'
    return render(request, 'monitor/index.html', {'estado': estado})

def encender(request):    
    if request.method == 'GET':
                print('encender')
    response = 'ok'
    return HttpResponse(response)