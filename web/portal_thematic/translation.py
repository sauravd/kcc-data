from modeltranslation.translator import register, TranslationOptions
from .models import PortalThematicSetting, PortalCard, AboutPage

@register(PortalThematicSetting)
class PortalThematicSettingTR(TranslationOptions):
    fields = ("site_title", "organization",)

@register(PortalCard)
class PortalCardTR(TranslationOptions):
    fields = ("title", "description",)

@register(AboutPage)
class AboutPageTR(TranslationOptions):
    fields = ("content",)
