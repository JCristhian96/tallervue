from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# Serializers
from apps.clients.api.serializers import NaturalSerializer, JuridicaSerializer
# Models
from apps.clients.models import Natural, Juridica


class NaturalViewSet(viewsets.ModelViewSet):
    serializer_class = NaturalSerializer
    queryset = Natural.objects.all()    

    @action(detail=True, methods=['get'])
    def search(self, request, pk=None):
        queryset = Natural.objects.filter(dni=pk)
        serializer = NaturalSerializer(queryset, many=True)
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message' : 'Ningun dato encontrado :c'}, status=status.HTTP_202_ACCEPTED)


class JuridicaViewSet(viewsets.ModelViewSet):
    serializer_class = JuridicaSerializer
    queryset = Juridica.objects.all()


    