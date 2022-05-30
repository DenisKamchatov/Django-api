from rest_framework.viewsets import ModelViewSet
from .serializers import PartnersSerializer, ProductsSerializer
from .models import Products, Partners
from rest_framework.generics import ListAPIView 
import django_filters.rest_framework
from django.db.models import Q

class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class GetProductsView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['amount','price','delivery']


class PartnersViewSet(ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class GetPartnersView(ListAPIView):
    queryset = Partners.objects.filter( Q(reviews__gt=7) | Q(reviews='0') )
    serializer_class = PartnersSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['reviews']

# @action(methods=['GET'], detail=False)
# def get_data(self, request, **kwargs):
#     data = Partners.objects
    # print(data)
    # data['info'] = 'тут можем вернуть какие-то данные'
    # return Response(data)