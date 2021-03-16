from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomePageView, GalleryFrontPageView, CityPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('gallery/', GalleryFrontPageView.as_view(), name='gallery'),
    path('gallery/<slug>', CityPageView.as_view(), name='city'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
