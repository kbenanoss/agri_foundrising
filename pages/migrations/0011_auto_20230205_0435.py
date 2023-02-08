# Generated by Django 3.2.16 on 2023-02-05 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20230205_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='logo',
            field=models.ImageField(default='', upload_to='assets/images/users/profile_pic/'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='name',
            field=models.CharField(default='Name of Company', max_length=200),
        ),
    ]
