from django.shortcuts import render, redirect
from django.contrib.auth import authenticate as auth , login, logout
from django.contrib import messages
from accounts.froms import SignupForm
# Create your views here.
def accounts_signup(request):
    if request.user.is_authenticated:
        msg= f'{request.user.first_name}, you have been logged in as {request.user.username}.'
        messages.success(request, msg)
        return redirect('/')
    elif request.method == 'POST':
        Form = SignupForm(request.POST)
        Next = request.POST.get('next')
        if Form.is_valid():
            pass1 = Form.cleaned_data.get('password')
            pass2 = request.POST['password2']
            if pass1 == pass2:
                user= Form.save()
                login(request, user)
                msg= f'Welcome {request.user.get_full_name()}, You\'ve been signed up successfully.'
                messages.success(request, msg)
                if Next:
                    return redirect(Next)
                else:
                    return redirect('/')
            else:
                msg= f'Dear visitor your entired passwords do not match or other fields are not filled correctly'
                messages.warning(request, msg)
                if Next :
                    return redirect(f"/accounts/signup?next={Next}")
                else:
                    return redirect('/accounts/signup')
        else:
            msg= f'Dear visitor your entired information are not valid! Maybe your email is submitted before.'
            messages.warning(request, msg)
            if Next:
                return redirect(f"/accounts/signup?next={Next}")
            else:
                return redirect('/accounts/signup')
    else:
        Form = SignupForm()
        return render(request, 'registration/signup.html', {'Form': Form})

def accounts_login(request):
    if request.user.is_authenticated:
        msg= f'{request.user.first_name}, you have been logged in as {request.user.username}.'
        messages.success(request, msg)
        return redirect('/')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth(request, username = username, password = password)
        if user is not None:
            login(request, user)
            msg= f'Hi {request.user.get_full_name()}, You\'ve been logged in successfully.'
            messages.success(request, msg)
            return redirect(request.POST['next'])
        else:
            msg= f'Username or password or both are not correct'
            messages.success(request, msg)
            return redirect(request.POST['next'])
    else:
        return render(request, 'registration/login.html')

def accounts_logout(request):
    if request.user.is_authenticated:
        msg= f'Bye {request.user.get_full_name()}, You logged out successfully.'
        logout(request)
        messages.info(request, msg)
        return redirect('/')
    else:
        msg= f'Dear visitor, you\'re not logged in yet, if you want you can login or singup.'
        messages.warning(request, msg)
        return render(request, 'registration/login.html')