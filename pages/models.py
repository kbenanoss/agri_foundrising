from django.db import models

# Create your models here.


class Pages(models.Model):

    name = models.CharField(default="Name of Company", max_length=200)
    about = models.TextField(default="", max_length=200)
    logo = models.ImageField(
        upload_to='assets/images/users/profile_pic/', default="")
    abouttxt = models.TextField(default="")
    general_address = models.TextField(default="")
    fb = models.CharField(default="-", max_length=200)
    tw = models.CharField(default="-", max_length=200)
    insta = models.CharField(default="-", max_length=200)
    yt = models.CharField(default="-", max_length=200)
    tell = models.CharField(default="-", max_length=200)
    link = models.CharField(default="-", max_length=200)
    site_email = models.EmailField(default="site@email.com", max_length=254)
    set_name = models.CharField(default="-", max_length=200)

    
    picurl = models.TextField(default="")
    picname = models.TextField(default="")

    picurl2 = models.TextField(default="")
    picname2 = models.TextField(default="")

    class Meta:
        verbose_name = 'page'
        verbose_name_plural = 'pages'

    def __str__(self):
        return self.set_name + " | " + str(self.pk)


class HomePage(models.Model):
    title = models.CharField(default="", max_length=200, blank=True)
    strengh = models.TextField(default="", max_length=200, blank=True)
    our_mission = models.CharField(default="", max_length=255, blank=True)
    our_vision = models.CharField(default="", max_length=255, blank=True)
    our_trademark = models.CharField(default="", max_length=255, blank=True)
    our_strategy = models.CharField(default="", max_length=255, blank=True)
    achi_title = models.TextField(default="", max_length=200, blank=True)
    achi_description = models.CharField(default="", max_length=255, blank=True)
    achi_image = models.ImageField(upload_to='assets/images/achievements/', default="", blank=True)
    quote = models.CharField(default="", max_length=255, blank=True)
    # our_strategy = models.CharField(default="", max_length=255, blank=True)

    def __str__(self):
        return self.title


class MainSlider(models.Model):
    images = models.ImageField(
        upload_to='assets/frontend/images/main-sliders', default="gdggd", blank=True)
    title_one = models.CharField(
        max_length=200, default='Title one', blank=True)
    title_two = models.CharField(
        max_length=200, default='Title two', blank=True)
    description = models.CharField(
        max_length=200, default='Description here', blank=True)
    btn_one_text = models.CharField(
        max_length=200, default='Button one text', blank=True)
    btn_two_text = models.CharField(
        max_length=200, default='Button two text', blank=True)
    btn_three_text = models.CharField(
        max_length=200, default='Button three text', blank=True)
    btn_four_text = models.CharField(
        max_length=200, default='Button four text', blank=True)

    btn_one_url = models.CharField(
        max_length=200, default='Button one url', blank=True)
    btn_two_url = models.CharField(
        max_length=200, default='Button two url', blank=True)
    btn_three_url = models.CharField(
        max_length=200, default='Button three url', blank=True)
    btn_four_url = models.CharField(
        max_length=200, default='Button four url', blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

class FooterConfig(models.Model):
    
    working_hours_txt_name = models.CharField(default="-", max_length=200)
    working_day = models.CharField(default="-", max_length=200)
    working_hours = models.CharField(default="No Work", max_length=200)
    services = models.CharField(default="Services List", max_length=200)

    def __str__(self):
        return self.working_day + " | " + self.working_hours