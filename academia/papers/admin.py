from django.contrib import admin
from .models import Paper

class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

admin.site.register(Paper, PaperAdmin)
