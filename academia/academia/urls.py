from django.contrib import admin
from django.urls import path
from books.views import books_list
from academia.views import home
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('books/', books_list, name='books_list'),
    path('papers/', include('papers.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
