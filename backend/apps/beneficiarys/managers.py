from django.db import models
from django.db.models import Q, Count


class BeneficiarioManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()

    def search(self, search):
        if search:
            data = self.filter(
                Q(dni__icontains = search) |
                Q(names__icontains = search) |
                Q(origin__name__icontains = search)
            ).order_by(
                'names'
            )
        return data
    


class OriginManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()

    def count(self):
        return self.annotate(num = Count('beneficiario')).order_by('name')
    