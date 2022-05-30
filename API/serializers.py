from rest_framework.serializers import ModelSerializer
from .models import Partners, Products


class PartnersSerializer(ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'

class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'