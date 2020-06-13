# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import mark_safe


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class main_site(models.Model):
    site_id = models.AutoField(primary_key=True, verbose_name='ID')
    site_name = models.CharField(max_length=250, unique=True, verbose_name='Site Name', blank=False,
                                 null=False)
    site_short_name = models.CharField(max_length=100, unique=True, verbose_name='Site Short Name', blank=False,
                                       null=False)
    site_name_link = models.CharField(max_length=250, unique=True, verbose_name='Site Name link', blank=False,
                                      null=False)
    site_author = models.CharField(max_length=250, unique=True, verbose_name='Site Author', default='')
    site_generator = models.CharField(max_length=250, unique=True, verbose_name='Site Generator', default='')
    site_description = models.CharField(max_length=2000, unique=True, verbose_name='Site Description', default='')
    site_default_theme = models.CharField(max_length=100, unique=True, verbose_name='Site Default Theme',
                                          default='blogs')

    site_name_link = models.CharField(max_length=250, unique=True, verbose_name='Site Name link', blank=False,
                                      null=False)

    site_logo = models.ImageField(upload_to='core/website/images/')

    def __str__(self):
        return self.site_name

    class Meta:
        ordering = ['site_id']
        verbose_name_plural = 'Main Sites'
        verbose_name = 'Main Site'
        indexes = [
            models.Index(fields=['site_name', ]),
            models.Index(fields=['site_short_name', ]),
        ]


class menu(models.Model):
    menu_id = models.AutoField(primary_key=True, verbose_name='ID')
    menu_order = models.IntegerField(verbose_name='Menu Order', unique=True)
    menu_name = models.CharField(max_length=250, unique=True, verbose_name='Menu Name', blank=False,
                                 null=False)
    menu_link = models.CharField(max_length=250, verbose_name='Menu Link', blank=False,
                                 null=True)
    menu_isRootMenu = models.BooleanField(verbose_name='is Root Menu', default=True)
    menu_super_menu = models.ForeignKey('self', null=True, blank=True, related_name='items',
                                        limit_choices_to={'menu_isRootMenu': True}, on_delete=models.CASCADE)
    menu_fontawesome = models.CharField(max_length=250, verbose_name='Menu Box Item fontawesome',
                                        help_text="get Images form https://fontawesome.com/icons?m=free",
                                        blank=True,
                                        null=True)

    def __str__(self):
        return self.menu_name

    class Meta:
        ordering = ['menu_order']
        verbose_name_plural = 'Menu Items'
        verbose_name = 'Menu Item'
        indexes = [
            models.Index(fields=['menu_name', ]),
            models.Index(fields=['menu_link', ]),
            models.Index(fields=['menu_order', ]),
            models.Index(fields=['menu_super_menu', ]),
        ]


class footer(models.Model):
    footer_id = models.AutoField(primary_key=True, verbose_name='ID')
    footer_text = models.CharField(max_length=250, unique=True, verbose_name='Footer Text', blank=False,
                                   null=False)
    footer_year = models.CharField(max_length=250, unique=True, verbose_name='Footer Year', blank=False,
                                   null=True)
    footer_version = models.CharField(max_length=250, unique=True, verbose_name='Footer Version', blank=False,
                                      null=False)
    footer_address = models.CharField(max_length=1024, unique=True, verbose_name='Footer Address', blank=False,
                                      null=False)

    footer_logo = models.ImageField(upload_to='core/website/images/')

    def __str__(self):
        return self.footer_text

    class Meta:
        ordering = ['footer_id']
        verbose_name_plural = 'Footers'
        verbose_name = 'Footer'
        indexes = [
            models.Index(fields=['footer_text', ]),
            models.Index(fields=['footer_year', ]),
            models.Index(fields=['footer_version', ]),
            models.Index(fields=['footer_address', ]),
        ]


class menu_box(models.Model):
    menu_box_id = models.AutoField(primary_key=True, verbose_name='ID')
    menu_box_name = models.CharField(max_length=250, unique=True, verbose_name='Menu Box Name', blank=False,
                                     null=False)
    menu_box_logo = models.ImageField(upload_to='core/website/images/', null=True, blank=True)
    menu_box_order = models.IntegerField(verbose_name='Menu Box Order')

    def __str__(self):
        return self.menu_box_name

    class Meta:
        ordering = ['menu_box_order']
        verbose_name_plural = 'Menu Boxes'
        verbose_name = 'Menu Box'
        indexes = [
            models.Index(fields=['menu_box_name', ]),
            models.Index(fields=['menu_box_order', ]),
        ]


class menu_box_item(models.Model):
    menu_box_item_id = models.AutoField(primary_key=True, verbose_name='ID')
    menu_box_item_name = models.CharField(max_length=250, unique=True, verbose_name='Menu Box Item Name', blank=False,
                                          null=False)
    menu_box_item_order = models.IntegerField(verbose_name='Menu Box Item Order')
    menu_box = models.ForeignKey(menu_box, null=True, related_name='items', on_delete=models.CASCADE)
    menu_box_link = models.CharField(max_length=250, verbose_name='Item link', blank=False,
                                     null=False, default='')

    # see https://fontawesome.com/icons?m=free
    menu_box_item_fontawesome = models.CharField(max_length=250, verbose_name='Menu Box Item fontawesome',
                                                 help_text="get Images form https://fontawesome.com/icons?m=free",
                                                 blank=True,
                                                 null=True)

    def __str__(self):
        return self.menu_box_item_name

    class Meta:
        ordering = ['menu_box', 'menu_box_item_order']
        verbose_name_plural = 'Menu Box Items'
        verbose_name = 'Menu Box Item'
        indexes = [
            models.Index(fields=['menu_box_item_name', ]),
            models.Index(fields=['menu_box_item_order', ]),
            models.Index(fields=['menu_box', ]),
        ]


class language(models.Model):
    language_id = models.AutoField(primary_key=True, verbose_name='Language ID')
    language_name = models.CharField(max_length=250, unique=True, verbose_name='Language name', blank=False,
                                     help_text="see https://developer.chrome.com/webstore/i18n", null=False)
    language_code = models.CharField(max_length=10, unique=True,
                                     verbose_name='Language Code',
                                     help_text="see https://developer.chrome.com/webstore/i18n",
                                     blank=False,
                                     null=False)
    language_logo = models.ImageField(upload_to='core/languages/flags/')
    right_to_left_text = models.BooleanField(verbose_name='Is the text is written from right to left?', default=False)

    def image_tag(self):
        return mark_safe('<img src="%s" width="20" height="20" />' % (self.language_logo.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.language_name

    class Meta:
        ordering = ['language_name']
        verbose_name_plural = 'Languages'
        verbose_name = 'Language'
        indexes = [
            models.Index(fields=['language_name', ]),
            models.Index(fields=['language_code', ]),
        ]


class translation(models.Model):
    translation_id = models.AutoField(primary_key=True, verbose_name='translation ID')
    original_text = models.TextField(verbose_name='Original Text', blank=False, null=False)
    translation_language = models.ForeignKey(language, null=True, related_name='translations', on_delete=models.CASCADE)
    translated_text = models.TextField(verbose_name='Original Text', blank=False, null=False)
    checked = models.BooleanField(verbose_name='Translation Validated', default=False)

    def __str__(self):
        return 'to ' + self.translation_language.language_name + '[' + self.original_text + ']'

    class Meta:
        ordering = ['translation_language']
        verbose_name_plural = 'Translations'
        verbose_name = 'Translation'
        indexes = [
            models.Index(fields=['translation_language', ]),
            models.Index(fields=['original_text', ]),
            models.Index(fields=['checked', ]),

        ]
