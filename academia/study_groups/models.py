from django.db import models

class StudyGroup(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    meeting_time = models.DateTimeField()
    contact_info = models.CharField(max_length=200)
    document = models.FileField(upload_to='study_groups/', blank=True, null=True)
    whatsapp_link = models.URLField(blank=True, null=True)  # Add this line

    def __str__(self):
        return self.name
