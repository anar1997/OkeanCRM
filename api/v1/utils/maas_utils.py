import pandas as pd
from company.models import (
    Holding, 
    HoldingKassa, 
    HoldingKassaMedaxil, 
    HoldingKassaMexaric, 
    OfisKassa, 
    OfisKassaMedaxil, 
    OfisKassaMexaric, 
    ShirketKassa, 
    ShirketKassaMedaxil, 
    ShirketKassaMexaric
)
from maas.models import Bonus, Avans,Kesinti,MaasGoruntuleme
from api.v1.all_serializers.maas_serializers import AvansSerializer,KesintiSerializer,MaasGoruntulemeSerializer
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response
import datetime

def bonus_create(self, request, *args, **kwargs):
    """
    İşçilərə bonus vermək funksiyası
    """
    serializer = self.get_serializer(data=request.data)
    user = self.request.user
    print(f"login olan user ==> {user}")
    if serializer.is_valid():
        isci = serializer.validated_data.get("isci")
        print(f"{isci=}")
        mebleg = serializer.validated_data.get("mebleg")
        print(f"{mebleg=}")
        qeyd = serializer.validated_data.get("qeyd")
        print(f"{qeyd=}")
        bonus_tarixi = serializer.validated_data.get("bonus_tarixi")
        if (serializer.validated_data.get("bonus_tarixi") == None):
            bonus_tarixi = datetime.date.today()
        elif (serializer.validated_data.get("bonus_tarixi") == ""):
            bonus_tarixi = datetime.date.today()
        print(f"{bonus_tarixi=}")

        indi = datetime.date.today()
        print(f"Celery indi ==> {indi}")
        d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
        print(f"d ==> {d}")
        next_m = d + pd.offsets.MonthBegin(1)
        print(f"next_m ==> {next_m}")

        maas_goruntuleme = MaasGoruntuleme.objects.get(isci=isci, tarix=next_m)
        print(f"{maas_goruntuleme=}")
        maas_goruntuleme.yekun_maas = maas_goruntuleme.yekun_maas + float(mebleg)
        

        ofis = isci.ofis
        print(f"{ofis=}")

        shirket = isci.shirket
        print(f"{shirket=}")

        holding = Holding.objects.all()[0]
        print(f"{holding=}")

        qeyd = f"{user.asa} tərəfindən {isci.asa} adlı işçiyə {mebleg} AZN bonus"

        if ofis is not None:
            ofis_kassa = OfisKassa.objects.get(ofis=ofis)
            print(f"{ofis_kassa=}")
            print(f"{ofis_kassa.balans=}")
            if float(ofis_kassa.balans) < float(mebleg):
                return Response({"detail": "Ofisin kassasında yetəri qədər məbləğ yoxdur"})
            ofis_kassa.balans = float(ofis_kassa.balans) - float(mebleg)
            ofis_kassa.save()
            print(f"{ofis_kassa.balans=}")
            ofis_kassa_mexaric = OfisKassaMexaric.objects.create(
                mexaric_eden=user,
                ofis_kassa=ofis_kassa,
                mebleg=mebleg,
                mexaric_tarixi=bonus_tarixi,
                qeyd=qeyd
            )
            ofis_kassa_mexaric.save()
        elif ofis == None and shirket is not None:
            shirket_kassa = ShirketKassa.objects.get(shirket=shirket)
            print(f"{shirket_kassa=}")
            print(f"{shirket_kassa.balans=}")
            if float(shirket_kassa.balans) < float(mebleg):
                return Response({"detail": "Şirkətin kassasında yetəri qədər məbləğ yoxdur"})
            shirket_kassa.balans = float(shirket_kassa.balans) - float(mebleg)
            shirket_kassa.save()
            print(f"{shirket_kassa.balans=}")
            shirket_kassa_mexaric = ShirketKassaMexaric.objects.create(
                mexaric_eden=user,
                shirket_kassa=shirket_kassa,
                mebleg=mebleg,
                mexaric_tarixi=bonus_tarixi,
                qeyd=qeyd
            )
            shirket_kassa_mexaric.save()
        elif ofis == None and shirket == None and holding is not None:
            holding_kassa = HoldingKassa.objects.get(holding=holding)
            print(f"{holding_kassa=}")
            print(f"{holding_kassa.balans=}")
            if float(holding_kassa.balans) < float(mebleg):
                return Response({"detail": "Holdingin kassasında yetəri qədər məbləğ yoxdur"})
            holding_kassa.balans = float(holding_kassa.balans) - float(mebleg)
            holding_kassa.save()
            print(f"{holding_kassa.balans=}")
            holding_kassa_mexaric = HoldingKassaMexaric.objects.create(
                mexaric_eden=user,
                holding_kassa=holding_kassa,
                mebleg=mebleg,
                mexaric_tarixi=bonus_tarixi,
                qeyd=qeyd
            )
            holding_kassa_mexaric.save()

        maas_goruntuleme.save()
        serializer.save()


        return Response({"detail": "Bonus əlavə olundu"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"detail": "Xəta baş verdi"}, status=status.HTTP_400_BAD_REQUEST)

def kesinti_create(self, request, *args, **kwargs):
    """
    İşçinin maaşından kəsinti tutmaq funksiyası
    """
    serializer = self.get_serializer(data=request.data)
    user = self.request.user
    print(f"login olan user ==> {user}")
    if serializer.is_valid():
        isci = serializer.validated_data.get("isci")
        print(f"{isci=}")
        mebleg = serializer.validated_data.get("mebleg")
        print(f"{mebleg=}")
        qeyd = serializer.validated_data.get("qeyd")
        print(f"{qeyd=}")
        kesinti_tarixi = serializer.validated_data.get("kesinti_tarixi")
        if (serializer.validated_data.get("kesinti_tarixi") == None):
            kesinti_tarixi = datetime.date.today()
        elif (serializer.validated_data.get("kesinti_tarixi") == ""):
            kesinti_tarixi = datetime.date.today()
        print(f"{kesinti_tarixi=}")

        indi = datetime.date.today()
        print(f"Celery indi ==> {indi}")
        d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
        print(f"d ==> {d}")
        next_m = d + pd.offsets.MonthBegin(1)
        print(f"next_m ==> {next_m}")

        maas_goruntuleme = MaasGoruntuleme.objects.get(isci=isci, tarix=next_m)
        print(f"{maas_goruntuleme=}")
        maas_goruntuleme.yekun_maas = maas_goruntuleme.yekun_maas - float(mebleg)

        ofis = isci.ofis
        print(f"{ofis=}")

        shirket = isci.shirket
        print(f"{shirket=}")

        holding = Holding.objects.all()[0]
        print(f"{holding=}")

        qeyd = f"{user.asa} tərəfindən {isci.asa} adlı işçinin maaşından {mebleg} AZN kəsinti"

        if ofis is not None:
            ofis_kassa = OfisKassa.objects.get(ofis=ofis)
            print(f"{ofis_kassa=}")
            print(f"{ofis_kassa.balans=}")
            ofis_kassa.balans = float(ofis_kassa.balans) + float(mebleg)
            ofis_kassa.save()
            print(f"{ofis_kassa.balans=}")
            ofis_kassa_medaxil = OfisKassaMedaxil.objects.create(
                medaxil_eden=user,
                ofis_kassa=ofis_kassa,
                mebleg=mebleg,
                medaxil_tarixi=kesinti_tarixi,
                qeyd=qeyd
            )
            ofis_kassa_medaxil.save()
        elif ofis == None and shirket is not None:
            shirket_kassa = ShirketKassa.objects.get(shirket=shirket)
            print(f"{shirket_kassa=}")
            print(f"{shirket_kassa.balans=}")
            shirket_kassa.balans = float(shirket_kassa.balans) + float(mebleg)
            shirket_kassa.save()
            print(f"{shirket_kassa.balans=}")
            shirket_kassa_medaxil = ShirketKassaMedaxil.objects.create(
                medaxil_eden=user,
                shirket_kassa=shirket_kassa,
                mebleg=mebleg,
                medaxil_tarixi=kesinti_tarixi,
                qeyd=qeyd
            )
            shirket_kassa_medaxil.save()
        elif ofis == None and shirket == None and holding is not None:
            holding_kassa = HoldingKassa.objects.get(holding=holding)
            print(f"{holding_kassa=}")
            print(f"{holding_kassa.balans=}")
            holding_kassa.balans = float(holding_kassa.balans) + float(mebleg)
            holding_kassa.save()
            print(f"{holding_kassa.balans=}")
            holding_kassa_medaxil = HoldingKassaMedaxil.objects.create(
                medaxil_eden=user,
                holding_kassa=holding_kassa,
                mebleg=mebleg,
                medaxil_tarixi=kesinti_tarixi,
                qeyd=qeyd
            )
            holding_kassa_medaxil.save()

        maas_goruntuleme.save()
        serializer.save()


        return Response({"detail": "Kəsinti əməliyyatı yerinə yetirildi"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"detail": "Xəta baş verdi"}, status=status.HTTP_400_BAD_REQUEST)

def avans_create(self, request, *args, **kwargs):
    """
    İşçiyə avans vermə funksiyası
    """
    serializer = self.get_serializer(data=request.data)
    user = self.request.user
    print(f"login olan user ==> {user}")
    if serializer.is_valid():
        isci = serializer.validated_data.get("isci")
        print(f"{isci=}")
        mebleg = serializer.validated_data.get("mebleg")
        print(f"{mebleg=}")
        qeyd = serializer.validated_data.get("qeyd")
        print(f"{qeyd=}")
        avans_tarixi = serializer.validated_data.get("avans_tarixi")
        if (serializer.validated_data.get("avans_tarixi") == None):
            avans_tarixi = datetime.date.today()
        elif (serializer.validated_data.get("avans_tarixi") == ""):
            avans_tarixi = datetime.date.today()
        print(f"{avans_tarixi=}")

        indi = datetime.date.today()
        print(f"Celery indi ==> {indi}")
        d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
        print(f"d ==> {d}")
        next_m = d + pd.offsets.MonthBegin(1)
        print(f"next_m ==> {next_m}")

        maas_goruntuleme = MaasGoruntuleme.objects.get(isci=isci, tarix=f"{indi.year}-{indi.month}-{1}")
        print(f"{maas_goruntuleme=}")

        yarim_ay_emek_haqqi = serializer.validated_data.get("yarim_ay_emek_haqqi")
        print(f"{yarim_ay_emek_haqqi=}")
        if yarim_ay_emek_haqqi is not None:
            mebleg = float(maas_goruntuleme.yekun_maas) % int(yarim_ay_emek_haqqi)

        maas_goruntuleme.yekun_maas = maas_goruntuleme.yekun_maas - float(mebleg)

        ofis = isci.ofis
        print(f"{ofis=}")

        shirket = isci.shirket
        print(f"{shirket=}")

        holding = Holding.objects.all()[0]
        print(f"{holding=}")

        qeyd = f"{user.asa} tərəfindən {isci.asa} adlı işçiyə {mebleg} AZN avans"

        if ofis is not None:
            ofis_kassa = OfisKassa.objects.get(ofis=ofis)
            print(f"{ofis_kassa=}")
            print(f"{ofis_kassa.balans=}")
            if float(ofis_kassa.balans) < float(mebleg):
                return Response({"detail": "Ofisin kassasında yetəri qədər məbləğ yoxdur"})
            ofis_kassa.balans = float(ofis_kassa.balans) - float(mebleg)
            ofis_kassa.save()
            print(f"{ofis_kassa.balans=}")
            ofis_kassa_mexaric = OfisKassaMexaric.objects.create(
                mexaric_eden=user,
                ofis_kassa=ofis_kassa,
                mebleg=mebleg,
                mexaric_tarixi=avans_tarixi,
                qeyd=qeyd
            )
            ofis_kassa_mexaric.save()
        elif ofis == None and shirket is not None:
            shirket_kassa = ShirketKassa.objects.get(shirket=shirket)
            print(f"{shirket_kassa=}")
            print(f"{shirket_kassa.balans=}")
            if float(shirket_kassa.balans) < float(mebleg):
                return Response({"detail": "Şirkətin kassasında yetəri qədər məbləğ yoxdur"})
            shirket_kassa.balans = float(shirket_kassa.balans) - float(mebleg)
            shirket_kassa.save()
            print(f"{shirket_kassa.balans=}")
            shirket_kassa_mexaric = ShirketKassaMexaric.objects.create(
                mexaric_eden=user,
                shirket_kassa=shirket_kassa,
                mebleg=mebleg,
                mexaric_tarixi=avans_tarixi,
                qeyd=qeyd
            )
            shirket_kassa_mexaric.save()
        elif ofis == None and shirket == None and holding is not None:
            holding_kassa = HoldingKassa.objects.get(holding=holding)
            print(f"{holding_kassa=}")
            print(f"{holding_kassa.balans=}")
            if float(holding_kassa.balans) < float(mebleg):
                return Response({"detail": "Holdingin kassasında yetəri qədər məbləğ yoxdur"})
            holding_kassa.balans = float(holding_kassa.balans) - float(mebleg)
            holding_kassa.save()
            print(f"{holding_kassa.balans=}")
            holding_kassa_mexaric = HoldingKassaMexaric.objects.create(
                mexaric_eden=user,
                holding_kassa=holding_kassa,
                mebleg=mebleg,
                mexaric_tarixi=avans_tarixi,
                qeyd=qeyd
            )
            holding_kassa_mexaric.save()

        maas_goruntuleme.save()
        serializer.save(mebleg=mebleg)


        return Response({"detail": "Avans vermə əməliyyatı yerinə yetirildi"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"detail": "Xəta baş verdi"}, status=status.HTTP_400_BAD_REQUEST)