from django.shortcuts import render
from django.contrib import messages, auth

from django.contrib.auth.models import User
from django.core.mail import message
from django.shortcuts import render, redirect,HttpResponse


# Create your views here.
def login(request):
    if request.method=='POST':
        usernam=request.POST['username']
        passwor= request.POST['password']
        user=auth.authenticate(username=usernam,password=passwor)
        if user is not None:
            auth.login(request,user)
            return render(request,'inde.html')

        else:
            messages.info(request,"invalid credential")
            return redirect("credential:login")
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('credential:register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,'email taken')
            #     return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('credential:login')
                print("user registered")
        else:
            messages.info(request,"password not matching")
            return redirect('credential:register')
        return render(request,'inde.html')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def forms(request):
     # if request.method == 'POST':
     #    name = request.POST.get('name', )
     #    desc = request.POST.get('desc', )
     #    year = request.POST.get('year', )
     #
     #    movie = Movie(name=name, desc=desc, year=year, img=imag)
     #    movie.save()
     #    return redirect('/')
    return render(request, 'forms.html')
def submit(request):
    return render (request,'submit.html')