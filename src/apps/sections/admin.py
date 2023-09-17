from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from .models import Section

class SectionAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

# admin.site.register(Section, SectionAdmin) - Не нуждается в отображении в админ-панели