# Generated by Django 5.0.3 on 2024-04-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lainatehdas', '0010_item_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_img',
            field=models.ImageField(default='static/images/placeholder.jpg', upload_to='images/'),
        ),
    ]
