from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include('apps.elements.api.urls')),
    path('api/v1.0/', include('apps.books.api.urls')),
    url('', TemplateView.as_view(template_name="index.html")),
]
