from rest_framework import routers
from django.urls import path,include
from . import views
router = routers.DefaultRouter()
router.register('activity',viewset=views.ActivityView)
router.register('manager',viewset=views.ManagerView)
router.register('throttle',viewset=views.ThrottleView)
urlpatterns = [
    path ('',include(router.urls))
]