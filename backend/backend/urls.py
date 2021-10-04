from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include('apps.elements.api.urls')),
    path('api/v1.0/', include('apps.books.api.urls')),
    path('api/v1.0/', include('apps.clients.api.urls')),
    path('api/v1.0/', include('apps.beneficiarys.api.urls')),
    re_path(r"^(?!media).*$", TemplateView.as_view(template_name="index.html"), name="entry-point"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
