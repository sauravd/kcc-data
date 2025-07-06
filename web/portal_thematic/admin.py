from django.contrib import admin
from .models import PortalThematicSetting, CarouselImage, PortalCard, AboutPage


# Fetch the one PortalThematicSetting (if it exists)
try:
    cfg = PortalThematicSetting.objects.first()
    admin_title = cfg.site_title
except Exception:
    admin_title = "Portal Administration"


admin.site.site_header = admin_title
admin.site.site_title = admin_title
admin.site.index_title = admin_title

@admin.register(PortalThematicSetting)
class PortalThematicSettingAdmin(admin.ModelAdmin):
    fieldsets = [
      (None, {'fields': ['logo','favicon','site_title','organization','copyright_year','home_label', 'main_label']}),
      ('Colors', {'fields': ['header_color','footer_color','card_color','body_bg_color','body_text_color']}),
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

    