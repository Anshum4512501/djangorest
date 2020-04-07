from rest_framework import serializers
from .models import Languages,Paradigm,Programmer,Activity,Manager,Throttle


class ActivitySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('id','url','start_time','end_time_time')
class ManagerSerializers(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Manager
            
            fields = ('id','url','real_name','activity')
class ThrottleSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
            model = Throttle
            fields = ('id','url','ok','manager')
            depth = 2
