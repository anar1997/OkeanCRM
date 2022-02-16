from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from mehsullar.models import Emeliyyat, Hediyye, Muqavile, OdemeTarix, Anbar, Mehsullar, AnbarQeydler, Servis, Stok
from account.models import Musteri, Shirket, Shobe, User, Vezifeler, Ofis, MusteriQeydler, Komanda


class ShirketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shirket
        fields = "__all__"

    def create(self, validated_data):
        shirket_adi = validated_data.get('shirket_adi')
        validated_data['shirket_adi'] = shirket_adi.upper()
        try:
            return super(ShirketSerializer, self).create(validated_data)
        except:
            raise ValidationError('Bu ad ilə şirkət artıq qeydiyyatdan keçirilib')


class KomandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Komanda
        fields = "__all__"

    def create(self, validated_data):
        komanda_adi = validated_data.get('komanda_adi')
        validated_data['komanda_adi'] = komanda_adi.upper()
        try:
            return super(KomandaSerializer, self).create(validated_data)
        except:
            raise ValidationError('Bu ad ilə komanda artıq qeydiyyatdan keçirilib')



class OfisSerializer(serializers.ModelSerializer):
    shirket = ShirketSerializer(read_only=True)
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket', write_only=True
    )

    class Meta:
        model = Ofis
        fields = "__all__"

    def create(self, validated_data):
        ofis_adi = validated_data.get('ofis_adi')
        validated_data['ofis_adi'] = ofis_adi.upper()
        try:
            return super(OfisSerializer, self).create(validated_data)
        except:
            raise ValidationError('Bu ad ilə ofis artıq qeydiyyatdan keçirilib')


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


class ShobeSerializer(serializers.ModelSerializer):
    ofis = OfisSerializer(read_only=True)
    ofis_id = serializers.PrimaryKeyRelatedField(
        queryset=Ofis.objects.all(), source='ofis', write_only=True
    )

    class Meta:
        model = Shobe
        fields = "__all__"

class VezifelerSerializer(serializers.ModelSerializer):
    shobe = ShobeSerializer(read_only=True)
    shirket = ShirketSerializer(read_only=True)
    shobe_id = serializers.PrimaryKeyRelatedField(
        queryset=Shobe.objects.all(), source='shobe', write_only=True
    )
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket', write_only=True
    )
    class Meta:
        model = Vezifeler
        fields = "__all__"

    def create(self, validated_data):
        vezife_adi = validated_data.get('vezife_adi')
        validated_data['vezife_adi'] = vezife_adi.upper()
        return super(VezifelerSerializer, self).create(validated_data)

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'asa', 'maas', 'dogum_tarixi', 'tel1', 'tel2',
                  'sv_image', 'shirket', 'ofis', 'vezife', 'komanda', 'shobe', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], password=validated_data['password'],
                                        asa=validated_data['asa'], maas=validated_data['maas'], dogum_tarixi=validated_data['dogum_tarixi'], tel1=validated_data['tel1'], tel2=validated_data['tel2'], sv_image=validated_data['sv_image'], shirket=validated_data['shirket'], ofis=validated_data['ofis'], vezife=validated_data['vezife'], komanda=validated_data['komanda'], shobe=validated_data['shobe'])
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
    class Meta:
        model = Musteri
        fields = "__all__"

class HediyyeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hediyye
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
    hediyye1 = HediyyeSerializer(read_only=True)
    hediyye2 = HediyyeSerializer(read_only=True)
    hediyye3 = HediyyeSerializer(read_only=True)

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

    hediyye1_id = serializers.PrimaryKeyRelatedField(
        queryset=Hediyye.objects.all(), source='hediyye1', write_only=True, required=False, allow_null=True
    )

    hediyye2_id = serializers.PrimaryKeyRelatedField(
        queryset=Hediyye.objects.all(), source='hediyye2', write_only=True, required=False, allow_null=True
    )

    hediyye3_id = serializers.PrimaryKeyRelatedField(
        queryset=Hediyye.objects.all(), source='hediyye3', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Muqavile
        fields = "__all__"


class OdemeTarixSerializer(serializers.ModelSerializer):
    muqavile = MuqavileSerializer(read_only=True)
    muqavile_id = serializers.PrimaryKeyRelatedField(
        queryset=Muqavile.objects.all(), source='muqavile', write_only=True
    )

    class Meta:
        model = OdemeTarix
        fields = "__all__"

class MusteriQeydlerSerializer(serializers.ModelSerializer):
    musteri = MusteriSerializer(read_only=True)

    musteri_id = serializers.PrimaryKeyRelatedField(
        queryset=MusteriQeydler.objects.all(), source='musteri', write_only=True
    )
    class Meta:
        model = MusteriQeydler
        fields = "__all__"

class ServisSerializer(serializers.ModelSerializer):
    muqavile = MuqavileSerializer(read_only=True)
    kartric1 = MehsullarSerializer(read_only=True)
    kartric2 = MehsullarSerializer(read_only=True)
    kartric3 = MehsullarSerializer(read_only=True)
    kartric4 = MehsullarSerializer(read_only=True)
    kartric5 = MehsullarSerializer(read_only=True)
    kartric6 = MehsullarSerializer(read_only=True)

    muqavile_id = serializers.PrimaryKeyRelatedField(
        queryset=Muqavile.objects.all(), source='muqavile', write_only=True
    )
    kartric1_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source='kartric1', write_only=True
    )
    kartric2_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source='kartric2', write_only=True
    )
    kartric3_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source='kartric3', write_only=True
    )
    kartric4_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source='kartric4', write_only=True
    )
    kartric5_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source='kartric5', write_only=True
    )
    kartric6_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source='kartric6', write_only=True
    )

    class Meta:
        model = Servis
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