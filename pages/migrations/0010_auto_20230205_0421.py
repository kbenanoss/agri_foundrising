# Generated by Django 3.2.16 on 2023-02-05 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20230205_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='about',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='pages',
            name='picurl',
            field=models.TextField(default=''),
        ),
    ]
