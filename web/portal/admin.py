from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import PortalSetting, CarouselImage, PortalCard, AboutPage

admin.site.site_header = admin.site.site_title = admin.site.index_title = "Admin"

@admin.register(PortalSetting)
class PortalSettingAdmin(TranslationAdmin):
    fieldsets = [
        (None, {
            "fields": ["logo", "favicon", "site_title", "organization", "copyright_year"]
        }),
        ("Colors", {
            "fields": [
                "header_color", "header_text_color", "login_text_color",
                "footer_color", "footer_text_color",
                "card_color", "body_bg_color", "body_text_color",
            ]
        }),
    ]

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ("id", "order")

@admin.register(PortalCard)
class PortalCardAdmin(TranslationAdmin):
    list_display = ("title", "order")

@admin.register(AboutPage)
class AboutPageAdmin(TranslationAdmin):
    list_display = ("__str__",)
