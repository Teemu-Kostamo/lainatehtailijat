# Generated by Django 5.0.3 on 2024-04-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lainatehdas', '0009_alter_reservation_date_returned'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_img',
            field=models.ImageField(default='images/image-coming-soon-placeholder.webp', upload_to='images/'),
        ),
    ]