from django.shortcuts import render, redirect, HttpResponse
from .models import CustomUser
from .EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from .forms import RegistrationForm
from django.contrib.auth.models import User, Group, Permission
from django.core.files.storage import FileSystemStorage
from pages.models import Pages, FooterConfig
from django.shortcuts import get_object_or_404
# from django.views.generic import TemplateView, View



def Index(request):
    return render(request, 'index.html')


def signupAdmin(request):
    return render(request, "user_account/signup.html")


def signupStaff(request):
    return render(request, "user_account/signup.html")


def LOGIN(request):
    return render(request, 'user_account/login.html')

# def Settings(request):
#     return render(request, 'settings.html')

def footer_settings(request):
    footer_list = FooterConfig.objects.all()
    context = {'footer_list':footer_list}
    return render(request, 'footer_settings.html', context)

def add_footer_settings(request):
    # footer = Pages.objects.all() 
    if request.method == 'POST':
        
        working_hours_txt_name = request.POST.get('working_hours_txt_name')
        working_day = request.POST.get('working_day')
        working_hours = request.POST.get('working_hours')
        services = request.POST.get('services')

        f = FooterConfig(
            working_hours_txt_name = working_hours_txt_name,
            working_day = working_day,
            working_hours = working_hours,
            services = services
        )
        f.save()
        messages.info(request, "Your item is added successfully")
    else:
        pass
        return render(request, 'footer_settings.html')
   
    
        
    footer_list = FooterConfig.objects.all()
    context = {'footer_list':footer_list}
    return render(request, 'footer_settings.html', context)


def edit_footer_settings(request, id):
    
    footer_list = FooterConfig.objects.all()
    footer_edit = FooterConfig.objects.get(id=id)

    context = {
        'footer_edit':footer_edit,
        'footer_list':footer_list,
            # 'error': 'The post was not successfully updated. The title and content must be filled out.'

    }
    return render(request, 'footer_settings.html', context)

def update_footer_settings(request, id):
    footer_update = FooterConfig.objects.get(id=id)


    footer_update.working_hours_txt_name = request.POST.get('working_hours_txt_name')
    footer_update.working_day = request.POST.get('working_day')
    footer_update.working_hours = request.POST.get('working_hours')
    footer_update.services = request.POST.get('services')
    footer_update.save()
    messages.info(request, "Your information is updated successfully")
    return redirect('footer_settings')


def delete_footer_settings(request, id):
    footer_item = FooterConfig.objects.get(id=id)
    footer_item.delete()
    messages.info(request, "Your information is deleted successfully")
    return redirect('footer_settings')

def site_settings(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('login')
    # login check end

    # perm = 0
    # for i in request.user.groups.all():
    #     if i.name == "admin":
    #         perm = 1
        # if i.name == "staff":
        #     perm = 2

    # if perm == 0:
    #     error = "Access Denied"
    #     return render(request, '404_page.html', {'error': error})

    if request.method == 'POST':

        name = request.POST.get('name')
        logo = request.FILES.get('logo')
        site_email = request.POST.get('site_email')
        tell = request.POST.get('tell')
        fb = request.POST.get('fb')
        tw = request.POST.get('tw')
        yt = request.POST.get('yt')
        insta = request.POST.get('insta')
        link = request.POST.get('link')
        # about = request.POST.get('about')

        txt = request.POST.get('txt')

        if fb == "":
            fb = "#"
        if tw == "":
            tw = "#"
        if insta == "":
            insta = "#"
        if yt == "":
            yt = "#"

        if name == "" or tell == "" or txt == "":
            error = "All Fields Requirded"
            return render(request, '404_page.html', {'error': error})

        try:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            picurl = url
            picname = filename

        except:

            picurl = "-"
            picname = "-"

        try:

            myfile2 = request.FILES['myfile2']
            fs2 = FileSystemStorage()
            filename2 = fs2.save(myfile2.name, myfile2)
            url2 = fs2.url(filename2)

            picurl2 = url2
            picname2 = filename2

        except:

            picurl2 = "-"
            picname2 = "-"

        b = Pages.objects.get(pk=1)
        b.name = name
        b.logo = logo
        b.site_email = site_email
        b.tell = tell
        b.fb = fb
        b.tw = tw
        b.insta = insta
        b.yt = yt
        b.link = link
        # b.txt = txt
        # b.about = about

        if picurl != "-":
            b.picurl = picurl
        if picname != "-":
            b.picname = picname
        if picurl2 != "-":
            b.picurl2 = picurl2
        if picname2 != "-":
            b.picname2 = picname2

        b.save()

    site = Pages.objects.get(pk=1)

    context = {
        'site': site
    }

    return render(request, 'settings.html', context)


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get(
            "email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.user_type == "1":
                messages.success(request, 'Successfully logged in as ' +
                                 user.first_name + ' ' + user.last_name + '.')
                return redirect('admin_dashboard')
            elif user.user_type == "2":
                return redirect('staff_dashboard')
            elif user.user_type == "3":
                return redirect('member_dashboard')
            else:
                return HttpResponse('Wrong credentials')
        else:
            messages.error(request, "Invalid Login Details")
            return redirect('login')


def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")


def doLogout(request):
    logout(request)
    messages.success(request, 'You have logged out successfully !')
    return redirect('login')


def register(request):
    return render(request, 'user_account/signup.html')


@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    print(user)
    context = {
        'user': user,
    }
    return render(request, 'user_account/profile.html', context)


@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # username = request.POST.get('username')
        password = request.POST.get('password')
        print(profile_pic)
        try:
            customuser = CustomUser.objects.get(id=request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name

            if password != None and password != "":
                customuser.set_password(password)
            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, 'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.error(request, 'Failed To Update Your Profile')
    return render(request, 'user_account/profile.html')



# def StaffNumJsonView(View):
#     def get(self, *args, **kwargs):
#         staff_count = Staff.objects.filter(active=True).count()
#         return JsoonResponse({'staff_count': staff_count})
