from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", max_length=50, required=True)
    email=forms.CharField(label="Email", max_length=50, required=True)
    contacto=forms.CharField(label="Contacto", widget=forms.Textarea)

