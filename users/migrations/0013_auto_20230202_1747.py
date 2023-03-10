# Generated by Django 3.2.16 on 2023-02-02 17:47

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20230202_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='profile_pic',
            field=models.FileField(blank=True, default='gsggsg', upload_to=''),
        ),
    ]
