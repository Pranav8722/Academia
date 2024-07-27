from django.db import models

class Paper(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    document = models.FileField(upload_to='papers/')
    read_online_url = models.URLField(blank=True, null=True)
    # cover_image = models.ImageField(upload_to='papers/covers/', blank=True, null=True)  # Remove or comment out this line if you no longer need it

    def __str__(self):
        return self.title
