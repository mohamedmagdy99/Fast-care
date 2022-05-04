from rest_framework import serializers
from api.models import Hospital, Room, FindByClothe, FindById, Blood
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['name',
                  'phone',
                  'longtitude',
                  'latitude',
                  'covid',
                  'id']


class RoomSerializer(serializers.ModelSerializer):
    hospital_name = serializers.CharField(
        source='hospital.name', read_only=True)
    hospital_longtitude = serializers.CharField(
        source='hospital.longtitude', read_only=True)
    hospital_latitude = serializers.CharField(
        source='hospital.latitude', read_only=True)
    hospital_phone = serializers.CharField(
        source='hospital.phone', read_only=True)

    class Meta:
        model = Room
        fields = ['number',
                  'price',
                  'type',
                  'available',
                  'hospital_name',
                  'hospital_phone',
                  'hospital_longtitude',
                  'hospital_latitude',
                  'hospital']
        extra_kwargs = {
            'hospital': {'write_only': True},
        }


class FindByClothesSerializer(serializers.ModelSerializer):
    hospital_name = serializers.CharField(
        source='hospital.name', read_only=True)
    hospital_phone = serializers.CharField(
        source='hospital.phone', read_only=True)

    class Meta:
        model = FindByClothe
        fields = ['shirt_color',
                  'hair_color',
                  'skin_color',
                  'height',
                  'date_of_lost',
                  'gender',
                  'case',
                  'reason',
                  'hospital_name',
                  'hospital_phone',
                  'hospital']
        extra_kwargs = {
            'hospital': {'write_only': True},
        }


class FindByIdSerializer(serializers.ModelSerializer):
    hospital_name = serializers.CharField(
        source='hospital.name', read_only=True)
    hospital_phone = serializers.CharField(
        source='hospital.phone', read_only=True)

    class Meta:
        model = FindById
        fields = ['name',
                  'national_id',
                  'date_of_lost',
                  'gender',
                  'case',
                  'reason',
                  'hospital_name',
                  'hospital_phone',
                  'hospital']
        extra_kwargs = {
            'hospital': {'write_only': True},
        }


class BloodTypeSerializer(serializers.ModelSerializer):

    hospital_name = serializers.CharField(
        source='hospital.name', read_only=True)
    hospital_longtitude = serializers.CharField(
        source='hospital.longtitude', read_only=True)
    hospital_latitude = serializers.CharField(
        source='hospital.latitude', read_only=True)
    hospital_phone = serializers.CharField(
        source='hospital.phone', read_only=True)

    class Meta:
        model = Blood
        fields = ['type',
                  'count',
                  'hospital_name',
                  'hospital_longtitude',
                  'hospital_latitude',
                  'hospital_phone',
                  'hospital']
        extra_kwargs = {
            'hospital': {'write_only': True},
        }


class UserSerializer(serializers.ModelSerializer):
    hospital_name = serializers.RelatedField(source='hospital', read_only=True)

    class Meta:
        model = User
        fields = ['username', 'hospital_name']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')
