from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
# Serializers
from apps.elements.api.serializers import TypeSerializer, CategorySerializer, ElementSerializer
# Models
from apps.elements.models import Type, Category, Element


class TypeViewSet(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
    
    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Element.objects.filter(type__id=pk)
        serializer = ElementSerializer(queryset, many=True)
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message' : 'Ningun elemento de este Tipo :c'}, status=status.HTTP_202_ACCEPTED)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()   

    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Element.objects.filter(category__id=pk)
        serializer = ElementSerializer(queryset, many=True)
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message' : 'Ningun elemento en esta Categoria :c'}, status=status.HTTP_202_ACCEPTED)


class ElementViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category__description', 'type__description']
    lookup_field = 'slug'
    queryset = Element.objects.all()
    search_fields = ['description']
    serializer_class = ElementSerializer
