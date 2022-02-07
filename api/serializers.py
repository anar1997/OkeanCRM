from rest_framework import serializers
from mehsullar.models import Emeliyyat, Hediyye, Muqavile, Dates, Anbar, Mehsullar, AnbarQeydler, Servis
from account.models import Musteri, Shirket, Shobe, User, Vezifeler, Merkezler, MusteriQeydler, Komanda


class ShirketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shirket
        fields = "__all__"


class KomandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Komanda
        fields = "__all__"


class MerkezlerSerializer(serializers.ModelSerializer):
    shirket = ShirketSerializer(read_only=True)
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket', write_only=True
    )

    class Meta:
        model = Merkezler
        fields = "__all__"


class AnbarSerializer(serializers.ModelSerializer):
    shirket = ShirketSerializer(read_only=True)
    merkez = MerkezlerSerializer(read_only=True)
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket', write_only=True
    )
    merkez_id = serializers.PrimaryKeyRelatedField(
        queryset=Merkezler.objects.all(), source='merkez', write_only=True
    )

    class Meta:
        model = Anbar
        fields = "__all__"


class MehsullarSerializer(serializers.ModelSerializer):
    anbar = AnbarSerializer(read_only=True)
    shirket = ShirketSerializer(read_only=True)
    anbar_id = serializers.PrimaryKeyRelatedField(
        queryset=Anbar.objects.all(), source='anbar',
        write_only=True
    )
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket',
        write_only=True
    )

    class Meta:
        model = Mehsullar
        fields = "__all__"


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
    merkez = MerkezlerSerializer(read_only=True)
    merkez_id = serializers.PrimaryKeyRelatedField(
        queryset=Merkezler.objects.all(), source='merkez', write_only=True
    )

    class Meta:
        model = Shobe
        fields = "__all__"


class VezifelerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vezifeler
        fields = "__all__"


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
    ofis = MerkezlerSerializer(read_only=True)
    shobe = ShobeSerializer(read_only=True)
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket', write_only=True, required=False, allow_null=True
    )
    ofis_id = serializers.PrimaryKeyRelatedField(
        queryset=Merkezler.objects.all(), source='ofis', write_only=True, required=False, allow_null=True
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


class ShobeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shobe
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


class DatesSerializer(serializers.ModelSerializer):
    muqavile = MuqavileSerializer(read_only=True)
    muqavile_id = serializers.PrimaryKeyRelatedField(
        queryset=Muqavile.objects.all(), source='muqavile', write_only=True
    )

    class Meta:
        model = Dates
        fields = "__all__"


class VezifelerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vezifeler
        fields = "__all__"


class MusteriQeydlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusteriQeydler
        fields = "__all__"

class ServisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servis
        fields = "__all__"