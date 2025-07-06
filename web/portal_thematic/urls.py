from django.urls import path, include
from .views import index, about, site_logout

app_name = 'portal_thematic'

urlpatterns = [
  path('', index, name='index'),
  path('about/', about, name='about'),
  path('logout/', site_logout, name='logout'), 
]

