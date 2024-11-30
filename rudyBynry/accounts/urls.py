

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
]