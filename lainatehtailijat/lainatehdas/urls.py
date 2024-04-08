from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserLoginForm
app_name = 'lainatehdas'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='lainatehdas/login.html',authentication_form=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
