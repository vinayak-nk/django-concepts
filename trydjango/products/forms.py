from dataclasses import fields
from turtle import title
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
  title = forms.CharField(required=True)
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
  class Meta:
    model = Product
    fields = [
      'title',
      'description',
      'price',
    ]
    
  def clean_title(self):
    title = self.cleaned_data.get("title")
    if 'vinay' in title:
      return title
    else:
      raise forms.ValidationError("not a valid title")
        
    
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
  