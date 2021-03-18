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


class AbstractMedia(models.Model):
    title = models.CharField(max_length=200)
    content_path = models.CharField(max_length=500, null=True, blank=True)
    abstract = models.TextField()
    coauthors = models.TextField(blank=True, default="")

    class Meta:
        abstract = True

    def __str__(self):
        return self.title[:100]

    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.title)


class Paper(AbstractMedia):
    pass


class Project(AbstractMedia):
    pass

