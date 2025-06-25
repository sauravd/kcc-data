from django.contrib import admin
from .models import PortalSetting, CarouselImage, PortalCard, AboutPage


# Fetch the one PortalSetting (if it exists)
try:
    cfg = PortalSetting.objects.first()
    admin_title = cfg.site_title
except Exception:
    admin_title = "Portal Administration"


admin.site.site_header = admin_title
admin.site.site_title = admin_title
admin.site.index_title = admin_title

@admin.register(PortalSetting)
class PortalSettingAdmin(admin.ModelAdmin):
    fieldsets = [
      (None, {'fields': ['logo','favicon','site_title','organization','copyright_year']}),
      ('Colors', {'fields': ['header_color','footer_color','card_color','body_bg_color','body_text_color']}),
    ]
    fieldsets = [
      (None, {
         'fields': [
           'logo', 
           'site_title',
           'organization',
           'copyright_year',
         ]
      }),
      ('Colors', {
         'fields': [
           'header_color',
           'header_text_color',
           'login_text_color',
           'footer_color',
           'footer_text_color',
           'card_color',
           'body_bg_color',
           'body_text_color',
         ]
      }),
    ]



@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    pass

@admin.register(PortalCard)
class PortalCardAdmin(admin.ModelAdmin):
    pass

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ['__str__']