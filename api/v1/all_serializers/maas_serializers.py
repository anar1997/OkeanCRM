from rest_framework import serializers
from account.models import IsciStatus, User
from api.v1.all_serializers.company_serializers import VezifelerSerializer
from company.models import Vezifeler
from mehsullar.models import Mehsullar
from api.v1.all_serializers.account_serializers import (
    IsciStatusSerializer, 
    UserSerializer,
)
from api.v1.all_serializers.muqavile_serializers import MehsullarSerializer
from maas.models import (
    Avans,
    Kesinti,
    Bonus,
    MaasGoruntuleme,
    MaasOde, 
    VanLeaderPrim, 
    DealerPrim, 
    OfficeLeaderPrim,
    CanvasserPrim
)

class MaasGoruntulemeSerializer(serializers.ModelSerializer):
    isci = UserSerializer(read_only=True)
    isci_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='isci', write_only=True
    )

    class Meta:
        model = MaasGoruntuleme
        fields = "__all__"

class AvansSerializer(serializers.ModelSerializer):
    isci = UserSerializer(read_only=True)
    isci_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='isci', write_only=True
    )

    class Meta:
        model = Avans
        fields = "__all__"

class KesintiSerializer(serializers.ModelSerializer):
    isci = UserSerializer(read_only=True)
    isci_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='isci', write_only=True
    )
    
    class Meta:
        model = Kesinti
        fields = "__all__"
        
class BonusSerializer(serializers.ModelSerializer):
    isci = UserSerializer(read_only=True)
    isci_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='isci', write_only=True
    )

    class Meta:
        model = Bonus
        fields = "__all__"

class MaasOdeSerializer(serializers.ModelSerializer):
    isci = UserSerializer(read_only=True)
    isci_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='isci', write_only=True
    )

    class Meta:
        model = MaasOde
        fields = "__all__"

class OfficeLeaderPrimSerializer(serializers.ModelSerializer):
    prim_status = IsciStatusSerializer(read_only=True)
    prim_status_id = serializers.PrimaryKeyRelatedField(
        queryset=IsciStatus.objects.all(), source="prim_status", write_only=True
    )

    mehsul = MehsullarSerializer(read_only=True)
    mehsul_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source="mehsul", write_only=True
    )

    vezife = VezifelerSerializer(read_only=True)
    vezife_id = serializers.PrimaryKeyRelatedField(
        queryset=Vezifeler.objects.all(), source="vezife", write_only=True
    )

    class Meta:
        model = OfficeLeaderPrim
        fields = "__all__"

class VanLeaderPrimSerializer(serializers.ModelSerializer):
    prim_status = IsciStatusSerializer(read_only=True)
    prim_status_id = serializers.PrimaryKeyRelatedField(
        queryset=IsciStatus.objects.all(), source="prim_status", write_only=True
    )

    mehsul = MehsullarSerializer(read_only=True)
    mehsul_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source="mehsul", write_only=True
    )

    vezife = VezifelerSerializer(read_only=True)
    vezife_id = serializers.PrimaryKeyRelatedField(
        queryset=Vezifeler.objects.all(), source="vezife", write_only=True
    )

    class Meta:
        model = VanLeaderPrim
        fields = "__all__"

class DealerPrimSerializer(serializers.ModelSerializer):
    prim_status = IsciStatusSerializer(read_only=True)
    prim_status_id = serializers.PrimaryKeyRelatedField(
        queryset=IsciStatus.objects.all(), source="prim_status", write_only=True
    )

    mehsul = MehsullarSerializer(read_only=True)
    mehsul_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source="mehsul", write_only=True
    )

    vezife = VezifelerSerializer(read_only=True)
    vezife_id = serializers.PrimaryKeyRelatedField(
        queryset=Vezifeler.objects.all(), source="vezife", write_only=True
    )

    class Meta:
        model = DealerPrim
        fields = "__all__"

class CanvasserPrimSerializer(serializers.ModelSerializer):
    prim_status = IsciStatusSerializer(read_only=True)
    prim_status_id = serializers.PrimaryKeyRelatedField(
        queryset=IsciStatus.objects.all(), source="prim_status", write_only=True
    )

    mehsul = MehsullarSerializer(read_only=True)
    mehsul_id = serializers.PrimaryKeyRelatedField(
        queryset=Mehsullar.objects.all(), source="mehsul", write_only=True
    )

    vezife = VezifelerSerializer(read_only=True)
    vezife_id = serializers.PrimaryKeyRelatedField(
        queryset=Vezifeler.objects.all(), source="vezife", write_only=True
    )

    class Meta:
        model = CanvasserPrim
        fields = "__all__"