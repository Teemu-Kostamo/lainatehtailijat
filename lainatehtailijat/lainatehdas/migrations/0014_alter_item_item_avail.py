# Generated by Django 5.0.3 on 2024-04-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lainatehdas', '0013_alter_item_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_avail',
            field=models.CharField(choices=[('Va', 'Vapaa'), ('Vr', 'Varattu'), ('Hu', 'Huollossa'), ('Ri', 'Rikki')], default='Va', max_length=2),
        ),
    ]