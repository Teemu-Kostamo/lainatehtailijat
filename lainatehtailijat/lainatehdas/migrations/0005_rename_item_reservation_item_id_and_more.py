# Generated by Django 5.0.3 on 2024-04-17 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lainatehdas', '0004_remove_item_item_avail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='item',
            new_name='item_id',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='user',
            new_name='user_id',
        ),
    ]