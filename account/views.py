from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib import messages



def user_login(request):
    if request.user.is_authenticated:
        return redirect("pages_menu") 

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("pages_menu") 
        else:
            return render(request, "account/login.html", {"error":"username ya da password hatalı"})
    else:
        return render(request, "account/login.html", {"nav_request": True})


def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", {"error": "kullanıcı adı alınmış"})
            else:
                if User.objects.filter(email = email).exists():
                    return render(request, "account/register.html", {"error": "email kullanılmakta"})
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect("pages_menu")
        else:
            return render(request, "account/register.html", {"error": "parolalar birbirine uymamaktadır"})

    else:
        return render(request, "account/register.html", {"nav_request": True})



def user_logout(request):
    logout(request)
    return redirect("pages_menu")