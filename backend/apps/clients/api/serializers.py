from rest_framework import serializers
# Models
from apps.clients.models import Natural, Juridica


class NaturalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Natural
        fields = "__all__"
    

class JuridicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juridica
        fields = "__all__"
    
