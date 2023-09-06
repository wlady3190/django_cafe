from typing import Any, List, Optional, Tuple, Union
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Social
# Register your models here.

class socialAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    
    # COnfigurtación para grupo de personlas
    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name = 'Personal').exists():
            return('created','updated', 'key', 'name')
        else:
            return ('created', 'updated',)


admin.site.register(Social, socialAdmin)