from django.urls import path
from .views import home, register, login, inventory, product, logoutValidation

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('login/', logoutValidation, name='logout'),
    path('inventory/', inventory, name='inventory'),
    path('product/', product, name='product'),
]