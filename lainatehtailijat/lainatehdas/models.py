from django.db import models

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
    # item_img = 
    item_avail = models.CharField(max_length=2, choices=item_avail_choices, verbose_name="Availability")
    def __str__(self) -> str:
        return self.item_name