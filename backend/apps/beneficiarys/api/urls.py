from django.conf.urls import url
from django.urls.conf import path
from rest_framework import routers
# ViewSets
from apps.beneficiarys.api import viewsets

router = routers.SimpleRouter()

router.register('origin', viewsets.OriginViewSet)
router.register('beneficiario', viewsets.BeneficiarioViewSet)

urlpatterns = router.urls

urlpatterns += [
    path(
        'resume/',
        viewsets.OriginListAPIView.as_view(),
    )
]