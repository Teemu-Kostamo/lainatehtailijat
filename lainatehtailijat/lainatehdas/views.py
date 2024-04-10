from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from .models import Item
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
        return redirect('/main')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request, 'lainatehdas/register.html', {'form': form})

@login_required(login_url="/login")
def main(request):
    items_list = Item.objects.order_by("item_name")
    context = {'items_list' : items_list}
    return render(request, 'lainatehdas/main.html', context)

@login_required(login_url="/login")
def detail(request, item_id):
    item = get_object_or_404(Item, pk = item_id)
    return render(request, 'lainatehdas/detail.html', {'item' : item})