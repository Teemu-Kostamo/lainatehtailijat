from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserLoginForm
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

app_name = 'lainatehdas'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='lainatehdas/login.html',authentication_form=UserLoginForm, extra_context={'MEDIA_URL': settings.MEDIA_URL}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('main/', views.main, name='main'),
    path('main/<int:item_id>/', views.detail, name='detail'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations/<int:reservation_id>/update_return_date/<int:item_id>/', views.update_return_date, name='update_return_date'),
    path('reservations/<int:item_id>/create/', views.create_new_reservation, name='create_new_reservation'),
    path('info/', views.info, name='info'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
