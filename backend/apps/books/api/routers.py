from rest_framework import routers
# Viewsets
from apps.books.api import viewsets

router = routers.SimpleRouter()
router.register('books', viewsets.BookViewSet)

urlpatterns = router.urls
