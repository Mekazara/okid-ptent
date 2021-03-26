from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import prikazList, auth, createPrikaz, editPrikaz

urlpatterns = [
    path('prikazy/', prikazList, name='prikazy'),
    path('', auth, name='login'),
    path('login/', auth, name='login'),
    path('sozdat/', createPrikaz, name='create'),
    path('edit/<int:prikaz_id>', editPrikaz, name='edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
