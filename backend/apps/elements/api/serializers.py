from rest_framework import fields, serializers
# Models
from apps.elements.models import Category, Element, Type


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'


class ElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Element
        fields = '__all__'
    

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'
    
