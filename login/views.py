from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import loginForm
from django.contrib.auth import authenticate, login, logout

def login_user(request):
   if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'username atau password salah. Silakan coba lagi.')
                return render(request, 'login.html', {'form': form})
        else:
            messages.error(request, 'Form tidak valid')
            return render(request, 'login.html', {'form': form})
   else:
      form = loginForm()
      return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')
