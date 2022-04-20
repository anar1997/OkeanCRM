from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from mehsullar.models import Emeliyyat, MuqavileHediyye, Muqavile, OdemeTarix, Anbar, Mehsullar, AnbarQeydler, Servis, ServisOdeme, Stok

from account.models import (
    User, 
    Musteri,
)

from api.v1.all_serializers.company_serializers import (
    ShirketSerializer,
    OfisSerializer,
    ShobeSerializer,
)

from api.v1.all_serializers.account_serializers import (
    UserSerializer,
    MusteriSerializer
)

from company.models import (
    Shirket,
    Ofis,
    Shobe,
)

class AnbarSerializer(serializers.ModelSerializer):
    shirket = ShirketSerializer(read_only=True)
    ofis = OfisSerializer(read_only=True)
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket', write_only=True
    )
    ofis_id = serializers.PrimaryKeyRelatedField(
        queryset=Ofis.objects.all(), source='ofis', write_only=True
    )

    class Meta:
        model = Anbar
        fields = "__all__"

    def create(self, validated_data):
        ad = validated_data.get('ad')
        validated_data['ad'] = ad.upper()
        try:
            return super(AnbarSerializer, self).create(validated_data)
        except:
            raise ValidationError('Bu ad ilə anbar artıq qeydiyyatdan keçirilib')


class MehsullarSerializer(serializers.ModelSerializer):
    shirket = ShirketSerializer(read_only = True)
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset = Shirket.objects.all(), source = "shirket", write_only= True
    )
    class Meta:
        model = Mehsullar
        fields = "__all__"

    def create(self, validated_data):
        mehsulun_adi = validated_data.get('mehsulun_adi')
        validated_data['mehsulun_adi'] = mehsulun_adi.upper()
        try:
            return super(MehsullarSerializer, self).create(validated_data)
        except:
            raise ValidationError('Bu ad ilə məhsul artıq qeydiyyatdan keçirilib')


class EmeliyyatSerializer(serializers.ModelSerializer):
    gonderen = AnbarSerializer(read_only=True)
    qebul_eden = AnbarSerializer(read_only=True)
    gonderilen_mehsul = MehsullarSerializer(read_only=True)

    gonderen_id = serializers.PrimaryKeyRelatedField(
        queryset=Anbar.objects.all(), source="gonderen", write_only=True
    )
    qebul_eden_id = serializers.PrimaryKeyRelatedField(
        queryset=Anbar.objects.all(), source="qebul_eden", write_only=True
    )

    gonderilen_mehsul_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source="gonderilen_mehsul", write_only=True
    )

    class Meta:
        model = Emeliyyat
        fields = "__all__"

class AnbarQeydlerSerializer(serializers.ModelSerializer):
    anbar = AnbarSerializer(read_only=True)
    anbar_id = serializers.PrimaryKeyRelatedField(
        queryset=Anbar.objects.all(), source='anbar', write_only=True
    )

    class Meta:
        model = AnbarQeydler
        fields = "__all__"

class MuqavileSerializer(serializers.ModelSerializer):
    vanleader = UserSerializer(read_only=True)
    dealer = UserSerializer(read_only=True)
    canvesser = UserSerializer(read_only=True)
    musteri = MusteriSerializer(read_only=True)
    mehsul = MehsullarSerializer(read_only=True)
    shirket = ShirketSerializer(read_only=True)
    shobe = ShobeSerializer(read_only=True)
    ofis = OfisSerializer(read_only=True)

    vanleader_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='vanleader', write_only=True, required=False, allow_null=True
    )
    dealer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='dealer', write_only=True, required=False, allow_null=True
    )
    canvesser_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='canvesser', write_only=True, required=False, allow_null=True
    )
    musteri_id = serializers.PrimaryKeyRelatedField(
        queryset=Musteri.objects.all(), source='musteri', write_only=True, required=False, allow_null=True
    )
    mehsul_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source='mehsul', write_only=True, required=False, allow_null=True
    )
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket', write_only=True, required=False, allow_null=True
    )

    shobe_id = serializers.PrimaryKeyRelatedField(
        queryset=Shobe.objects.all(), source='shobe', write_only=True, required=False, allow_null=True
    )

    ofis_id = serializers.PrimaryKeyRelatedField(
        queryset=Ofis.objects.all(), source='ofis', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Muqavile
        fields = "__all__"
        read_only_fields = (
            'muqavile_umumi_mebleg', 
            'negd_odenis_gecikdirme', 
            'negd_odenis_1_status', 
            'negd_odenis_2_status',
            'ilkin_odenis_status',
            'qaliq_ilkin_odenis_status'
        )

class MuqavileHediyyeSerializer(serializers.ModelSerializer):
    mehsul = MehsullarSerializer(read_only=True)
    muqavile = MuqavileSerializer(read_only=True)

    mehsul_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source='mehsul', write_only=True,
    )

    muqavile_id = serializers.PrimaryKeyRelatedField(
        queryset=Muqavile.objects.all(), source='muqavile', write_only=True
    )

    class Meta:
        model = MuqavileHediyye
        fields = "__all__"


class OdemeTarixSerializer(serializers.ModelSerializer):
    muqavile = MuqavileSerializer(read_only=True)
    muqavile_id = serializers.PrimaryKeyRelatedField(
        queryset=Muqavile.objects.all(), source='muqavile', write_only=True
    )

    class Meta:
        model = OdemeTarix
        fields = "__all__"

class ServisSerializer(serializers.ModelSerializer):
    muqavile = MuqavileSerializer(read_only=True)
    mehsullar = MehsullarSerializer(read_only=True, many=True)

    muqavile_id = serializers.PrimaryKeyRelatedField(
        queryset=Muqavile.objects.all(), source='muqavile', write_only=True, required=False, allow_null=True
    )
    mehsullar_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source='mehsullar', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Servis
        fields = "__all__"

class ServisOdemeSerializer(serializers.ModelSerializer):
    servis = ServisSerializer(read_only=True)
    servis_id = serializers.PrimaryKeyRelatedField(
        queryset=Servis.objects.all(), source='servis', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = ServisOdeme
        fields = "__all__"


class StokSerializer(serializers.ModelSerializer):
    anbar = AnbarSerializer(read_only=True)
    mehsul = MehsullarSerializer(read_only=True)

    anbar_id = serializers.PrimaryKeyRelatedField(
        queryset=Anbar.objects.all(), source='anbar', write_only=True
    )

    mehsul_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source='mehsul', write_only=True
    )
    
    class Meta:
        model = Stok
        fields = "__all__" 

