from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import userform 
from .models import Myuser

def adminview(request):
    return render('admin/base.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('dashboard')
    else:
        return render(request, 'registration/login.html')

def register(request):
    if request.method == 'POST':
     # Get form values
        username = request.POST['username']
        phone = request.POST['phone']
        department = request.POST['department']
        age = request.POST['age']
        address  = request.POST['address']
        email = request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']

        # Check if passwords match
        if psw == psw_repeat:
        # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('registation/register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('registration/register')
                else:
                
                    user = User.objects.create_user(username=username, password=psw,email=email, age=age, address=address, phone = phone, department= department)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
                messages.error(request, 'Passwords do not match')
                return redirect('registration/register.html')
    else:
        return render(request, 'registration/login.html')

def dashboard(request):
    return render(request, 'registration/dashboard.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

def viewalluser(request):  
    myusers = Myuser.objects.all()  
    return render(request,"admin/viewalluser.html",{'myusers':myusers})  
def edituser(request, username):  
    myuser = Myuser.objects.get(username=username)  
    return render(request,'edituser.html', {'myuser':myuser})  
def deleteuser(request, username):  
    myuser = Myuser.objects.get(username=username)  
    myuser.delete()  
    return redirect("/viewalluser")

def update(request, username):  
    myuser = Myuser.objects.get(username=username)  
    form = userform(request.POST, instance = Myuser)  
    if form.is_valid():  
        form.save()  
        return redirect("/viewalluser")  
    return render(request, 'edituser.html', {'myuser': myuser})  

def adduser(request):  
    if request.method == "POST":  
        form = userform(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/admin/viewalluser')  
            except:  
                pass  
    else:  
        form = userform()  
    return render(request,'admin/adduser.html',{'form':form})  
