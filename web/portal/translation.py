from modeltranslation.translator import register, TranslationOptions
from .models import PortalSetting, PortalCard, AboutPage

@register(PortalSetting)
class PortalSettingTR(TranslationOptions):
    # Add site_title (and organization if you want it translatable too)
    fields = ("site_title", "organization",)

@register(PortalCard)
class PortalCardTR(TranslationOptions):
    fields = ("title", "description",)

@register(AboutPage)
class AboutPageTR(TranslationOptions):
    fields = ("content",)
