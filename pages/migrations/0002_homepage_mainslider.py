# Generated by Django 3.2.16 on 2023-02-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MainSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='assets/frontend/images/main-sliders')),
                ('title_one', models.CharField(blank=True, default='Title one', max_length=200)),
                ('title_two', models.CharField(blank=True, default='Title two', max_length=200)),
                ('description', models.CharField(blank=True, default='Description here', max_length=200)),
                ('btn_one_text', models.CharField(blank=True, default='Button one text', max_length=200)),
                ('btn_two_text', models.CharField(blank=True, default='Button two text', max_length=200)),
                ('btn_three_text', models.CharField(blank=True, default='Button three text', max_length=200)),
                ('btn_four_text', models.CharField(blank=True, default='Button four text', max_length=200)),
                ('btn_one_url', models.CharField(blank=True, default='Button one url', max_length=200)),
                ('btn_two_url', models.CharField(blank=True, default='Button two url', max_length=200)),
                ('btn_three_url', models.CharField(blank=True, default='Button three url', max_length=200)),
                ('btn_four_url', models.CharField(blank=True, default='Button four url', max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
