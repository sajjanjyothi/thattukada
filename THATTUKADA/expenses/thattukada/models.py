# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Expenses(models.Model):
    date = models.DateField('Date')
    total_sale = models.FloatField('Total Sale', blank=True,null=True)
    card1 = models.FloatField('Card Machine 1', blank=True,null=True)
    card2 = models.FloatField('Card Machine 2', blank=True,null=True)
    card3 = models.FloatField('Card Machine 3', blank=True,null=True)
    take_away = models.FloatField('Take Away', blank=True,null=True)
    meat = models.FloatField('Meat', blank=True,null=True)
    vegetables = models.FloatField('Vegetables', blank=True,null=True)
    fish = models.FloatField('Fish', blank=True,null=True)
    containers = models.FloatField('Containers', blank=True,null=True)
    beer = models.FloatField('Beer', blank=True,null=True)
    cash_carry = models.FloatField('Cash & Carry', blank=True,null=True)
    soft_drinks = models.FloatField('Soft Drinks', blank=True,null=True)
    credit = models.FloatField('Credit', blank=True,null=True)
    salary = models.FloatField('Salary', blank=True,null=True)
    miscellaneous = models.FloatField('Miscellaneous', blank=True,null=True)
    balance = models.FloatField('Balance', blank=True,null=True)

