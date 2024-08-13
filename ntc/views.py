from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# login and logout functionality
def login_view(request):
    if request.method == 'POST':
        username = request.POST['NTC_username']
        password = request.POST['NTC_password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('invoice_filter')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'main/login_form.html')

def logout_view(request):
    logout(request)
    return redirect('login')