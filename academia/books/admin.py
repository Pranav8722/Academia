from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'read_online_url')  # Display this field in the list view
    search_fields = ('title', 'author')  # Add search functionality

admin.site.register(Book, BookAdmin)
