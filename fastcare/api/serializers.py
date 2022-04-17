from rest_framework import serializers
from api.models import Hospital, Room, FindByClothe, FindById, Blood


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['name',
                  'phone',
                  'longtitude',
                  'latitude',
                  'covid']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['number',
                  'price',
                  'type']


class FindByClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindByClothe
        fields = ['shirt_color',
                  'hair_color',
                  'skin_color',
                  'height']


class FindByIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindById
        fields = ['name',
                  'id']


class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blood
        fields = ['type',
                  'count']
