# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Expenses(models.Model):
    date = models.DateField('Date')
    total_sale = models.FloatField('Total Sale', blank=True,null=True, default=0)
    card1 = models.FloatField('Card Machine 1', blank=True,null=True , default=0)
    card2 = models.FloatField('Card Machine 2', blank=True,null=True , default=0)
    card3 = models.FloatField('Card Machine 3', blank=True,null=True , default=0)
    take_away = models.FloatField('Take Away', blank=True,null=True , default=0)
    meat = models.FloatField('Meat', blank=True,null=True , default=0)
    vegetables = models.FloatField('Vegetables', blank=True,null=True, default=0)
    fish = models.FloatField('Fish', blank=True,null=True , default=0)
    containers = models.FloatField('Containers', blank=True,null=True , default=0)
    beer = models.FloatField('Beer', blank=True,null=True , default=0)
    cash_carry = models.FloatField('Cash & Carry', blank=True,null=True , default=0)
    soft_drinks = models.FloatField('Soft Drinks', blank=True,null=True , default=0)
    credit = models.FloatField('Credit', blank=True,null=True , default=0)
    salary = models.FloatField('Salary', blank=True,null=True , default=0)
    miscellaneous = models.FloatField('Miscellaneous', blank=True,null=True , default=0)
    balance = models.FloatField('Balance', blank=True,null=True , default=0)

