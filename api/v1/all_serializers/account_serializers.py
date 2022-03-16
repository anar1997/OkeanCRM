from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from account.models import (
    IsciSatisSayi,
    MusteriQeydler, 
    User, 
    Musteri,
    Maas,
    Bonus,
    Bolge
)

from api.v1.all_serializers.company_serializers import (
    ShirketSerializer,
    OfisSerializer,
    ShobeSerializer,
    KomandaSerializer,
    VezifelerSerializer
)

from company.models import (
    Shirket,
    Ofis,
    Komanda,
    Shobe,
    Vezifeler
)


class BolgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolge
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'asa', 'dogum_tarixi', 'tel1', 'tel2',
                  'sv_image', 'shirket', 'status', 'ofis', 'vezife', 'komanda', 'shobe', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'],
                                        asa=validated_data['asa'], dogum_tarixi=validated_data['dogum_tarixi'], tel1=validated_data['tel1'], tel2=validated_data['tel2'], sv_image=validated_data['sv_image'], shirket=validated_data['shirket'], ofis=validated_data['ofis'], vezife=validated_data['vezife'], komanda=validated_data['komanda'], shobe=validated_data['shobe'])
        return user

class UserSerializer(serializers.ModelSerializer):
    shirket = ShirketSerializer(read_only=True)
    ofis = OfisSerializer(read_only=True)
    shobe = ShobeSerializer(read_only=True)
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket', write_only=True, required=False, allow_null=True
    )
    ofis_id = serializers.PrimaryKeyRelatedField(
        queryset=Ofis.objects.all(), source='ofis', write_only=True, required=False, allow_null=True
    )
    shobe_id = serializers.PrimaryKeyRelatedField(
        queryset=Shobe.objects.all(), source='shobe',
        write_only=True, required=False, allow_null=True
    )

    vezife = VezifelerSerializer(read_only=True)
    vezife_id = serializers.PrimaryKeyRelatedField(
        queryset=Vezifeler.objects.all(), source='vezife', write_only=True, required=False, allow_null=True
    )

    komanda = KomandaSerializer(read_only=True)
    komanda_id = serializers.PrimaryKeyRelatedField(
        queryset=Komanda.objects.all(), source='komanda', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = User
        fields = "__all__"

class MusteriSerializer(serializers.ModelSerializer):
    bolge = BolgeSerializer(read_only=True)
    bolge_id = serializers.PrimaryKeyRelatedField(
        queryset = Bolge.objects.all(), source = "bolge", write_only=True
    )
    class Meta:
        model = Musteri
        fields = "__all__"


class MusteriQeydlerSerializer(serializers.ModelSerializer):
    musteri = MusteriSerializer(read_only=True)

    musteri_id = serializers.PrimaryKeyRelatedField(
        queryset=MusteriQeydler.objects.all(), source='musteri', write_only=True
    )
    class Meta:
        model = MusteriQeydler
        fields = "__all__"

class MaasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maas
        fields = "__all__"

class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = "__all__"

class IsciSatisSayiSerializer(serializers.ModelSerializer):
    isci = UserSerializer(read_only=True)
    isci_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(), source='isci', write_only=True
    )
    class Meta:
        model = IsciSatisSayi
        fields = "__all__"