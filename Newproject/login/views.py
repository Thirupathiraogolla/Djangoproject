
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import register

def display(request):
    if request.method == 'POST':
        a = request.POST
        name = a['name']
        email = a['email']
        num = a['num']
        password = a['password']
        password1 = a['password1']
        
        if password1 != password:
            return redirect('index')  # URL pattern name 'index' should be defined
        
        obj = register(name=name, email=email, phone=num, password=make_password(password))
        obj.save()
        return redirect('login')  # URL pattern name 'new' should be defined

    return render(request, 'login/register.html')

def index(request):
    return HttpResponse('<h1>Both passwords are not the same</h1>')

def new(request):
    if request.method == 'POST':
        email1 = request.POST['email']
        if register.objects.filter(email=email1).exists():
            return redirect('select')
        else:
            return HttpResponse('Email not found')
    
    return render(request, 'login/login.html')

def select(request):
    registers = register.objects.all()
    context={
        'register':registers,
    }
    return render(request,'login/select.html',context)