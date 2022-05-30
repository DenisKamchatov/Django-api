from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet, GetProductsView, PartnersViewSet, GetPartnersView

router = DefaultRouter()
router.register('products', ProductsViewSet, )
router.register('partners', PartnersViewSet, )


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/products/filter', GetProductsView.as_view()),
    path('api/partners/filter', GetPartnersView.as_view()),
]
