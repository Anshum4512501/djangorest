from django.shortcuts import render
from rest_framework import viewsets
from .models import Activity,Manager,Throttle
from .serializers import ActivitySerializers,ManagerSerializers,ThrottleSerializers
# Create your views here.


class ActivityView(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializers
class ManagerView(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializers
class ThrottleView(viewsets.ModelViewSet):
    queryset = Throttle.objects.all()
    serializer_class = ThrottleSerializers