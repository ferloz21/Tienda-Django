from django import forms

class FormularioContacto(forms.Form):
    
    Nombre=forms.CharField(label="Nombre", required=True)
    Email=forms.CharField(label="Email", required=True)
    Contenido=forms.CharField(label="Contenido", widget=forms.Textarea)
    
    
   