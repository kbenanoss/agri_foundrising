# Generated by Django 3.2.16 on 2023-01-31 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230129_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(upload_to='images/users/profile_pic/'),
        ),
        migrations.AlterField(
            model_name='staffs',
            name='profile_pic',
            field=models.FileField(upload_to=''),
        ),
    ]