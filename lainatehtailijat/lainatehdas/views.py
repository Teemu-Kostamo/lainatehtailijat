from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from .models import Item, Reservation
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse_lazy
from datetime import date

# Create your views here.
def index(request):
        return redirect('/main')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/main')
    else:
        form = UserRegisterForm()
    return render(request, 'lainatehdas/register.html', {'form': form})

@login_required
def main(request):
    items_list = Item.objects.order_by("item_name")
    reservation_list = Reservation.objects.all()
    context = {'items_list' : items_list, 'reservation_list' : reservation_list}
    return render(request, 'lainatehdas/main.html', context)

@login_required
def detail(request, item_id):
    item = get_object_or_404(Item, pk = item_id)
    reservation_list = Reservation.objects.all()
    context = {'item' : item, 'reservation_list' : reservation_list}
    return render(request, 'lainatehdas/detail.html', context)

@login_required
def reservations(request):
    user_id = request.user.id
    active_reservations = Reservation.objects.filter(user_id=user_id, date_returned__isnull=True)
    old_reservations = Reservation.objects.filter(user_id=user_id).exclude(date_returned__isnull=True)
    
    context = {
        'active_reservations': active_reservations,
        'old_reservations': old_reservations,
    }
    
    return render(request, 'lainatehdas/reservations.html', context)

@login_required
def create_new_reservation(request, item_id):
    user = request.user.id
    Reservation.objects.create(user_id = user, item_id = item_id, date_reserved = date.today())
    item = get_object_or_404(Item, id=item_id)
    item.item_avail = "Vr"
    item.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@login_required
def update_return_date(request, reservation_id, item_id):
    reservation = Reservation.objects.get(id=reservation_id)
    reservation.date_returned = date.today()
    reservation.save()
    item = get_object_or_404(Item, id=item_id)
    item.item_avail = "Va"
    reservation.reservation_complete = True
    item.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


