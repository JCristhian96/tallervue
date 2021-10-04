from django.http import response
from django.utils.functional import empty
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
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
    serializer_class = ElementSerializer
    queryset = Element.objects.all()
