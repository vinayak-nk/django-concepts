from dataclasses import fields
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = [
      'title',
      'description',
      'price',
    ]
    
class RawProductForm(forms.Form):
  title = forms.CharField(required=True, label='my title')
  description = forms.CharField(
    required=False,
    widget=forms.Textarea(
      attrs={
        'placeholder': 'Your description',
        'class': 'clas_name',
        'id': 'some_id',
        "row": 5,
        "cols": 50,
      }
    )
  )
  price = forms.DecimalField(initial=100)
  