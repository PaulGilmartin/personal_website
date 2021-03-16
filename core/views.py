from dataclasses import dataclass

from django.views.generic import TemplateView


@dataclass
class Link:
    link: str
    display: str
    link_args: str = ''


class HomePageView(TemplateView):
    template_name = 'home.html'

    # TODO: is it worth abstracting this context gathering method as an inheritable extendable one?
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = [
            # Link(link='projects', display='Projects'),
            # Link(link='publications', display='Publications'),
            # Link(link='gallery', display='Gallery'),
        ]
        context['central_image'] = 'images/necropolis.jpg'
        return context
