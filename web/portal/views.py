from django.shortcuts import render, get_object_or_404
from .models import PortalSetting, CarouselImage, PortalCard, AboutPage

def index(request):
    cfg, _ = PortalSetting.objects.get_or_create(
        pk=1,
        defaults={'site_title':'FAO-NRM Thematic Data Portal'}
    )
    context = {
      'cfg': cfg,
      'carousel': cfg.carousel_images.all(),
      'cards': cfg.cards.all(),
    }
    return render(request, 'portal/index.html', context)


def about(request):
    cfg, _       = PortalSetting.objects.get_or_create(pk=1, defaults={'site_title': 'Sand Systems Portal'})
    about_page, _ = AboutPage.objects.get_or_create()
    context = {
        'cfg': cfg,
        'about': about_page,
    }
    return render(request, 'portal/about.html', context)