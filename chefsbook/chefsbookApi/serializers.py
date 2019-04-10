from django.contrib.auth.models import User, Group
from rest_framework import serializers

from chefsbook.chefsbookApi.models.models import Table, OrderPosition, Order


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
        fields = ('name', 'url')


class OrderPositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderPosition
        fields = ('name', 'amount', 'url')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('table', 'positions', 'associatedStaff', 'url')
        # read_only_fields = ('table', 'positions')
        # depth = 2
