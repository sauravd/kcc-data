from django.shortcuts import render, get_object_or_404, redirect
from .models import PortalSetting, CarouselImage, PortalCard, AboutPage
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views 
from django.views.decorators.http import require_http_methods


class PortalLoginView(auth_views.LoginView):
    template_name = "portal/login.html"

    def get_success_url(self):
        user = self.request.user
        if user.is_active and user.is_staff:
            return "/admin/"
        return super().get_success_url()

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


@require_http_methods(["GET", "POST"])
def site_logout(request):
    """
    Unified logout for both admin and site.
    Accepts GET (for safety if a plain link is followed) and POST.
    Always redirects to the portal home page.
    """
    logout(request)
    return redirect("portal:index")

