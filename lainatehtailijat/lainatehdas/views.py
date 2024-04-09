from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from .models import Item
from django.http import Http404, HttpResponse

# Create your views here.
def index(request): #Vaihda tämä pääsivuksi
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

def main(request):
    items_list = Item.objects.order_by("item_name")
    context = {'items_list' : items_list}
    return render(request, 'lainatehdas/main.html', context)

def detail(request, item_id):
    item = get_object_or_404(Item, pk = item_id)
    return render(request, 'lainatehdas/detail.html', {'item' : item})