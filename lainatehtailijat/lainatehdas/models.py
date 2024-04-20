from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date

# Create your models here.

class Item(models.Model):
    item_choices = {
       "Leik" : "Ruohonleikkuri",
       "Trim" : "Trimmeri",
       "Saha" : "Saha",
       "Lapi" : "Lapio",
       "Saks" : "Sakset",
       "Harv" : "Harava",
       "Muu" : "Muu"
    }
    item_avail_choices = {
        "Va" : "Vapaa",
        "Vr" : "Varattu",
        "Hu" : "Huollossa",
        "Ri" : "Rikki"
    }
    item_name = models.CharField(max_length= 200, verbose_name="Name")
    item_desc = models.CharField(max_length= 500, verbose_name="Description")
    item_type = models.CharField(max_length=4, choices=item_choices, verbose_name="Type")
    item_avail = models.CharField(max_length=2, choices=item_avail_choices, default="Va")
    item_img = models.ImageField(upload_to='media/', default='media/placeholder.jpg')
    def __str__(self) -> str:
        return self.item_name
    
class Reservation(models.Model):
    def __str__(self):
        return f"{self.item} varattuna käyttäjälle {self.user.username}"
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_reserved = models.DateField(auto_now_add=True)
    date_returned = models.DateField(null=True, blank=True)

