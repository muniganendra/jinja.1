from django.urls import path
from app2.views import *

urlpatterns=[
    path('first/',first,name='first'),
]