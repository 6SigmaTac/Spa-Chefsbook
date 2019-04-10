from django.contrib.auth.models import Group, User
from rest_framework import viewsets

from chefsbook.chefsbookApi.models.models import Table, OrderPosition, Order
from chefsbook.chefsbookApi.serializers import UserSerializer, GroupSerializer, TableSerializer, \
    OrderPositionSerializer, OrderSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class OrderPositionViewSet(viewsets.ModelViewSet):
    queryset = OrderPosition.objects.all()
    serializer_class = OrderPositionSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
