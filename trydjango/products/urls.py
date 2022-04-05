from django.urls import path

from . import views
urlpatterns = [
  path('', views.product_detail_view),
  path('create/', views.render_initial_data)
]