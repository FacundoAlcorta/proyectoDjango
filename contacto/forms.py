from django import forms

class formularioContacto(forms.Form):
    nombre = forms.CharField(label="nombre", required=True, max_length=30)
    email = forms.CharField(label="email", required=True, max_length=30)
    contenido = forms.CharField(label="contenido",widget=forms.Textarea)
    ##your_name = forms.CharField(label="tu nombre", max_length=100)
