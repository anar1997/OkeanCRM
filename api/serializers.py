from django.db.models import fields
from rest_framework import serializers
from mehsullar.models import Emeliyyat, Muqavile, Dates, Anbar, Kateqoriyalar, Mehsullar, AnbarQeydler
from account.models import Musteri, Shirket, Shobe, User, Vezifeler, Merkezler, MusteriQeydler


class ShirketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shirket
        fields="__all__"


class MerkezlerSerializer(serializers.ModelSerializer):
    shirket = ShirketSerializer(read_only=True)
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset = Shirket.objects.all(), source='shirket', write_only=True
    )
    class Meta:
        model=Merkezler
        fields="__all__"



class AnbarSerializer(serializers.ModelSerializer):
    shirket = ShirketSerializer(read_only=True)
    merkez=MerkezlerSerializer(read_only=True)
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset = Shirket.objects.all(), source='shirket', write_only=True
    )
    merkez_id = serializers.PrimaryKeyRelatedField(
        queryset = Merkezler.objects.all(), source='merkez', write_only=True
    )
    class Meta:
        model=Anbar
        fields="__all__"

class MehsullarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mehsullar
        fields="__all__"

class EmeliyyatSerializer(serializers.ModelSerializer):
    gonderen = AnbarSerializer(read_only=True)
    qebul_eden = AnbarSerializer(read_only=True)
    gonderilen_mehsul = MehsullarSerializer(read_only=True)

    gonderen_id = serializers.PrimaryKeyRelatedField(
        queryset=Anbar.objects.all(), source = "gonderen", write_only=True
    )
    qebul_eden_id = serializers.PrimaryKeyRelatedField(
        queryset=Anbar.objects.all(), source = "qebul_eden", write_only=True
    )

    gonderilen_mehsul_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source = "gonderilen_mehsul", write_only=True
    )
    class Meta:
        model=Emeliyyat
        fields="__all__"

class AnbarQeydlerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=AnbarQeydler
        fields="__all__"

class MuqavileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Muqavile
        fields="__all__"

class DatesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dates
        fields="__all__"

class KateqoriyalarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Kateqoriyalar
        fields="__all__"




class MusteriSerializer(serializers.ModelSerializer):
    class Meta:
        model=Musteri
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"




class VezifelerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vezifeler
        fields="__all__"



class MusteriQeydlerSerializer(serializers.ModelSerializer):
    class Meta:
        model=MusteriQeydler
        fields="__all__"



class ShobeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shobe
        fields="__all__"
