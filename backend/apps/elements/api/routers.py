from rest_framework import routers
# ViewSets
from apps.elements.api import viewsets

router = routers.SimpleRouter()

router.register('types', viewsets.TypeViewSet)
router.register('categorys', viewsets.CategoryViewSet)
router.register('elements', viewsets.ElementViewSet)

urlpatterns = router.urls