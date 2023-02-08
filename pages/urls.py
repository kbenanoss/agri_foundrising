from django.urls import path
from pages import pages_views
from django.conf import settings
from . import views
from django.conf.urls.static import static
urlpatterns = [
    
    path('home', views.home, name='backend_home_page'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
