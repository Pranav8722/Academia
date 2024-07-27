from django.contrib import admin
from .models import StudyGroup

class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'meeting_time', 'contact_info', 'whatsapp_link')  # Add 'whatsapp_link' to list_display

admin.site.register(StudyGroup, StudyGroupAdmin)
