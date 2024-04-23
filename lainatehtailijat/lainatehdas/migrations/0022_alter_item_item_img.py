# Generated by Django 5.0.3 on 2024-04-23 14:46

import lainatehdas.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lainatehdas', '0021_alter_reservation_date_reserved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_img',
            field=models.ImageField(default='media/placeholder.jpg', upload_to='media/', validators=[lainatehdas.models.validate_image_dimensions]),
        ),
    ]