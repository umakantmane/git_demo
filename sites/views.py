from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from sites.forms import LoginForm
from django.contrib.auth.decorators import login_required


def staticExample(request):

    return render(request, 'static_examples.html')

def signUp(request):

    form = UserCreationForm()
    if request.method == 'POST':

        form  = UserCreationForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            #user.password = form.cleaned_data['password1']
            user.save()
            request.session['message'] = 'Registration done successfully!'
            return redirect('signin')

    return render(request, 'signup.html', {'form':form, 'msg':''})


def signIn(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:

                return render(request, 'signin.html', {'form': form, 'msg': 'User Not Found!'})
            else:
                login(request, user)
                return redirect('dashboard')

    if 'message' in request.session:
        msg = request.session['message']
        del request.session['message']
        # for k in request.session.keys():
        #     del request.session[k]
        return render(request, 'signin.html', {'form': form, 'msg': msg})
    else:
        return render(request, 'signin.html', {'form':form, 'msg':''})

def logOut(request):

    logout(request)


    return redirect('signin')

@login_required(login_url='/signin')
def dashBoard(request):

    return render(request, 'dashboard.html')

