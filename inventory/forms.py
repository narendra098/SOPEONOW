from django.forms import ModelForm
from orders.models import received_order
from .models import Item
from django import forms
from django.core.exceptions import ValidationError

class CreateNewItemForm(ModelForm):
    class Meta:
        model = received_order
        fields = ['item_name', 'item_cost', 'item_quantity', 'item_selling_price', 'item_stock_alert']

        widgets = {
            'item_name':forms.TextInput(attrs={'class':'form-control'}),
            'item_cost':forms.NumberInput(attrs={'class':'form-control'}),
            'item_quantity':forms.NumberInput(attrs={'class':'form-control'}),
            'item_selling_price': forms.NumberInput(attrs={'class':'form-control'}),
            'item_stock_alert':forms.NumberInput(attrs={'class':'form-control'}),

        }

    def clean(self):
        cleaned_data = super().clean()
        cost_price = cleaned_data.get('item_cost')
        selling_price = cleaned_data.get('item_selling_price')

        if selling_price <= cost_price:
            raise forms.ValidationError("Selling price must be greater than the cost price.")

        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.order_type = 'buy'  # Set the default value for order_type
        if commit:
            instance.save()
        return instance   


class EditItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'item_name':forms.TextInput(attrs={'class':'form-control'}),
            'item_cost':forms.NumberInput(attrs={'class':'form-control'}),
            'item_quantity_left':forms.NumberInput(attrs={'class':'form-control'}),
            'item_selling_price': forms.NumberInput(attrs={'class':'form-control'}),

        }

    def clean(self):
        cleaned_data = super().clean()
        
        cost_price = cleaned_data.get('item_cost')
        selling_price = cleaned_data.get('item_selling_price')
        
        if selling_price <= cost_price:
            raise ValidationError("Selling price must be greater than the cost price.")

        return cleaned_data

class OrderItemForm(ModelForm):
    order_item_quantity = forms.IntegerField(label='Quantity Ordering')
    class Meta:
        model = Item
        fields = ['item_id','item_name', 'order_item_quantity']
        widgets = {
            'item_id':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'item_name':forms.TextInput(attrs={'class':'form-control','readonly':'readonly' }),
            'order_item_quantity':forms.NumberInput(attrs={'class':'form-control'}),
        } 

class SellItemForm(ModelForm):
    item_quantity_selling = forms.IntegerField(label='Quantity Selling')
    class Meta:
        model = Item
        fields = ['item_id','item_name', 'item_quantity_left', 'item_quantity_selling']
        widgets = {
            'item_id':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'item_name':forms.TextInput(attrs={'class':'form-control','readonly':'readonly' }),
            'item_quantity_left':forms.NumberInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'item_quantity_selling':forms.NumberInput(attrs={'class':'form-control'}),
        } 

    def clean(self):
        cleaned_data = super().clean()
        item_id = cleaned_data.get('item_id')
        item_quantity_left = cleaned_data.get('item_quantity_left')
        item_quantity_selling = cleaned_data.get('item_quantity_selling')
        
        if item_quantity_selling > item_quantity_left:
                
            raise ValidationError("Quantity selling cannot be greater than available quantity.")
    

        return cleaned_data





 
    


    
 
    







