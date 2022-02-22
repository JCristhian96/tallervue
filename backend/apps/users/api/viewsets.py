from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# Models
from apps.users.models import User
# Serializers
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
    @action(detail=True, methods=['get'])
    def details(self, request, pk):
        queryset = get_object_or_404(User, pk=pk)
        serializer = serializers.BiographySerializer(queryset.biography)
        return Response(data=serializer.data)