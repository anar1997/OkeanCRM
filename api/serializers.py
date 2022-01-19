from django.db.models import fields, query
from rest_framework import serializers
from mehsullar.models import Emeliyyat, Hediyye, Muqavile, Dates, Anbar, Mehsullar, AnbarQeydler
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
    anbar=AnbarSerializer(read_only=True)
    shirket=ShirketSerializer(read_only=True)
    anbar_id=serializers.PrimaryKeyRelatedField(
        queryset=Anbar.objects.all(), source='anbar', 
        write_only=True
    )
    shirket_id=serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket',
        write_only=True
    )
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
    anbar=AnbarSerializer(read_only=True)
    anbar_id=serializers.PrimaryKeyRelatedField(
        queryset=Anbar.objects.all(), source='anbar', write_only=True
    )
    class Meta:
        model=AnbarQeydler
        fields="__all__"

class ShobeSerializer(serializers.ModelSerializer):
    merkez=MerkezlerSerializer(read_only=True)
    merkez_id=serializers.PrimaryKeyRelatedField(
        queryset=Merkezler.objects.all(), source='merkez', write_only=True
    )
    class Meta:
        model=Shobe
        fields="__all__"

class VezifelerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vezifeler
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    shirket=ShirketSerializer(read_only=True)
    ofis=MerkezlerSerializer(read_only=True)
    shobe=ShobeSerializer(read_only=True)
    shirket_id=serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket', write_only=True
    )
    ofis_id=serializers.PrimaryKeyRelatedField(
        queryset=Merkezler.objects.all(), source='ofis', write_only=True
    )
    shobe_id=serializers.PrimaryKeyRelatedField(
        queryset=Shobe.objects.all(), source='shobe',
        write_only=True
    )

    vezife = VezifelerSerializer(read_only = True)
    vezife_id=serializers.PrimaryKeyRelatedField(
        queryset=Vezifeler.objects.all(), source='vezife', write_only=True
    )
    class Meta:
        model=User
        fields="__all__"

class MusteriSerializer(serializers.ModelSerializer):
    class Meta:
        model=Musteri
        fields="__all__"

class MuqavileSerializer(serializers.ModelSerializer):
    dealer=UserSerializer(read_only=True)
    canvesser=UserSerializer(read_only=True)
    musteri=MusteriSerializer(read_only=True)
    mehsul=MehsullarSerializer(read_only=True)
    shirket=ShirketSerializer(read_only=True)
    dealer_id=serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='dealer', write_only=True
    )
    canvesser_id=serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='canvesser', write_only=True
    )
    musteri_id=serializers.PrimaryKeyRelatedField(
        queryset=Musteri.objects.all(), source='muster', write_only=True
    )
    mehsul_id=serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source='mehsul', write_only=True
    )
    shirket_id=serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket', write_only=True
    )

    class Meta:
        model=Muqavile
        fields="__all__"

class DatesSerializer(serializers.ModelSerializer):
    muqavile=MuqavileSerializer(read_only=True)
    muqavile_id=serializers.PrimaryKeyRelatedField(
        queryset=Muqavile.objects.all(), source='muqavile', write_only=True
    )
    class Meta:
        model=Dates
        fields="__all__"

class HediyyeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hediyye
        fields="__all__"

# class Hediyye2Serializer(serializers.ModelSerializer):
#     class Meta:
#         model=Hediyye2
#         fields="__all__"

# class Hediyye3Serializer(serializers.ModelSerializer):
#     class Meta:
#         model=Hediyye3
#         fields="__all__"
# class KateqoriyalarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Kateqoriyalar
#         fields="__all__"


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
