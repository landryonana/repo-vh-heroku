from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts import views
from . import views as hone_views

urlpatterns = [
    path('', hone_views.index, name="index_hone"),
    path('evangelisations/tu-dois-etre-sauver', views.tu_dois_etre_sauver, name="tu_dois_etre_sauver"),
    path('evangelisations/', include('accounts.urls', namespace='accounts')),
    path('evangelisations/remplissages/', include('remplissages.urls', namespace='rempl')),
    path('evangelisations/suivie/', include('suivie.urls', namespace='suivie')),
    path('evangelisations/rapport/', include('rapport.urls', namespace='rapport')),
    path('evangelisations/gallerie/', include('gallerie.urls', namespace='gallerie')),

    path('admin/', admin.site.urls),
]
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
