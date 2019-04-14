from django.contrib.auth.models import User, Group
from rest_framework import serializers

from chefsbook.chefsbookApi.models.models import Table, OrderPosition, Order, Menu


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups', 'url')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'url')


class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = ('name', 'url', 'orders')
        read_only_fields = ('orders',)


class OrderPositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderPosition
        fields = ('menu', 'amount', 'url', 'order')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('table', 'positions', 'associatedStaff', 'url', 'isFinished')
        read_only_fields = ('positions',)
        # depth = 2


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('name', 'speciePrice', 'url')
