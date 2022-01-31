from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Author, Book

class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(request=request, *args, **kwargs)
        

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'name' : 'Nombres',
            'last_name' : 'Apellidos',
            'country' : 'País',
            'image' : 'Foto',
            'biography' : 'Biografia'
        }
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingresa el nombre del Autor'
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder':'Ingrese los apellidos del Autor'
                }
            ),
            'country' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el pais de origen del Autor'
                }
            ),
            'image' : forms.FileInput(
                attrs={
                    'class' : 'form-control',
                }
            ),
            'biography' : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese la biografia del Autor'
                }
            )
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': 'Titulo',
            'date_published': 'Fecha de Publicación',
            'image': 'Portada',
            'author_id': 'Autores'
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa aqui el titulo'
                }
            ),
            'date_published': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'author_id': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }
