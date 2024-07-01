#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .models import CustomUser



class SignUpView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def dashboard_view(request):
    if request.user.user_type == 'patient':
        return render(request, 'users/dashboard_patient.html', {'user': request.user})
    else:
        return render(request, 'users/dashboard_doctor.html', {'user': request.user})

class HomeView(TemplateView):
    template_name = 'users/home.html'