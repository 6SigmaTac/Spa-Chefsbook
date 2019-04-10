from django.contrib.auth.models import User
from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=6, null=False)


class OrderPosition(models.Model):
    name = models.CharField(max_length=16)
    amount = models.SmallIntegerField()


class Order(models.Model):
    table = models.OneToOneField(Table, on_delete=models.DO_NOTHING, null=True)
    positions = models.ManyToManyField(OrderPosition, related_name='orders')
    associatedStaff = models.ManyToManyField(User)
