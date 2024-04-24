from django import forms



class formularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.EmailField(label="Correo Electrónico", required=True)
    telefono=forms.CharField(label="Numero de Teléfono", required=True)
    sujeto=forms.CharField(label="Sujeto", required=True)    
    contenido=forms.CharField(label="Contenido", required=True, widget=forms.Textarea)