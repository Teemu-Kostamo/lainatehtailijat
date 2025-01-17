# Generated by Django 5.0.3 on 2024-04-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200, verbose_name='Name')),
                ('item_desc', models.CharField(max_length=500, verbose_name='Description')),
                ('item_type', models.CharField(choices=[('Leik', 'Ruohonleikkuri'), ('Trim', 'Trimmeri'), ('Saha', 'Saha'), ('Lapi', 'Lapio'), ('Saks', 'Sakset'), ('Harv', 'Harava'), ('Muu', 'Muu')], max_length=4, verbose_name='Type')),
                ('item_avail', models.BooleanField(default=True, verbose_name='Availability')),
            ],
        ),
    ]
