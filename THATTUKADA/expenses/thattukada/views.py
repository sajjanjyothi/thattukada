# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Expenses
from django.views.generic import ListView
from .forms import ExpenseForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
import csv
from django.http import HttpResponse

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
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.balance = expense.total_sale + expense.card1 + \
                                expense.card2 + \
                                expense.card3 + \
                                expense.take_away - \
                                expense.meat - \
                                expense.vegetables - \
                                expense.fish - \
                                expense.containers - \
                                expense.beer - \
                                expense.cash_carry - \
                                expense.soft_drinks - \
                                expense.credit - \
                                expense.salary - \
                                expense.miscellaneous 
            expense.save()
        return render(request,'index.html')
    else:   
        form = ExpenseForm()
        return render(request,'new.html',{'form':form})

def update(request,pk):
    expense = get_object_or_404(Expenses, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expenseData = form.save(commit=False)
            expense.balance = expense.total_sale + expense.card1 + \
                                expense.card2 + \
                                expense.card3 + \
                                expense.take_away - \
                                expense.meat - \
                                expense.vegetables - \
                                expense.fish - \
                                expense.containers - \
                                expense.beer - \
                                expense.cash_carry - \
                                expense.soft_drinks - \
                                expense.credit - \
                                expense.salary - \
                                expense.miscellaneous 
            expenseData.save()  
        listExpenses = Expenses.objects.order_by('-date')
        total = 0
        for expense in listExpenses:
            if expense.balance is not None:
                total = total + expense.balance
        return render(request,'list.html',{'expenses':listExpenses,'total':total})  
    else:
        form = ExpenseForm(instance=expense)
        return render(request,'update.html',{'form':form})

def delete(request,pk):
    expense = get_object_or_404(Expenses, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expenseData = form.save(commit=False)
            expenseData.delete()  
        listExpenses = Expenses.objects.order_by('-date')
        total = 0
        for expense in listExpenses:
            if expense.balance is not None:
                total = total + expense.balance
        return render(request,'list.html',{'expenses':listExpenses,'total':total})  
    else:
        form = ExpenseForm(instance=expense)
        return render(request,'delete.html',{'form':form})

def search(request):
    if request.method == "POST":
        fromdate = request.POST.get("fromdate", "")
        todate = request.POST.get("todate", "")
        if len(fromdate) == 0:
            messages.error(request, 'From date cannot be empty')
            return render(request,'list.html')
        if len(todate) == 0:
            messages.error(request, 'To date cannot be empty')
            return render(request,'list.html')
    listExpenses = Expenses.objects.filter(date__range=[fromdate, todate])
    total = 0
    for expense in listExpenses:
        if expense.balance is not None:
            total = total + expense.balance
    return render(request,'list.html',{'expenses':listExpenses,'total':total})


def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="expenses.csv"'
    writer = csv.writer(response)
    writer.writerow(['Date', 'Total Sale', 'Card Machine 1', 'Card Machine 2', 'Card Machine 3','Take Away','Meat','Vegetables','Fish','Containers',\
    'Beer','Cash & Carry','Soft Drinks','Credit','Salary','Miscellaneous','Balance'])
    expenses = Expenses.objects.all()
    for expense in expenses:
        writer.writerow([expense.date, expense.total_sale, expense.card1, expense.card2,expense.card3, expense.take_away, \
        expense.meat,expense.vegetables,expense.fish,expense.containers,\
        expense.beer, expense.cash_carry,expense.soft_drinks,expense.credit,\
        expense.salary,expense.miscellaneous,expense.balance])
    return response