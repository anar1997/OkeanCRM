from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from account.models import User
from api.v1.all_serializers.account_serializers import UserSerializer
from api.v1.all_serializers.company_serializers import HoldingSerializer, KomandaSerializer, OfisSerializer, ShirketSerializer, ShobeSerializer, VezifelerSerializer
from company.models import Holding, Komanda, Ofis, Shirket, Shobe, Vezifeler

from gunler.models import (
    HoldingGunler,
    IsciGunler,
    KomandaGunler,
    OfisGunler,
    ShirketGunler,
    ShobeGunler,
    VezifeGunler,
    HoldingIstisnaIsci
)

class HoldingGunlerSerializer(serializers.ModelSerializer):
    holding = HoldingSerializer(read_only=True)
    holding_id = serializers.PrimaryKeyRelatedField(
        queryset=Holding.objects.all(), source='holding', write_only=True
    )
    
    class Meta:
        model = HoldingGunler
        fields = "__all__"

class IsciGunlerSerializer(serializers.ModelSerializer):
    isci = UserSerializer(read_only=True)
    isci_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='isci', write_only=True,
    )
    
    class Meta:
        model = IsciGunler
        fields = "__all__"


class KomandaGunlerSerializer(serializers.ModelSerializer):
    komanda = KomandaSerializer(read_only=True)
    komanda_id = serializers.PrimaryKeyRelatedField(
        queryset=Komanda.objects.all(), source='komanda', write_only=True,
    )
    
    class Meta:
        model = KomandaGunler
        fields = "__all__"

class OfisGunlerSerializer(serializers.ModelSerializer):
    ofis = OfisSerializer(read_only=True)
    ofis_id = serializers.PrimaryKeyRelatedField(
        queryset=Ofis.objects.all(), source='ofis', write_only=True,
    )
    
    class Meta:
        model = OfisGunler
        fields = "__all__"

class ShirketGunlerSerializer(serializers.ModelSerializer):
    shirket = ShirketSerializer(read_only=True)
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket', write_only=True
    )
    
    class Meta:
        model = ShirketGunler
        fields = "__all__"

class ShobeGunlerSerializer(serializers.ModelSerializer):
    shobe = ShobeSerializer(read_only=True)
    shobe_id = serializers.PrimaryKeyRelatedField(
        queryset=Shobe.objects.all(), source='shobe', write_only=True
    )
    
    class Meta:
        model = ShobeGunler
        fields = "__all__"

class VezifeGunlerSerializer(serializers.ModelSerializer):
    vezife = VezifelerSerializer(read_only=True)
    vezife_id = serializers.PrimaryKeyRelatedField(
        queryset=Vezifeler.objects.all(), source='vezife', write_only=True,
    )
    
    class Meta:
        model = VezifeGunler
        fields = "__all__"

class HoldingIstisnaIsciSerializer(serializers.ModelSerializer):
    holding_gunler = HoldingGunlerSerializer(read_only=True)
    holding_gunler_id = serializers.PrimaryKeyRelatedField(
        queryset=HoldingGunler.objects.all(), source='holding_gunler', write_only=True,
    )
    
    class Meta:
        model = HoldingIstisnaIsci
        fields = "__all__"