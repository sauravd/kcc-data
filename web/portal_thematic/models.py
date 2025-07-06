from django.db import models
from django.utils.translation import gettext_lazy as _


class PortalThematicSetting(models.Model):
    favicon = models.ImageField(_('Favicon'), upload_to='favicons/', blank=True, help_text=_('Upload a 16x16 or 32x32 .ico or .png favicon'))
    logo = models.ImageField(_('Logo'), upload_to='logos/', blank=True, help_text=_('Upload a square or landscape logo (e.g. 100x100px or 200x50px)'))
    site_title       = models.CharField(_('Site title'), max_length=100, default='FAO-NRM Data Portal')
    header_color     = models.CharField(_('Header color'), max_length=7, default='#ffffff')
    header_text_color = models.CharField(_('Header text color'), max_length=7, default="#080808")
    login_text_color  = models.CharField(_('Login link color'), max_length=7, default='#007bff')
    home_label        = models.CharField(_('Home link text'), max_length=30, default=_('Home'), help_text=_('Label for the Home nav link'))
    main_label        = models.CharField(_('Main site link text'), max_length=30, default=_('Main'), help_text=_('Label for the Main-site nav link (back to the central portal)'))
    footer_color     = models.CharField(_('Footer color'), max_length=7, default='#5792c9')
    footer_text_color = models.CharField(_('Footer text color'), max_length=7, default="#080808")
    card_color       = models.CharField(_('Card background'), max_length=7, default='#ffffff')
    body_bg_color    = models.CharField(_('Body background'), max_length=7, default='#f8f9fa')
    body_text_color  = models.CharField(_('Body text color'), max_length=7, default='#5792c9')
    organization     = models.CharField(_('Organization name'), max_length=100, default='FAO-NRM Data Portal')
    copyright_year   = models.PositiveIntegerField(_('Copyright year'), default=2025)

    class Meta:
        verbose_name = _('Portal setting')
        verbose_name_plural = _('Portal settings')

    def __str__(self):
        return self.site_title


class CarouselImage(models.Model):
    portal      = models.ForeignKey(PortalThematicSetting, on_delete=models.CASCADE, related_name='carousel_images')
    image       = models.ImageField(_('Image'), upload_to='carousel/')
    caption     = models.CharField(_('Caption'), max_length=200, blank=True)
    order       = models.PositiveSmallIntegerField(_('Order'), default=0)

    class Meta:
        ordering = ['order']
        verbose_name = _('Carousel image')
        verbose_name_plural = _('Carousel images')


class PortalCard(models.Model):
    portal      = models.ForeignKey(PortalThematicSetting, on_delete=models.CASCADE, related_name='cards')
    title       = models.CharField(_('Card title'), max_length=100)
    description = models.TextField(_('Description'), blank=True)
    url         = models.URLField(_('Link URL'))
    order       = models.PositiveSmallIntegerField(_('Order'), default=0)

    class Meta:
        ordering = ['order']
        verbose_name = _('Portal card')
        verbose_name_plural = _('Portal cards')


class AboutPage(models.Model):
    content = models.TextField(
        _('About content'),
        help_text=_('HTML or plain text for the About page')
    )

    class Meta:
        verbose_name = _('About page')
        verbose_name_plural = _('About pages')

    def __str__(self):
        return str(_('About Page'))