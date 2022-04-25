from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from company.models import (
    HoldingdenShirketlereTransfer,
    ShirketdenHoldingeTransfer,
    ShirketdenOfislereTransfer,
    OfisdenShirketeTransfer, ShirketKassa, HoldingKassa, OfisKassa
)

from account.models import User

import traceback


def holding_shirket_transfer_create(self, request, *args, **kwargs):
    """
        Holdingden sirketlere transfer ucun istifade olunan method
    """
    serializer = self.get_serializer(data=request.data)

    if (serializer.is_valid()):
        transfer_meblegi = serializer.validated_data.get("transfer_meblegi")
        print(f"transfer_meblegi ==> {transfer_meblegi} -- {type(transfer_meblegi)}")

        gonderen_kassa = serializer.validated_data.get("holding_kassa")
        print(f"gonderen_kassa ==> {gonderen_kassa} -- {type(gonderen_kassa)}")

        gonderen_kassa_balans = gonderen_kassa.balans
        print(f"gonderen_kassa_balans ==> {gonderen_kassa_balans}")

        gonderilen_kassalar = serializer.validated_data.get("shirket_kassa")
        print(f"gonderilen_kassalar ==> {gonderilen_kassalar} -- {type(gonderilen_kassalar)}")
        gonderilen_kassalar_cemi = len(gonderilen_kassalar)
        print(f"gonderilen_kassalar_cemi ==> {gonderilen_kassalar_cemi} -- {type(gonderilen_kassalar_cemi)}")

        if (transfer_meblegi != ""):
            if float(transfer_meblegi) <= float(gonderen_kassa_balans):
                gonderen_kassa_yekun_balans = float(gonderen_kassa_balans) - (
                        float(transfer_meblegi) * gonderilen_kassalar_cemi)
                gonderen_kassa.balans = gonderen_kassa_yekun_balans
                gonderen_kassa.save()
            else:
                return Response({"detail": "Transfer məbləği kassanın balansıdan böyük ola bilməz"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Məbləği doğru daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

        for i in gonderilen_kassalar:
            gonderilen_kassa = i
            print(f"gonderilen_kassa ==> {gonderilen_kassa} -- {type(gonderilen_kassa)}")
            gonderilen_kassa_balans = gonderilen_kassa.balans
            print(f"gonderilen_kassa_balans ==> {gonderilen_kassa_balans}")

            gonderilen_kassa_balans = float(transfer_meblegi) + float(gonderilen_kassa_balans)

            gonderilen_kassa.balans = gonderilen_kassa_balans
            gonderilen_kassa.save()

        serializer.save()
    return Response({"detail": "Transfer edildi"}, status=status.HTTP_201_CREATED)


def shirket_holding_transfer_create(self, request, *args, **kwargs):
    """
        Sirketden holdinge transfer ucun istifade olunan method
    """
    serializer = self.get_serializer(data=request.data)

    if (serializer.is_valid()):
        gonderen_kassa = serializer.validated_data.get("shirket_kassa")
        transfer_meblegi = request.data.get("transfer_meblegi")

        gonderen_kassa_balans = gonderen_kassa.balans
        print(f"gonderen_kassa_balans ==> {gonderen_kassa_balans}")

        if (transfer_meblegi != ""):
            if float(transfer_meblegi) <= float(gonderen_kassa_balans):
                gonderen_kassa.balans = float(gonderen_kassa_balans) - float(transfer_meblegi)
                gonderen_kassa.save()
            else:
                return Response({"detail": "Transfer məbləği kassanın balansıdan böyük ola bilməz"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Məbləği doğru daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

        gonderilen_kassa = serializer.validated_data.get("holding_kassa")

        gonderilen_kassa_balans = gonderilen_kassa.balans
        print(f"gonderilen_kassa_balans ==> {gonderilen_kassa_balans}")

        gonderilen_kassa.balans = float(transfer_meblegi) + float(gonderilen_kassa_balans)
        gonderilen_kassa.save()

        serializer.save()

        return Response({"detail": "Transfer edildi"}, status=status.HTTP_201_CREATED)


def shirket_ofis_transfer_create(self, request, *args, **kwargs):
    """
        Sirketden ofislere transfer ucun istifade olunan method
    """
    serializer = self.get_serializer(data=request.data)

    if (serializer.is_valid()):
        transfer_meblegi = serializer.validated_data.get("transfer_meblegi")
        print(f"transfer_meblegi ==> {transfer_meblegi} -- {type(transfer_meblegi)}")

        gonderen_kassa = serializer.validated_data.get("shirket_kassa")
        print(f"gonderen_kassa ==> {gonderen_kassa} -- {type(gonderen_kassa)}")

        gonderen_kassa_balans = gonderen_kassa.balans
        print(f"gonderen_kassa_balans ==> {gonderen_kassa_balans}")

        gonderilen_kassalar = serializer.validated_data.get("ofis_kassa")
        print(f"gonderilen_kassalar ==> {gonderilen_kassalar} -- {type(gonderilen_kassalar)}")

        gonderilen_kassalar_cemi = len(gonderilen_kassalar)
        print(f"gonderilen_kassalar_cemi ==> {gonderilen_kassalar_cemi} -- {type(gonderilen_kassalar_cemi)}")

        if (transfer_meblegi != ""):
            if float(transfer_meblegi) <= float(gonderen_kassa_balans):
                gonderen_kassa_yekun_balans = float(gonderen_kassa_balans) - (
                            float(transfer_meblegi) * gonderilen_kassalar_cemi)
                gonderen_kassa.balans = gonderen_kassa_yekun_balans
                gonderen_kassa.save()
            else:
                return Response({"detail": "Transfer məbləği kassanın balansıdan böyük ola bilməz"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Məbləği doğru daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

        for i in gonderilen_kassalar:
            gonderilen_kassa = i
            print(f"gonderilen_kassa ==> {gonderilen_kassa} -- {type(gonderilen_kassa)}")
            gonderilen_kassa_balans = gonderilen_kassa.balans
            print(f"gonderilen_kassa_balans ==> {gonderilen_kassa_balans}")

            gonderilen_kassa_balans = float(transfer_meblegi) + float(gonderilen_kassa_balans)

            gonderilen_kassa.balans = gonderilen_kassa_balans
            gonderilen_kassa.save()

        serializer.save()
    return Response({"detail": "Transfer edildi"}, status=status.HTTP_201_CREATED)


def ofis_shirket_transfer_create(self, request, *args, **kwargs):
    """
        Ofisden sirkete transfer ucun istifade olunan method
    """
    serializer = self.get_serializer(data=request.data)

    if (serializer.is_valid()):
        gonderen_kassa = serializer.validated_data.get("ofis_kassa")
        transfer_meblegi = request.data.get("transfer_meblegi")

        gonderen_kassa_balans = gonderen_kassa.balans
        print(f"gonderen_kassa_balans ==> {gonderen_kassa_balans}")

        if (transfer_meblegi != ""):
            if float(transfer_meblegi) <= float(gonderen_kassa_balans):
                gonderen_kassa.balans = float(gonderen_kassa_balans) - float(transfer_meblegi)
                gonderen_kassa.save()
            else:
                return Response({"detail": "Transfer məbləği kassanın balansıdan böyük ola bilməz"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Məbləği doğru daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

        gonderilen_kassa = serializer.validated_data.get("shirket_kassa")

        gonderilen_kassa_balans = gonderilen_kassa.balans
        print(f"gonderilen_kassa_balans ==> {gonderilen_kassa_balans}")

        gonderilen_kassa.balans = float(transfer_meblegi) + float(gonderilen_kassa_balans)
        gonderilen_kassa.save()

        serializer.save()

        return Response({"detail": "Transfer edildi"}, status=status.HTTP_201_CREATED)
