
from .models import Social
def context(request):
    dict = {'context_key':'Hola Cuarto Sistemas'}
    listSocial = Social.objects.all()
    for social in listSocial:
        dict[social.key]=social.url
    return dict