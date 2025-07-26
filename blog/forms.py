from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from blog.models import Perfil, Comentario


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    edad = forms.IntegerField(label='Edad', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'edad', 'password1', 'password2')


class EditarPerfilFormulario(UserChangeForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="Nombre de usuario")
    
    # Campos extra de Perfil
    edad = forms.IntegerField(label="Edad", required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        self.perfil = kwargs.pop('perfil', None)
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)  # ocultamos el campo contraseña
        if self.perfil:
            self.fields['edad'].initial = self.perfil.edad

    def save(self, commit=True):
        user = super().save(commit)
        if self.perfil:
            self.perfil.edad = self.cleaned_data.get('edad')
            if commit:
                self.perfil.save()
        return user


class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar']


class BiografiaFormulario(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['biografia']
        widgets = {
            'biografia': forms.Textarea(attrs={
                'placeholder': 'Escribe tu biografía acá...',
                'rows': 4,
                'class': 'form-control'
            }),
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Escribí un comentario...',
                'class': 'form-control'
            }),
        }
