from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'blood/(?P<type>.+)', views.BloodList, basename='blood')
router.register(r'room/(?P<type>.+)', views.RoomList, basename='room')
urlpatterns = router.urls
