from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    cover_image = models.ImageField(upload_to='covers/')
    read_online_url = models.URLField(blank=True, null=True)  # Ensure this line is present
