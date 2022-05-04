from django.urls import path, include
from rest_framework import routers
from api import views
from api.views import SignInAPI
from knox import views as knox_views

router = routers.DefaultRouter()
router.register(r'blood/(?P<type>.+)',
                views.BloodList, basename='blood')
router.register(r'room/(?P<type>.+)/(?P<covid>.+)',
                views.RoomList, basename='room')
router.register(r'findbyid/(?P<nid>.+)/(?P<name>.+)',
                views.FindByIdList, basename='findbyid')
router.register(r'findbycl/(?P<date>.+)',
                views.FindByClotheList, basename='findbycl')
urlpatterns = [
    path('api/auth/', include('knox.urls')),
    path('api/auth/login', SignInAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name="knox-logout")
]

urlpatterns += router.urls
