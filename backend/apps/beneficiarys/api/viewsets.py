from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# Models
from apps.beneficiarys.models import Origin, Beneficiario
# Serializers
from apps.beneficiarys.api.serializers import OriginSerializer, BeneficiarioSerializer, OriginResumeSerializer
# Pagination
from apps.beneficiarys.api.pagination import BeneficiarioPagination
# Functions
from apps.beneficiarys.functions import response_with_paginator


class OriginViewSet(viewsets.ModelViewSet):
    serializer_class = OriginSerializer
    queryset = Origin.objects.all()


class BeneficiarioViewSet(viewsets.ModelViewSet):
    serializer_class = BeneficiarioSerializer
    queryset = Beneficiario.objects.all()
    pagination_class = BeneficiarioPagination


    @action(detail=True, methods=['get'])
    def search(self, request, pk=None):
        queryset = Beneficiario.plus_objects.search(pk)
        if queryset.exists():
            return response_with_paginator(self, queryset)
        else:
            return Response({'message' : 'Ningun dato encontrado :c'}, status=status.HTTP_202_ACCEPTED)
        


class OriginListAPIView(ListAPIView):
    queryset = Origin.plus_objects.count()
    serializer_class = OriginResumeSerializer
    
    


    
   