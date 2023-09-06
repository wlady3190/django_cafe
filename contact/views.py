from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contact (request):
    print(request.method)
    contact_form = ContactForm()
    if request.method =='POST':
        contact_form=ContactForm(data = request.POST)
        
        
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            message = request.POST.get('message','')
            emailContact = EmailMessage(
                'La cafettiera: Nuevo mensaje de contacto', #Asunto
                f'De {name} <{email}>\n\nMensaje:\n\n{message}', #cuerpo
                'wtierra@itsqmet.edu.ec', #email_origen
                ['correo-prueba@inbox.mailtrap.io'],#email_destino,
                reply_to=[email] # a donde responder
            )
            
            try:
                emailContact.send()
                return redirect(reverse('contact')+'?ok')
            except Exception:
                return redirect(reverse('contact')+'?fail')
                
            
            
        
    return render(request, 'contact/contact.html', {'contactForm': contact_form})


