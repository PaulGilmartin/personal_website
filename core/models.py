from django.db import models
from django.urls import reverse


class Picture(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True)
    picture = models.ImageField(upload_to='pictures/')
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def orientation(self):
        return 'Landscape'

    def modal_images(self):
        return [self.picture]

    def get_absolute_url(self):
        return reverse('picture_detail', kwargs={'pk': str(self.pk)})

