from django.shortcuts import render
from .models import Service

# Create your views here.

def services (request):
    services = Service.objects.all() # Consulta d eregistro de servicios
    return render(request, 'services/services.html', {'list_services':services})