from django.urls import path
from .views import home, register, login, inventory, product

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('inventory/', inventory, name='inventory'),
    path('product/', product, name='product'),
]