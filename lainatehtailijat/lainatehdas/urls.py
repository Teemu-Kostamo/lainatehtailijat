from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserLoginForm
from django.conf.urls.static import static
from django.conf import settings
app_name = 'lainatehdas'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='lainatehdas/login.html',authentication_form=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('main/', views.main, name='main'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations/<int:reservation_id>/update_return_date/', views.update_return_date, name='update_return_date'),
    path('reservations/<int:item_id>/create/', views.create_new_reservation, name='create_new_reservation'),
    path('main/<int:item_id>/', views.detail, name='detail')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
