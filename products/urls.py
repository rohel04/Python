import imp
from django.urls import path
from . import views as v

urlpatterns=[
    path('',v.index),
    path('add',v.add)
]