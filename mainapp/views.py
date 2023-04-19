from rest_framework.viewsets import ModelViewSet
from .models import Order, Tour
from rest_framework import permissions
from .serializers import OrderSerializer, TourSerializer


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    http_method_names = ['post', 'get']
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        order = Order(request.POST or None)
        if order.is_valid():
            new_order = order.save()


class TourView(ModelViewSet):
    queryset = Tour.objects.all()
    http_method_names = ['get']
    serializer_class = TourSerializer
    permission_classes = [permissions.AllowAny]