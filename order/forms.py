from django import forms
from .models import Order
from django.core.validators import RegexValidator


class OrderCreateForm(forms.ModelForm):
    email = forms.EmailField(label='Электронная почта', error_messages={'invalid': 'Введите корректный адрес электронной почты'})
    phone_number = forms.CharField(label='Номер телефона', validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Номер телефона должен быть в формате: '+7999999999'.")])

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'city', 'street', 'house', 'flat', 'email', 'phone_number']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'city': 'Город',
            'street': 'Улица',
            'house': 'Дом',
            'flat': 'Квартира',
            'email': 'Электронная почта',
            'phone_number': 'Номер телефона',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={"class":"form"}),
            'last_name': forms.TextInput(attrs={"class":"form"}),
            'city': forms.TextInput(attrs={"class": "form"}),
            'street': forms.TextInput(attrs={"class": "form"}),
            'house': forms.TextInput(attrs={"class": "form"}),
            'flat': forms.TextInput(attrs={"class": "form"}),
            'email': forms.EmailInput(attrs={"class":"form"}),
            'phone_number': forms.TextInput(attrs={"class":"form"}),
        }