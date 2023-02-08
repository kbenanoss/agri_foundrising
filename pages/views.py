from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin




def home(request):
    return render(request, 'pages/dashboard/home.html')