# portal/urls.py
from django.urls import path, reverse
from django.shortcuts import redirect
from .views import index, about, site_logout

app_name = "portal"

def admin_login_redirect(request):
    """
    Send users to the default Django admin login *with* ?next=/admin/,
    so after they log in they land in the admin dashboard.
    """
    return redirect(f"{reverse('admin:login')}?next=/admin/")

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),

    # Site-wide logout: Django 5 requires POST — our templates use a POST form.
    path("logout/", site_logout, name="logout"),

    # Keep the default admin login page (centered) but expose it at /login
    path("login/", admin_login_redirect, name="login"),
]
