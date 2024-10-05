from . import views
from django.urls import path

urlpatterns = [
    path('', views.helloWorld, name='helloWorld'),
]
