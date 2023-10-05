from .models import Users
from django.forms import ModelForm, TextInput, PasswordInput, NumberInput, RadioSelect


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'password', 'phone', 'role']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'name'
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }),
            'phone': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'phone number'
            }),
            'role': RadioSelect()
        }
