from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class CustomUser(AbstractUser):
    user_type_data = (
        (1, "HOC"),
        (2, "Staff"),
        (3, "WebAdmin")
    )
    user_type = models.CharField(
        default=1, choices=user_type_data, max_length=10)
    profile_pic = models.ImageField(
        upload_to='assets/images/users/profile_pic/')
    phone_number = PhoneNumberField(blank=True, unique=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone_number']


class AdminHOC(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Staff(models.Model):
    # id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255)
    # profile_pic = models.FileField(default='gsggsg', blank=True)
    address = models.TextField()
    phone_number = PhoneNumberField(blank=True, unique=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# class WebAdmin(models.Model):
#     id = models.AutoField(primary_key=True)
#     admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     gender = models.CharField(max_length=255)
#     profile_pic = models.FileField()
#     address = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     objects = models.Manager()

    # def __str__(self):
    #     return self.admin.username


class Member(models.Model):

    admin = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE)
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    username = models.CharField(max_length=255, default='username')
    gender = models.CharField(max_length=255)
    profile_pic = models.FileField()
    address = models.TextField()
    # phone_number = PhoneNumberField(blank=True, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.admin.first_name + "  " + self.admin.last_name

    # signals


# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.user_type == 1:
#             AdminHOC.objects.create(admin=instance)
#         if instance.user_type == 2:
#             Staff.objects.create(admin=instance, address="", profile_pic="")
#         if instance.user_type == 3:
#             WebAdmin.objects.create(
#                 admin=instance, address="", profile_pic="", gender="")


# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.user_type == 1:
#         instance.adminhoc.save()
#     if instance.user_type == 2:
#         instance.staff.save()
#     if instance.user_type == 3:
#         instance.webadmin.save()
