# Generated by Django 3.2.16 on 2023-02-02 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_staff_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='profile_pic',
        ),
    ]
