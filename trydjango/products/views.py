from django.shortcuts import render

from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.


def render_initial_data(request):
  initial_data = {
    "title": "Some title"
  }
  obj = Product.objects.get(id=1)
  # my_form = ProductForm(request.POST or None, initial=initial_data)
  my_form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
  if my_form.is_valid():
    my_form.save()
  context = {
    'form': my_form
  }
  return render(request, 'products/create.html', context)
  
  
def product_create_view(request):
  my_form = RawProductForm()
  if request.method == 'POST':
    my_form = RawProductForm(request.POST)
    if my_form.is_valid():
      Product.objects.create(**my_form.cleaned_data)
  context = {
    'form': my_form
  }
  return render(request, 'products/create.html', context)

# def product_create_view(request):
#   form = ProductForm(request.POST or None)
#   if form.is_valid():
#     form.save()
#     form = ProductForm()
  
#   context = {
#     'form': form
#   }
#   return render(request, 'products/create.html', context)

def product_detail_view(request):
  obj = Product.objects.get(id=1)
  context = {
    'object': obj
  }

  return render(request, 'products/detail.html', context)