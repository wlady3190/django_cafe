from django.contrib import admin
from .models import Page
# Register your models here.

class PageModel(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Page, PageModel)