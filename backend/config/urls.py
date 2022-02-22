from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# Views
from django.views.generic import TemplateView

# API Rest Docs
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion API",
      default_version='v0.1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include('apps.beneficiarys.api.routers')),
    path('api/v1.0/', include('apps.books.api.routers')),
    path('api/v1.0/', include('apps.clients.api.routers')),
    path('api/v1.0/', include('apps.elements.api.routers')),
    path('api/v1.0/', include('apps.users.api.routers')),
    # VueJS
    re_path(r"^(?!media).*$", TemplateView.as_view(template_name="index.html"), name="entry-point"),
    # API Rest Docs
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Debug Toolbar
if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),