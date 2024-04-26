from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from .models import Item, Reservation
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse_lazy
from datetime import date, timedelta
from django.conf import settings
from django.contrib import messages
import json

# Create your views here.
def index(request):
        return redirect('/info')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/info')
    else:
        form = UserRegisterForm()
    return render(request, 'lainatehdas/register.html', {'form': form, 'MEDIA_URL': settings.MEDIA_URL})

@login_required
def info(request):
        context = {
             'MEDIA_URL' : settings.MEDIA_URL
        }
        return render(request, 'lainatehdas/info.html', context)

@login_required
def main(request):
    items_list = Item.objects.order_by("item_name")
    reservation_list = Reservation.objects.all()

    msg_list = []
    for message in messages.get_messages(request):
        msg_list.append({
            "message": message.message,
            "tags": message.tags
        })

    context = {
        'items_list' : items_list, 
        'reservation_list' : reservation_list, 
        'MEDIA_URL' : settings.MEDIA_URL,
        'messages_json': json.dumps(msg_list)
    }
    return render(request, 'lainatehdas/main.html', context)

@login_required
def detail(request, item_id):
    item = get_object_or_404(Item, pk = item_id)

    if item.item_avail == "Vr":
        reservation = get_object_or_404(Reservation, date_returned__isnull=True, item__id=item_id)
        delta = reservation.date_deadline - date.today()
        reservation.days_until_deadline = delta.days
        if delta >= timedelta(days=0):
            reservation.return_ontime = True
        else:
            reservation.return_ontime = False
            reservation.days_until_deadline = abs(reservation.days_until_deadline)
    else:
        reservation = ""

    msg_list = []
    for message in messages.get_messages(request):
        msg_list.append({
            "message": message.message,
            "tags": message.tags
        })
             
    context = {
        'item' : item, 
        'reservation' : reservation,
        'MEDIA_URL' : settings.MEDIA_URL,
        'messages_json': json.dumps(msg_list)
    }
    return render(request, 'lainatehdas/detail.html', context)

@login_required
def reservations(request):
    user_id = request.user.id
    active_reservations = Reservation.objects.filter(user_id=user_id, date_returned__isnull=True)
    old_reservations = Reservation.objects.filter(user_id=user_id).exclude(date_returned__isnull=True)
    for reservation in active_reservations:
        delta = reservation.date_deadline - date.today()
        if delta >= timedelta(days=0):
            reservation.days_until_deadline = delta.days
            reservation.return_ontime = True
        else:
            reservation.return_ontime = False
            reservation.days_until_deadline = abs(delta.days)

    msg_list = []
    for message in messages.get_messages(request):
        msg_list.append({
            "message": message.message,
            "tags": message.tags
        })
    
    context = {
        'active_reservations': active_reservations,
        'old_reservations': old_reservations,
        'MEDIA_URL' : settings.MEDIA_URL,
        'messages_json': json.dumps(msg_list)
    }
    
    return render(request, 'lainatehdas/reservations.html', context)

@login_required
def create_new_reservation(request, item_id):
    user = request.user.id
    Reservation.objects.create(user_id = user, item_id = item_id, date_reserved = date.today())
    item = get_object_or_404(Item, id=item_id)
    item.item_avail = "Vr"
    item.save()
    message_text = f'{Item.objects.get(id=item_id)} on varattu onnistuneesti!'
    message_tag = 'normal'
    messages.add_message(request, messages.INFO, message_text, extra_tags=message_tag)
    
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@login_required
def update_return_date(request, reservation_id, item_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.date_returned = date.today()
    reservation.save()
    item = get_object_or_404(Item, id=item_id)
    item.item_avail = "Va"
    reservation.reservation_complete = True
    item.save()
    delta = reservation.date_returned - reservation.date_deadline
    if delta.days <= 0:
        message_text = f'Palautus onnistui. {item} palautettu ajallaan!'
        message_tag = 'normal'
    else:
        message_text = f'Palautus onnistui. {item} palautettu {delta.days} vuorokautta myöhässä!'
        message_tag  = 'late'
    messages.add_message(request, messages.INFO, message_text, extra_tags=message_tag)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


