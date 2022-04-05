from multiprocessing import context
from django.shortcuts import render

from .models import Product
from .forms import ProductForm
# Create your views here.

def product_create_view(request):
  form = ProductForm(request.POST or None)
  if form.is_valid():
    form.save()
  
  context = {
    'form': form
  }
  return render(request, 'products/create.html', context)

def product_detail_view(request):
  obj = Product.objects.get(id=1)
  context = {
    'object': obj
  }

  return render(request, 'products/detail.html', context)