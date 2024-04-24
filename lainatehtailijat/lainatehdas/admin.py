from django.contrib import admin
from .models import Item, Reservation

class ReservationAdmin(admin.ModelAdmin):
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
