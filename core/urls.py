from django.urls import path, include

from . import views
# from .views import about, blog, contact, home, services, store, sample



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('services/', views.services, name='services'),
    path('store/', views.store, name='store'),
    # path('contact/', views.contact, name='contact'),


    
]

#configuración extenbdida de URL, PARA CARGAR ESTATICOS, e imagenes mediante un path, 