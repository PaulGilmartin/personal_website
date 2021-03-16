from dataclasses import dataclass

from django.views.generic import TemplateView, ListView

from core.models import Picture


@dataclass
class Link:
    link: str
    display: str
    link_args: str = ''


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = [
            # Link(link='projects', display='Projects'),
            # Link(link='publications', display='Publications'),
            Link(link='gallery', display='Gallery'),
        ]
        context['central_image'] = 'images/necropolis.jpg'
        return context


class GalleryFrontPageView(TemplateView):
    template_name = 'gallery/gallery_front.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        locations = set(Picture.objects.values_list('location', flat=True))
        context['links'] = [
            Link(link='city', link_args=location, display=location) for location in locations]
        context['central_image'] = ''
        return context


class CityPageView(ListView):
    template_name = 'gallery/city.html'
    model = Picture

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        location = self.kwargs['slug']
        context['location'] = location
        return context

    def get_queryset(self, *args, **kwargs):
        location = self.kwargs['slug']
        images_of_location = self.model.objects.filter(location=location)
        landscape_images = images_of_location
        return [landscape_images[n:n+3] for n in range(0, len(landscape_images), 3)]
