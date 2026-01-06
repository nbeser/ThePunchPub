from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="drive")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"