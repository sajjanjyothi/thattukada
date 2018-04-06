# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Expenses
from django.views.generic import ListView

# Create your views here.
def index(request):
    return render(request,'index.html')

def list(request):
    listExpenses = Expenses.objects.order_by('-date')
    total = 0
    for expense in listExpenses:
        if expense.balance is not None:
            total = total + expense.balance
    return render(request,'list.html',{'expenses':listExpenses,'total':total})

def newentry(request):
    return render(request,'new.html')

