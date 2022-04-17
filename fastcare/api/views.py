from rest_framework import viewsets
from api.models import Hospital, Blood, Room, HospitalUser, FindById, FindByClothe
from api.serializers import HospitalSerializer


class BloodList(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer

    def get_queryset(self):
        bloodtype = self.kwargs['type']
        return Hospital.objects.filter(blood__type=bloodtype)


class RoomList(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer

    def get_queryset(self):
        roomtype = self.kwargs['type']
        return Hospital.objects.filter(room__type=roomtype).filter(room__available=True)

