# accounts/urls.py

from django.urls import path
from .views import SignUpView, login_view, dashboard_view, HomeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', HomeView.as_view(), name='home'),  # Home page URL
]
