# Generated by Django 2.2.6 on 2019-10-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelmy', '0007_destination_hotel_url1'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='dest_map',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
