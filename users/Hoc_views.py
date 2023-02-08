from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import CustomUser, Member, Staff
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    member_count = Member.objects.all().count()
    staff_count = Staff.objects.all().count()
    user_count = CustomUser.objects.all().count()
    context = {
        'member_count': member_count,
        'staff_count': staff_count,
        'user_count': user_count
    }
    return render(request, 'index.html', context)


@login_required(login_url='/')
def STAFF_HOME(request):
    member_count = Member.objects.all().count()
    staff_count = Staff.objects.all().count()
    user_count = CustomUser.objects.all().count()
    context = {
        'member_count': member_count,
        'staff_count': staff_count,
        'user_count': user_count
    }
    return render(request, 'index.html', context)


@login_required(login_url='/')
def MEMBER_HOME(request):
    return render(request, 'member.html')


# Add Staff

@login_required(login_url='/')
def Add_staff(request):

    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is already taken")
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username is already taken")
            return redirect('add_staff')

        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                phone_number=phone_number,
                user_type=2)
            user.set_password(password)
            user.save()

            staff = Staff(
                admin=user,
                address=address,
                gender=gender,
            )
            staff.save()
            messages.success(request, "staff is successfuly added")
            return redirect('add_staff')

    return render(request, 'Hoc/staffs/add_staff.html')

#  VIEW STAFF


def View_staff(request):
    staff = Staff.objects.all()

    context = {
        'staff': staff
    }
    return render(request, 'Hoc/staffs/view_staff.html', context)

# EDIT STAFF


def Edit_staff(request, id):
    staff = Staff.objects.filter(id=id)

    context = {
        'staff': staff,
    }
    return render(request, 'Hoc/staffs/edit_staff.html', context)

# UPDATE STAFF


def Update_staff(request):

    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        print(staff_id)
        profile_pic = request.FILES.get('profile.pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        user = CustomUser.objects.get(id=staff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.address = address
        staff.gender = gender

        staff.save()
        messages.success(request, 'Records are successfully updated')
        return redirect('view_staff')

    return render(request, 'Hoc/staffs/edit_staff.html')

# DELETE STAFF


def Delete_staff(request, admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()

    messages.success(request, 'Record are successfully deleted')

    return redirect('view_staff')


# ADD MEMBER
@login_required(login_url='/')
def Add_member(request):

    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is already taken")
            return redirect('add_member')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username is already taken")
            return redirect('add_member')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                phone_number=phone_number,
                user_type=3)
            user.set_password(password)
            user.save()

            member = Member(
                admin=user,
                address=address,
                gender=gender,
                # phone_number=phone_number,
            )
            member.save()
            messages.success(request, user.first_name +
                             ' ' + user.last_name + " is successfuly added")
            return redirect('add_member')

    return render(request, 'Hoc/members/add_member.html')


# VIEW MEMBER
def View_member(request):
    member = Member.objects.all()

    context = {
        'member': member
    }
    return render(request, 'Hoc/members/view_member.html', context)

# EDIT MEMBER


def Edit_member(request, id):
    member = Member.objects.filter(id=id)

    context = {
        'member': member,
    }
    return render(request, 'Hoc/members/edit_member.html', context)


def Update_member(request):

    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        print(member_id)
        profile_pic = request.FILES.get('profile.pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        user = CustomUser.objects.get(id=member_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        member = Member.objects.get(admin=member_id)
        member.address = address
        member.gender = gender

        member.save()
        messages.success(request, 'Records are successfully updated')
        return redirect('view_member')

    return render(request, 'Hoc/members/edit_member.html')


def Delete_member(request, admin):
    member = CustomUser.objects.get(id=admin)
    member.delete()

    messages.success(request, 'Record are successfully deleted')

    return redirect('view_member')
