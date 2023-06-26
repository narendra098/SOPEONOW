from django.forms import ModelForm
from . models import Item
from django import forms

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'cost':forms.NumberInput(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
            'quantity_sold':forms.NumberInput(attrs={'class':'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class':'form-control'}),

        }

    def clean(self):
        cleaned_data = super().clean()
        cost_price = cleaned_data.get('cost')
        selling_price = cleaned_data.get('selling_price')

        if cost_price and selling_price and selling_price <= cost_price:
            raise forms.ValidationError("Selling price must be greater than the cost price.")

        return cleaned_data



