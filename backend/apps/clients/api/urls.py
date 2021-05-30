from rest_framework import routers, urlpatterns
# ViewSets
from apps.clients.api import viewsets

router = routers.SimpleRouter()

router.register('natural', viewsets.NaturalViewSet)
router.register('juridica', viewsets.JuridicaViewSet)

urlpatterns = router.urls