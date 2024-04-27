from django.contrib import admin
from .models import Item, Reservation
from django.utils import timezone

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'item_name','reserved_date', 'returned_date', 'is_due')
    list_filter = ('date_returned',)
    # Nämä funktiot annettu chatgpt:n tehtäväksi
    def reserved_date(self, obj):
        return obj.date_reserved
    reserved_date.short_description = 'Varauspäivä'

    def returned_date(self, obj):
        return obj.date_returned
    returned_date.short_description = 'Palautuspäivä'

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'Käyttäjä'

    def item_name(self, obj):
        return obj.item.item_name
    item_name.short_description = 'Väline'

    def is_due(self, obj):
        return obj.date_returned is None and obj.date_deadline < timezone.now().date()
    #Tähän asti
    is_due.boolean = True
    is_due.short_description = 'Myöhässä'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.item.item_avail = "Vr"
            obj.item.save()
        else:
            if obj.date_returned is None:
                obj.item.item_avail = "Vr"
            else:
                obj.item.item_avail = "Va"
            obj.item.save()
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.item.item_avail = "Va"
        obj.item.save()
        super().delete_model(request, obj)

admin.site.register(Item)
admin.site.register(Reservation, ReservationAdmin)
