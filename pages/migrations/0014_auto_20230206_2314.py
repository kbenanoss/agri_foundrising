# Generated by Django 3.2.16 on 2023-02-06 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20230206_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footerconfig',
            name='set_name',
        ),
        migrations.AddField(
            model_name='pages',
            name='set_name',
            field=models.CharField(default='-', max_length=200),
        ),
    ]
