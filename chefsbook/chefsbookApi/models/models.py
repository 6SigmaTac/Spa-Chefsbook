from django.contrib.auth.models import User
from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=6, null=False)


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.PROTECT, related_name="orders")
    associatedStaff = models.ManyToManyField(User)
    isFinished = models.BooleanField(default=False)


class Menu(models.Model):
    name = models.CharField(max_length=16)
    speciePrice = models.IntegerField()

    def __str__(self):
        return self.name


class OrderPosition(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    amount = models.SmallIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions')
