from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    
    formulario_contacto=FormularioContacto()
    
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            Nombre=request.POST.get("Nombre")
            Email=request.POST.get("Email")
            Contenido=request.POST.get("Contenido")

            email=EmailMessage("Mensaje desde app django",
            "Nombre del Usuario: {} Direccion {} Mensaje:\n\n {}".format(Nombre,Email,Contenido),"",["contact.fernandolozada@gmail.com"],reply_to=[Email])

            try:
                email.send()

                return redirect("/contacto/?valido")

            except:
                return redirect("/contacto/?error")



    
    
    
    return render(request, "contacto/contacto.html", {'formulario':formulario_contacto})

