from django.shortcuts import redirect, render
from .models import Product, alert, RegistrationWeight, Inventory, Sales, Report, Role
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home/index.html', {'products':products})

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email = request.POST['email']
        username=email.split('@')[0] 
        password = request.POST['pass']
        user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        
        if user is not None:
            return redirect('login')
        else:
            messages={
                'error':'Datos invalidos'
            }
            return render(request,'register/index.html',messages)
        
    return render(request,'register/index.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass']
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home') 
        else:
            messages={
                'error':'Credenciales invalidas'
            }
            return render(request,'login/index.html',messages)   
        
    return render(request,'login/index.html') 

def logoutValidation(request):
    logout(request)
    return redirect('login')

def inventory(request):
    return render(request, 'inventory/index.html')

def product(request, id):
    product = Product.objects.get(id=id)
    return render(request,'product/index.html',{'product':product})