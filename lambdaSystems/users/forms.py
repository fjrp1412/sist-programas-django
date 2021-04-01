from django import forms


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

    company_name = forms.CharField(
        min_length=5,
        max_length=50,
        label=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Lambda Systems',
                'class': 'inputdata',
                'required': True
            }
        )
    )

    email_personal = forms.EmailField(
        label=False,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'lfgchang@gmail.com',
                'class': 'inputdata',
                'required': True
            }
        )
    )

    email_company = forms.EmailField(
        label=False,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'lambdasystems@gmail.com',
                'class': 'inputdata',
                'required': True
            }
        )
    )
