# Generated by Django 3.2.16 on 2023-02-05 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20230205_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='name',
            field=models.CharField(default='Glac', max_length=30),
        ),
    ]
