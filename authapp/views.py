from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method== "POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is not matching")
            return redirect('/auth/signup/')
            
            
        
        try:
            if User.objects.get(username=email):
                messages.info(request,'Email is already registered')
                return render(request,'signup.html')
                

                
                
        except Exception as identifier:
            pass

        user = User.objects.create_user(email,email,password)
        user.save()
        messages.success(request,"User Created  Successfully")
        return redirect('/auth/login')
    return render(request,'signup.html')


def handlelogin(request):
    if request.method=="POST":
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Successfully Login")
            return redirect('/')
        
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/auth/login')

    return render(request,'login.html')


def handlelogout(request):
    logout(request)
    messages.info(request,"Successfully Logout")
    return redirect('/auth/login')


