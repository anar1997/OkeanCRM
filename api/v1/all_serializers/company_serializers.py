from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from account.models import (
    User
)

from company.models import (
    Holding,
    HoldingKassa,
    HoldingKassaMedaxil,
    HoldingKassaMexaric,
    HoldingdenShirketlereTransfer,
    OfisKassaMedaxil,
    OfisKassaMexaric,

    Shirket,
    ShirketKassa,
    ShirketKassaMedaxil,
    ShirketKassaMexaric,
    ShirketdenHoldingeTransfer,
    ShirketdenOfislereTransfer,

    Ofis,
    OfisKassa,
    OfisdenShirketeTransfer,

    Komanda,
    Shobe,
    Vezifeler,
    MuqavileKreditor
)
from mehsullar.models import Muqavile


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
            k = Komanda.objects.filter(komanda_adi=komanda_adi.upper(), is_active=True)
            if len(k) > 0:
                raise ValidationError
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
        shirket = validated_data['shirket']
        print(f"{shirket=}")
        try:
            ofiss = Ofis.objects.filter(ofis_adi=ofis_adi.upper(), shirket=shirket)
            print(f"{ofiss=}")
            if len(ofiss)>0:
                raise ValidationError
            return super(OfisSerializer, self).create(validated_data)
        except:
            raise ValidationError({"detail": 'Bu ad ilə ofis artıq qeydiyyatdan keçirilib'})


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


class HoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holding
        fields = "__all__"

    def create(self, validated_data):
        holding_adi = validated_data.get('holding_adi')
        validated_data['holding_adi'] = holding_adi.upper()
        try:
            return super(HoldingSerializer, self).create(validated_data)
        except:
            raise ValidationError('Bu ad ilə holding artıq qeydiyyatdan keçirilib')


class HoldingKassaSerializer(serializers.ModelSerializer):
    holding = HoldingSerializer(read_only=True)
    holding_id = serializers.PrimaryKeyRelatedField(
        queryset=Holding.objects.all(), source='holding', write_only=True
    )

    class Meta:
        model = HoldingKassa
        fields = "__all__"


class ShirketKassaSerializer(serializers.ModelSerializer):
    shirket = ShirketSerializer(read_only=True)
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset=Shirket.objects.all(), source='shirket', write_only=True
    )

    class Meta:
        model = ShirketKassa
        fields = "__all__"


class OfisKassaSerializer(serializers.ModelSerializer):
    ofis = OfisSerializer(read_only=True)
    ofis_id = serializers.PrimaryKeyRelatedField(
        queryset=Ofis.objects.all(), source='ofis', write_only=True
    )

    class Meta:
        model = OfisKassa
        fields = "__all__"


class HoldingdenShirketlereTransferSerializer(serializers.ModelSerializer):
    transfer_eden = serializers.StringRelatedField()
    transfer_eden_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='transfer_eden', write_only=True, required=False, allow_null=True
    )
    holding_kassa = HoldingKassaSerializer(read_only=True)
    holding_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=HoldingKassa.objects.all(), source='holding_kassa', write_only=True
    )

    shirket_kassa = ShirketKassaSerializer(read_only=True, many=True)
    shirket_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=ShirketKassa.objects.all(), source='shirket_kassa', many=True, write_only=True
    )

    class Meta:
        model = HoldingdenShirketlereTransfer
        fields = "__all__"


class ShirketdenHoldingeTransferSerializer(serializers.ModelSerializer):
    transfer_eden = serializers.StringRelatedField()
    transfer_eden_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='transfer_eden', write_only=True, required=False, allow_null=True
    )
    shirket_kassa = ShirketKassaSerializer(read_only=True)
    shirket_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=ShirketKassa.objects.all(), source='shirket_kassa', write_only=True
    )

    holding_kassa = HoldingKassaSerializer(read_only=True)
    holding_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=HoldingKassa.objects.all(), source='holding_kassa', write_only=True
    )

    class Meta:
        model = ShirketdenHoldingeTransfer
        fields = "__all__"


class OfisdenShirketeTransferSerializer(serializers.ModelSerializer):
    transfer_eden = serializers.StringRelatedField()
    transfer_eden_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='transfer_eden', write_only=True, required=False, allow_null=True
    )
    ofis_kassa = OfisKassaSerializer(read_only=True)
    ofis_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=OfisKassa.objects.all(), source='ofis_kassa', write_only=True
    )
    shirket_kassa = ShirketKassaSerializer(read_only=True)
    shirket_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=ShirketKassa.objects.all(), source='shirket_kassa', write_only=True
    )

    class Meta:
        model = OfisdenShirketeTransfer,
        fields = "__all__"


class ShirketdenOfislereTransferSerializer(serializers.ModelSerializer):
    transfer_eden = serializers.StringRelatedField()
    transfer_eden_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='transfer_eden', write_only=True, required=False, allow_null=True
    )
    shirket_kassa = ShirketKassaSerializer(read_only=True)
    shirket_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=ShirketKassa.objects.all(), source='shirket_kassa', write_only=True
    )

    ofis_kassa = OfisKassaSerializer(read_only=True, many=True)
    ofis_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=OfisKassa.objects.all(), source='ofis_kassa', many=True,  write_only=True
    )

    class Meta:
        model = ShirketdenOfislereTransfer
        fields = "__all__"


class HoldingKassaMedaxilSerializer(serializers.ModelSerializer):
    medaxil_eden = serializers.StringRelatedField()
    medaxil_eden_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='medaxil_eden', write_only=True, required=False, allow_null=True
    )
    holding_kassa = HoldingKassaSerializer(read_only=True)
    holding_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=HoldingKassa.objects.all(), source='holding_kassa', write_only=True
    )

    class Meta:
        model = HoldingKassaMedaxil
        fields = "__all__"


class HoldingKassaMexaricSerializer(serializers.ModelSerializer):
    mexaric_eden = serializers.StringRelatedField()
    mexaric_eden_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='mexaric_eden', write_only=True, required=False, allow_null=True
    )
    holding_kassa = HoldingKassaSerializer(read_only=True)
    holding_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=HoldingKassa.objects.all(), source='holding_kassa', write_only=True
    )

    class Meta:
        model = HoldingKassaMexaric
        fields = "__all__"


class ShirketKassaMedaxilSerializer(serializers.ModelSerializer):
    medaxil_eden = serializers.StringRelatedField()
    medaxil_eden_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='medaxil_eden', write_only=True, required=False, allow_null=True
    )
    shirket_kassa = ShirketKassaSerializer(read_only=True)
    shirket_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=ShirketKassa.objects.all(), source='shirket_kassa', write_only=True
    )

    class Meta:
        model = ShirketKassaMedaxil
        fields = "__all__"


class ShirketKassaMexaricSerializer(serializers.ModelSerializer):
    mexaric_eden = serializers.StringRelatedField()
    mexaric_eden_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='mexaric_eden', write_only=True, required=False, allow_null=True
    )
    shirket_kassa = ShirketKassaSerializer(read_only=True)
    shirket_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=ShirketKassa.objects.all(), source='shirket_kassa', write_only=True
    )

    class Meta:
        model = ShirketKassaMexaric
        fields = "__all__"


class OfisKassaMedaxilSerializer(serializers.ModelSerializer):
    medaxil_eden = serializers.StringRelatedField()
    medaxil_eden_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='medaxil_eden', write_only=True, required=False, allow_null=True
    )
    ofis_kassa = OfisKassaSerializer(read_only=True)
    ofis_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=OfisKassa.objects.all(), source='ofis_kassa', write_only=True
    )

    class Meta:
        model = OfisKassaMedaxil
        fields = '__all__'


class OfisKassaMexaricSerializer(serializers.ModelSerializer):
    mexaric_eden = serializers.StringRelatedField()
    mexaric_eden_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='mexaric_eden', write_only=True, required=False, allow_null=True
    )
    ofis_kassa = OfisKassaSerializer(read_only=True)
    ofis_kassa_id = serializers.PrimaryKeyRelatedField(
        queryset=OfisKassa.objects.all(), source='ofis_kassa', write_only=True
    )

    class Meta:
        model = OfisKassaMexaric
        fields = '__all__'

class MuqavileKreditorSerializer(serializers.ModelSerializer):
    muqavile = serializers.StringRelatedField()
    muqavile_id = serializers.PrimaryKeyRelatedField(
        queryset=Muqavile.objects.all(), source='muqavile', write_only=True
    )
    kreditor = serializers.StringRelatedField()
    kreditor_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='kreditor', write_only=True
    )
    class Meta:
        model = MuqavileKreditor
        fields = '__all__'