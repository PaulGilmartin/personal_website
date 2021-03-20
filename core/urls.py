from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    HomePageView,
    GalleryFrontPageView,
    CityPageView,
    ProjectsPageView,
    PublicationsPageView,
    ContactPageView,
    AboutPageView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('gallery/', GalleryFrontPageView.as_view(), name='gallery'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('publications/', PublicationsPageView.as_view(), name='publications'),
    path('gallery/<slug>', CityPageView.as_view(), name='city'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

