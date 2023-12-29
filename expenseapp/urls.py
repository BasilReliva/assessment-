from django.urls import path
from .views import *
from .models import *

urlpatterns=[
     path('expenses/', ExpenseView.as_view()),  
     path('expenses/<int:id>/',ExpenseView.as_view()), 
     path('expenses/month/<int:month>/<int:year>/',ExpenseView.as_view()) 
]