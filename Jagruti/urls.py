from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.scheme_list, name='home'),
    path('info',views.society_information_view, name='society_information'),
    path('bod',views.bod, name='Board of Director'),
    path('download',views.download_view, name='Documnets to Download'),
    path('contact', views.contact, name='Contact Us'),
    path('schemes', views.scheme_list, name='scheme_list'),
    path('rdCal', views.rdCal, name='rdCal'),
    path('fdCal', views.fdCal, name='fdCal'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
