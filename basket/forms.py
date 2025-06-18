from django import forms

class AddBasketForm(forms.Form):
    quantity = forms.IntegerField(initial=1, label="Количество", min_value=1, max_value=10, widget=forms.HiddenInput)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)