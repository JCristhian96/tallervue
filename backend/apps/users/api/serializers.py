from rest_framework import serializers
# Models
from apps.users.models import User, Biography


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        
        
class BiographySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Biography
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.email
        return data