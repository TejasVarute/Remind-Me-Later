from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import UserData

def login(request):
    if request.method == "POST":
        if request.POST['form_type'] == "register":
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            
            if UserData.objects.filter(username = username).exists() or UserData.objects.filter(email = email).exists():
                return redirect('login:login')
            
            hashed_password = make_password(password)
            UserData(username = username, email=email, password = hashed_password).save()
            return redirect('login:login')
                            
        elif request.POST['form_type'] == "login":
            username = request.POST['username']
            password = request.POST['password']
        
        try:
            user = UserData.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return redirect('reminder:my_reminder')
        except: 
            return render(request, 'login.html', context = {"message" : "False Information"})
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('login:login')