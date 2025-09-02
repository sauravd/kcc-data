from modeltranslation.translator import register, TranslationOptions
from .models import PortalCard, AboutPage, PortalSetting

@register(PortalCard)
class PortalCardTranslation(TranslationOptions):
    fields = ('title', 'description',)

@register(AboutPage)
class AboutPageTranslation(TranslationOptions):
    fields = ('content',)


@register(PortalSetting)
class PortalSettingTranslation(TranslationOptions):
    fields = (
        'site_title',
        'organization',
        'home_label',
        # If you’d also like your login/logout link text or captions translatable:
        # 'login_text',
        # 'logout_text',
    )

