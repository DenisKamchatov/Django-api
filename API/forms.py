from dataclasses import fields
from .models import Products, Partners
from django.forms import DateTimeInput, ModelForm, NumberInput, TextInput, Textarea

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name','company','compound','amount','delivery','price']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название продукта'
            }),
             'company': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Производитель'
            }),
                'compound': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Состав'
            }),
                'amount': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество'
            }),
               'delivery': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Доставят к'
            }),
                'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
        }


class PartnersForm(ModelForm):
    class Meta:
        model = Partners
        fields = ['organization','link','reviews']

        widgets = {
            'organization': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название компании'
            }),
             'link': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на страницу'
            }),
                'reviews': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оценка'
            })
        }