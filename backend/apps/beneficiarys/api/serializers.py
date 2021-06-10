from rest_framework import serializers
# Models
from apps.beneficiarys.models import Origin, Beneficiario


class OriginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Origin
        exclude = ('created_at', )


class BeneficiarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Beneficiario
        exclude = ('created_at', )
    
    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'dni' : instance.dni,
            'names' : instance.names,
            'origin' : instance.origin.name,
        }


class OriginResumeSerializer(serializers.Serializer):
    name = serializers.CharField()
    num = serializers.IntegerField()