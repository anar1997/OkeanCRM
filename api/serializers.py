from django.db.models import fields
from rest_framework import serializers
from mehsullar.models import Emeliyyat, Muqavile, Dates, Anbar, Kateqoriyalar, Mehsullar, AnbarQeydler
from account.models import Musteri, Shirket, Shobe, User, Vezifeler, Merkezler, MusteriQeydler

class MuqavileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Muqavile
        fields="__all__"

class DatesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dates
        fields="__all__"

class AnbarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Anbar
        fields="__all__"

class KateqoriyalarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Kateqoriyalar
        fields="__all__"

class MehsullarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mehsullar
        fields="__all__"


class MusteriSerializer(serializers.ModelSerializer):
    class Meta:
        model=Musteri
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"


class MerkezlerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Merkezler
        fields="__all__"

class VezifelerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vezifeler
        fields="__all__"

class AnbarQeydlerSerializer(serializers.ModelSerializer):
    class Meta:
        model=AnbarQeydler
        fields="__all__"

class MusteriQeydlerSerializer(serializers.ModelSerializer):
    class Meta:
        model=MusteriQeydler
        fields="__all__"

class ShirketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shirket
        fields="__all__"

class ShobeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shobe
        fields="__all__"

class EmeliyyatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emeliyyat
        fields="__all__"