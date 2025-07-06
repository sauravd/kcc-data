from django.shortcuts import render, get_object_or_404, redirect
from .models import PortalThematicSetting, CarouselImage, PortalCard, AboutPage
from django.contrib.auth import logout

def index(request):
    cfg, _ = PortalThematicSetting.objects.get_or_create(
        pk=1,
        defaults={'site_title':'FAO-NRM Thematic Data Portal'}
    )
    context = {
      'cfg': cfg,
      'carousel': cfg.carousel_images.all(),
      'cards': cfg.cards.all(),
    }
    return render(request, 'portal_thematic/index.html', context)


def about(request):
    cfg, _       = PortalThematicSetting.objects.get_or_create(pk=1, defaults={'site_title': 'Sand Systems Portal'})
    about_page, _ = AboutPage.objects.get_or_create()
    context = {
        'cfg': cfg,
        'about': about_page,
    }
    return render(request, 'portal_thematic/about.html', context)


def site_logout(request):
    logout(request)
    return redirect('portal_thematic:index')

