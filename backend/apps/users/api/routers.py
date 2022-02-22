from rest_framework import routers
# ViewSets
from . import viewsets

router = routers.SimpleRouter()

router.register('users', viewsets.UserViewSet, basename="users")

urlpatterns = router.urls
