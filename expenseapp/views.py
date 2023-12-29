from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import *
from .serializers import *
from rest_framework import status
from django.db.models import Q
from django.db.models import Sum


# Create your views here.

class ExpenseView(APIView):
    def get(self, request):
        expense_items = Expense.objects.all()
        serializer = ExpenseSerializer(expense_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data.get('name')
        amount = request.data.get('amount')
        category = request.data.get('category')
        Expense.objects.create(name=name, amount=amount, category=category)
        response_data = {"response": "item Created"}
        return Response(response_data, status=status.HTTP_200_OK)

    def put(self, request, id):
        item = Expense.objects.filter(id=id).first()
        if item is None:
            response_data = {"response": "Item doesnot exists"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        ExpenseSerializer(data=request.data, instance=item)
        if ExpenseSerializer.is_valid():
            ExpenseSerializer.save()
            response_data = {"response": "item Updated"}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            pass

    def delete(self, request, id):
        item = Expense.objects.filter(id=id).first()
        item.delete()
        response_data = {"response": "item Deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

    def get(self, request, year, month):
        daily_expense = Expense.objects.filter(
            Q(updated_at__year=year) & Q(updated_at__month=month))
        serializer = ExpenseSerializer(daily_expense, many=True)
        return Response(serializer.data)

    def get(self, request):
        total_salary = 50000
        total_expense = Expense.objects.aggregate(Sum('amount'))
        remaining_amount = total_salary - total_expense
        return Response({"total_salary": total_salary, 'total_expense': total_expense, "remaining_amount": remaining_amount})
