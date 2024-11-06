from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.view import View
# import the user class model
from django.contrib.auth.models import User

# import the registerform from forms.py
from .forms import RegisterForm


def register_view(request):
    # request form is post or not
    if request.method == "POST":
        form = RegisterForm(request.form)
        if form.is_valid():
            username = form.clearned_data.get("username")
            password = form.cleaned_data.get("password")
            User.objects.create_user(username = username, password = password)
            login(request, user)
            return redirect('home')
        else:
            form = RegisterForm()
            return render(request, 'accounts/register.html', {'forms':form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            request.POST.get('next') or request.GET.get('next') or home_view
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials"
    return render(request, 'accounts/login.html', {'error':error_message})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')


# home view
# usng the decorator
@login_required
def home_view(request):
    return render(request, 'home/home.html')

# protected view
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    # next to redirect url
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'registration/protected.html')




# Create your views here.


