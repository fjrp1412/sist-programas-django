from django import forms
from django.contrib.auth.models import User
from users.models import Salesman


class SignupForm(forms.Form):

    username = forms.CharField(
        min_length=5,
        max_length=50,
        label=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Luis Francisco Garcia Chachati Chang',
                'class': 'inputdata',
                'required': True
            }
        )
    )

    email = forms.EmailField(
        label=False,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'lfgchang@gmail.com',
                'class': 'inputdata',
                'required': True
            }
        )
    )

    password = forms.CharField(
        min_length=8,
        max_length=150,
        label=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese su contraseña.',
                'class': 'inputdata',
                'required': True
            }
        )
    )
    confirm_password = forms.CharField(
        min_length=8,
        max_length=150,
        label=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repita su contraseña.',
                'class': 'inputdata',
                'required': True
            }
        )
    )

    identification_document = forms.CharField(
        min_length=7,
        max_length=8,
        label=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Inserte su cedula',
                'class': 'inputdata',
                'required': True
            }
        )
    )

    def save(self):
        """Create and save the new user."""
        data = self.cleaned_data
        data.pop('confirm_password')
        document = data.pop('identification_document')
        user = User.objects.create_user(**data)
        salesman = Salesman(user=user, identification_document=document)
        salesman.save()

    def clean(self):
        """Verify password confirmation"""
        data = super().clean()
        password = data['password']
        confirm_password = data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

        return data
