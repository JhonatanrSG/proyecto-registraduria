from django import forms
from django.contrib.auth.models import User
from .models import Ciudadano

# Formulario para crear un usuario (UserForm)
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Encriptar la contraseña antes de guardar
        if commit:
            user.save()
        return user

# Formulario para crear o actualizar el perfil de Ciudadano
class CiudadanoForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_expedicion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(max_length=100, required=True)  # Hacer obligatorio el email
    photo = forms.ImageField(required=False)  # Si el campo 'photo' es opcional, lo marcamos como no requerido

    class Meta:
        model = Ciudadano
        fields = [
            'photo', 'nombres', 'apellidos', 'identificacion', 'fecha_nacimiento',
            'lugar_nacimiento', 'fecha_expedicion', 'lugar_expedicion', 'rh',
            'grupo_sanguineo', 'estatura', 'email'
        ]  # Asegúrate de que todos los campos estén correctamente listados aquí
