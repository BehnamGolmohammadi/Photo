from django.shortcuts import render, redirect
from django.contrib.auth import authenticate as auth , login, logout
from django.contrib import messages
from accounts.froms import SignupForm
# Create your views here.

# Function to validate the password
def password_check(request, passwd, passwd2):
      
    SpecialSym =['$', '@', '#', '%', '.', '*']
    val = True
      
    if len(passwd) < 6:
        messages.add_message(request, 30, 'length should be at least 6')
        val = False
          
    if len(passwd) > 20:
        messages.add_message(request, 30, 'length should be not be greater than 20')
        val = False
          
    if passwd != passwd2:
        messages.add_message(request, 30, 'Passwords do not match with each other')
        val = False
        
    if not any(char.isdigit() for char in passwd):
        messages.add_message(request, 30, 'Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in passwd):
        messages.add_message(request, 30, 'Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in passwd):
        messages.add_message(request, 30, 'Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        messages.add_message(request, 30, 'Password should have at least one of the symbols [$ @ # % . *]')
        val = False
    if val:
        return val

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
            if not (password_check(request, pass1, pass2)):
                if Next :
                    return redirect(f"/accounts/signup?next={Next}")
                else:
                    return redirect('/accounts/signup')
            elif pass1 == pass2:
                # create new user without password so dont save now.
                user = Form.save(commit = False)
                # set password so now all fields are completed
                user.set_password(pass1)
                # now we can save new user
                user.save()
                login(request, user)
                msg= f'Welcome {request.user.get_full_name()}, You\'ve been signed up successfully.'
                messages.success(request, msg)
                if Next:
                    return redirect(Next)
                else:
                    return redirect('/')
            else:
                msg= f'Dear visitor, fields are not filled correctly'
                messages.warning(request, msg)
                if Next :
                    return redirect(f"/accounts/signup?next={Next}")
                else:
                    return redirect('/accounts/signup')
        else:
            msg= 'Dear visitor your entired information are not valid! check this cases:'
            error1 = '1. Maybe your email or username is submitted before. try to login with the button below if you are a member.'
            error2 = '2. Maybe your username and password are similar. try to use another password.'
            error3 = '3. Maybe your password is common password. try to use a specific password.'
            messages.add_message(request, 40, msg)
            messages.add_message(request, 30, error1)
            messages.add_message(request, 30, error2)
            messages.add_message(request, 30, error3)
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
            messages.error(request, msg)
            if request.POST['next']:
                return redirect(f"/accounts/login?next={request.POST['next']}")
            else:
                return redirect('/accounts/login')
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