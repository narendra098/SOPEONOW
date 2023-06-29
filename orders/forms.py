from django.forms import ModelForm
from inventory.models import Item
from django import forms

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

        widgets = {
            'item_name':forms.TextInput(attrs={'class':'form-control'}),
            'item_cost':forms.NumberInput(attrs={'class':'form-control'}),
            'item_quantity':forms.NumberInput(attrs={'class':'form-control'}),
            'item_selling_price': forms.NumberInput(attrs={'class':'form-control'}),

        }

   



