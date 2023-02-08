from django.urls import path, include
from . import views
from . import Hoc_views
from pages import pages_views
# from pages.pages_views import StaffNumJsonView
from django.conf import settings
from django.conf.urls.static import static
# from . views import StaffNumJsonView



urlpatterns = [
    # Frontend Pages
    path('', pages_views.home, name='index'),
#     path('/anani/', StaffNumJsonView.as_view(), name='staffs-json'),
    path('management-team', pages_views.managementTeam, name='management_team'),
    path('our-collaborators', pages_views.ourColaborators,
         name='our_collaborators'),
    path('our-gallery', pages_views.ourGallery, name='our_gallery'),




    path('admin-signup', views.signupAdmin, name="admin_signup"),
    path('staff/signup', views.signupStaff, name="staff_signup"),

    path('dashboard/', views.Index, name="dashboard"),
    path('register', views.register, name='register'),
    path('login', views.LOGIN, name='login'),
    # path('', include('frontend.urls')),
    path('doLogin', views.doLogin, name='doLogin'),
    path('get_user_details', views.GetUserDetails),
    path('doLogout', views.doLogout, name='logout'),

    # path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    # path('forgotPassword', views.forgotPassword, name='forgotPassword'),

    # path('resetpassword_validate/<uidb64>/<token>/',
    #      views.resetpassword_validate, name='resetpassword_validate'),

    # path('resetPassword/', views.resetPassword, name='resetPassword'),



    path('dashboard/profile', views.PROFILE, name='profile'),
    path('dashboard/profile/update', views.PROFILE_UPDATE, name='profile_update'),
#     path('dashboard/settings', views.Settings, name='settings'),
    path('dashboard/site-settings', views.site_settings, name='site_settings'),
    path('dashboard/footer-settings', views.footer_settings, name='footer_settings'),
    path('dashboard/footer-settings', views.add_footer_settings, name='add_footer_settings'),
    path('dashboard/footer-settings/edit/<int:id>/', views.edit_footer_settings, name='edit_footer_settings'),
    path('dashboard/footer-settings/update/<int:id>/', views.update_footer_settings, name='update_footer_settings'),
    path('dashboard/footer-settings/delete/<int:id>/', views.delete_footer_settings, name='delete_footer_settings'),


    # Pastor/MainAdmin panel
    path('dashboard/Home', Hoc_views.HOME, name='admin_dashboard'),
    path('dashboard/staff', Hoc_views.STAFF_HOME, name='staff_dashboard'),
    path('dashboard/member', Hoc_views.MEMBER_HOME, name='member_dashboard'),

    path('dashboard/member/add', Hoc_views.Add_member, name='add_member'),
    path('dashboard/member/view', Hoc_views.View_member, name='view_member'),
    path('dashboard/member/edit/<str:id>',
         Hoc_views.Edit_member, name='edit_member'),
    path('dashboard/member/update', Hoc_views.Update_member, name='update_member'),
    path('dashboard/member/delete/<str:admin>',
         Hoc_views.Delete_member, name='delete_member'),

    # Staff
    path('dashboard/staff/add', Hoc_views.Add_staff, name='add_staff'),
    path('dashboard/staff/view', Hoc_views.View_staff, name='view_staff'),
    path('dashboard/staff/edit/<str:id>',
         Hoc_views.Edit_staff, name='edit_staff'),
    path('dashboard/staff/update', Hoc_views.Update_staff, name='update_staff'),
    path('dashboard/staff/delete/<str:admin>',
         Hoc_views.Delete_staff, name='delete_staff'),


    path('dashboard/error_404', pages_views.error_404, name='error_404'),




    path('panel/pages/', include('pages.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
