from django.shortcuts import render
from .models import Pages, MainSlider, FooterConfig
from django.contrib.auth.decorators import login_required
from users.models import Staff
from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView


def home(request):
    site = Pages.objects.get(pk=1)
    sliders = MainSlider.objects.all()
    footer = FooterConfig.objects.all()
    

    context = {
        'site':site,
        'sliders': sliders,
        'footer': footer,
        
    }
    return render(request, 'frontend/index.html', context)


# def StaffNumJsonView(CreateView):
#     def get(self, *args, **kwargs):
#         staff_count = Staff.objects.filter(active=True).count()
#         return JsoonResponse({'staff_count': staff_count})


def managementTeam(request):
    site = Pages.objects.get(pk=1)
    return render(request, 'frontend/management-team.html', {'site': site})


def ourColaborators(request):
    site = Pages.objects.get(pk=1)
    return render(request, 'frontend/our-collaborators.html', {'site': site})


def ourGallery(request):
    site = Pages.objects.get(pk=1)
    return render(request, 'frontend/our-gallery.html', {'site': site})

def footer(request):
    footer = FooterConfig.objects.all()

    context = {
        'footer':footer,
    }
    return render(request, 'frontend/partials/footer.html', {'footer': footer})






@login_required(login_url='/')
def error_404(request):
    return render(request, '404_page.html')