from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomePageView, GalleryFrontPageView, CityPageView, ProjectsPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('gallery/', GalleryFrontPageView.as_view(), name='gallery'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('gallery/<slug>', CityPageView.as_view(), name='city'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
