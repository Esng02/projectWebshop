from .models import ProductList
from django.forms import ModelForm, TextInput, Textarea, DateInput


class ProductListForm(ModelForm):
    class Meta:
        model = ProductList
        fields = ['title', 'description', 'date', 'author']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название записи'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата добавления'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя автора'
            })
        }
