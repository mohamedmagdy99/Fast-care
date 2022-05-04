from rest_framework import viewsets
from api.models import Blood, Hospital, Room, FindById, FindByClothe
from api.serializers import FindByClothesSerializer, FindByIdSerializer, BloodTypeSerializer, RoomSerializer, LoginSerializer, UserSerializer, HospitalSerializer
from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken


class HospitalList(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()


class BloodList(viewsets.ModelViewSet):
    serializer_class = BloodTypeSerializer

    def get_queryset(self):
        bloodtype = self.kwargs['type']
        return Blood.objects.filter(type=bloodtype)


class RoomList(viewsets.ModelViewSet):
    serializer_class = RoomSerializer

    def get_queryset(self):
        roomtype = self.kwargs['type']
        covid = self.kwargs['covid']
        return Room.objects.filter(type=roomtype).filter(available=True).filter(hospital__covid=covid)


class FindByIdList(viewsets.ModelViewSet):
    serializer_class = FindByIdSerializer

    def get_queryset(self):
        nid = self.kwargs['nid']
        name = self.kwargs['name']
        return FindById.objects.filter(national_id=nid).filter(name=name)


class FindByClotheList(viewsets.ModelViewSet):
    serializer_class = FindByClothesSerializer

    def get_queryset(self):
        date = self.kwargs['date']
        return FindByClothe.objects.filter(date_of_lost=date)


class SignInAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# class MainUser(generics.RetrieveAPIView):
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]
#     serializer_class = UserSerializer
#     def get_object(self):
#         return self.request.user
