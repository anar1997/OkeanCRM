from rest_framework import status, permissions, generics

import math
import pandas as pd

import datetime

from rest_framework.response import Response
from rest_framework import generics

from api.v1.all_serializers.muqavile_serializers import (
    AnbarSerializer,
    MehsullarSerializer,
    EmeliyyatSerializer,
    AnbarQeydlerSerializer,
    MuqavileSerializer,
    MuqavileHediyyeSerializer,
    OdemeTarixSerializer,
    ServisSerializer,
    StokSerializer,
)

from mehsullar.models import (
    Emeliyyat, 
    MuqavileHediyye, 
    Muqavile, 
    OdemeTarix, 
    Anbar, 
    Mehsullar, 
    AnbarQeydler, 
    Servis, 
    Stok
)
from api.v1.utils import (
    odeme_tarixleri_utils,
    muqavile_utils,
    muqavile_hediyye_utils,
    anbar_emeliyyat_utils,
    servis_utils,
    stok_utils
)

from django_filters.rest_framework import DjangoFilterBackend

from api.v1.filters.muqavile_filters.filters import (
    OdemeTarixFilter,
    MuqavileFilter,
    StokFilter,
)

from rest_framework.generics import get_object_or_404

from api.v1.permissions.muqavile_permissions import permissions as muqavile_permissions

# ********************************** muqavile get post put delete **********************************

class MuqavileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Muqavile.objects.all()
    serializer_class = MuqavileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MuqavileFilter
    permission_classes = [muqavile_permissions.MuqavilePermissions]

    def create(self, request, *args, **kwargs):
        return muqavile_utils.muqavile_create(self, request, *args, **kwargs)


class MuqavileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Muqavile.objects.all()
    serializer_class = MuqavileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MuqavileFilter
    permission_classes = [muqavile_permissions.MuqavilePermissions]

    def patch(self, request, *args, **kwargs):
        return muqavile_utils.muqavile_patch(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return muqavile_utils.muqavile_update(self, request, *args, **kwargs)


# ********************************** odeme tarixi put get post delete **********************************


class OdemeTarixListCreateAPIView(generics.ListCreateAPIView):
    queryset = OdemeTarix.objects.all()
    serializer_class = OdemeTarixSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OdemeTarixFilter
    permission_classes = [muqavile_permissions.OdemeTarixleriPermissions]

class OdemeTarixDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OdemeTarix.objects.all()
    serializer_class = OdemeTarixSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['muqavile']
    filterset_class = OdemeTarixFilter
    permission_classes = [muqavile_permissions.OdemeTarixleriPermissions]


    # PATCH SORGUSU
    def patch(self, request, *args, **kwargs):
        return odeme_tarixleri_utils.odeme_tarixi_patch(self, request, *args, **kwargs)

    # PUT SORGUSU
    def update(self, request, *args, **kwargs):
        return odeme_tarixleri_utils.odeme_tarixi_update(self, request, *args, **kwargs)


# ********************************** anbar put get post delete **********************************


class AnbarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Anbar.objects.all()
    serializer_class = AnbarSerializer
    permission_classes = [muqavile_permissions.AnbarPermissions]


class AnbarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anbar.objects.all()
    serializer_class = AnbarSerializer
    permission_classes = [muqavile_permissions.AnbarPermissions]


# ********************************** mehsullar put get post delete **********************************


class MehsullarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mehsullar.objects.all()
    serializer_class = MehsullarSerializer
    permission_classes = [muqavile_permissions.MehsullarPermissions]


class MehsullarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mehsullar.objects.all()
    serializer_class = MehsullarSerializer
    permission_classes = [muqavile_permissions.MehsullarPermissions]


# ********************************** anbar put delete post get **********************************


class AnbarQeydlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = AnbarQeydler.objects.all()
    serializer_class = AnbarQeydlerSerializer
    permission_classes = [muqavile_permissions.AnbarQeydlerPermissions]


class AnbarQeydlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnbarQeydler.objects.all()
    serializer_class = AnbarQeydlerSerializer
    permission_classes = [muqavile_permissions.AnbarQeydlerPermissions]

# ********************************** emeliyyat put delete post get **********************************


class EmeliyyatListCreateAPIView(generics.ListCreateAPIView):
    queryset = Emeliyyat.objects.all()
    serializer_class = EmeliyyatSerializer
    permission_classes = [muqavile_permissions.EmeliyyatPermissions]

    def create(self, request, *args, **kwargs):
        return anbar_emeliyyat_utils.emeliyyat_create(self, request, *args, **kwargs)

class EmeliyyatDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emeliyyat.objects.all()
    serializer_class = EmeliyyatSerializer
    permission_classes = [muqavile_permissions.EmeliyyatPermissions]


# ********************************** hediyye put delete post get **********************************


class MuqavileHediyyeListCreateAPIView(generics.ListCreateAPIView):
    queryset = MuqavileHediyye.objects.all()
    serializer_class = MuqavileHediyyeSerializer
    permission_classes = [muqavile_permissions.MuqavileHediyyePermissions]

    def create(self, request, *args, **kwargs):
        return muqavile_hediyye_utils.muqavile_hediyye_create(self, request, *args, **kwargs)


class MuqavileHediyyeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MuqavileHediyye.objects.all()
    serializer_class = MuqavileHediyyeSerializer
    permission_classes = [muqavile_permissions.MuqavileHediyyePermissions]


# ********************************** servis put delete post get **********************************

class ServisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Servis.objects.all()
    serializer_class = ServisSerializer
    permission_classes = [muqavile_permissions.ServisPermissions]

    def perform_create(self, serializer):
        month6 = datetime.datetime.now() + datetime.timedelta(days=180)
        month18 = datetime.datetime.now() + datetime.timedelta(days=540)
        month24 = datetime.datetime.now() + datetime.timedelta(days=720)

        serializer.save(
            servis_tarix6ay=f"{month6.year}-{month6.month}-{datetime.datetime.now().day}",
            servis_tarix18ay=f"{month18.year}-{month18.month}-{datetime.datetime.now().day}",
            servis_tarix24ay=f"{month24.year}-{month24.month}-{datetime.datetime.now().day}"
        )


class ServisDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servis.objects.all()
    serializer_class = ServisSerializer
    permission_classes = [muqavile_permissions.ServisPermissions]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # indi_u = f"{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}"
        indi = datetime.date.today()
        servis_tarix6ay = request.POST["servis_tarix6ay"]
        servis_tarix18ay = request.POST["servis_tarix18ay"]
        servis_tarix24ay = request.POST["servis_tarix24ay"]
        kartric1_id = int(request.POST["kartric1_id"])
        kartric2_id = int(request.POST["kartric2_id"])
        kartric3_id = int(request.POST["kartric3_id"])
        kartric4_id = int(request.POST["kartric4_id"])
        kartric5_id = int(request.POST["kartric5_id"])
        kartric6_id = int(request.POST["kartric6_id"])
        muqavile_id = request.POST["muqavile_id"]

        month6 = datetime.date.today() + datetime.timedelta(days=180)
        month18 = datetime.date.today() + datetime.timedelta(days=540)
        month24 = datetime.date.today() + datetime.timedelta(days=720)

        print(f"month6 ==> {month6}")
        print(f"month18 ==> {month18}")
        print(f"month24 ==> {month24}")
        print(f"{month6.year}-{month6.month}-{datetime.datetime.now().day}")

        print(f"indi --> {indi}")

        print(f"Tarix 6ay ==> {servis_tarix6ay}")
        print(f"Tarix 18ay ==> {servis_tarix18ay}")
        print(f"Tarix 24ay ==> {servis_tarix24ay}")

        print(f"kartric1_id ==> {kartric1_id}")
        print(f"kartric2_id ==> {kartric2_id}")
        print(f"kartric3_id ==> {kartric3_id}")
        print(f"kartric4_id ==> {kartric4_id}")
        print(f"kartric5_id ==> {kartric5_id}")
        print(f"kartric6_id ==> {kartric6_id}")

        try:
            muqavile = get_object_or_404(Muqavile, pk=muqavile_id)
            servis = get_object_or_404(Servis, muqavile=muqavile)
            print(servis)
            print(servis.servis_tarix6ay)
            print(type(servis.servis_tarix6ay))
            print(f"Muqavile ==> {muqavile}")
            print(f"Muqavile ofis ==> {muqavile.vanleader.ofis}")
            anbar = get_object_or_404(Anbar, ofis=muqavile.vanleader.ofis)
            print(f"Muqavile anbar ==> {anbar}")

            if (str(indi) != str(servis.servis_tarix6ay) and indi != str(servis.servis_tarix18ay) and indi != str(servis.servis_tarix24ay)):
                return Response({"Servis müddətinə hələ var"}, status=status.HTTP_404_NOT_FOUND)

            if (str(servis.servis_tarix6ay) == str(indi)):
                print(f"servis_tarix6ay == indi ===> {servis_tarix6ay == str(indi)}")
                try:
                    mehsul_kartric1 = get_object_or_404(Mehsullar, pk=kartric1_id)
                    mehsul_kartric2 = get_object_or_404(Mehsullar, pk=kartric2_id)
                    mehsul_kartric3 = get_object_or_404(Mehsullar, pk=kartric3_id)
                    mehsul_kartric4 = get_object_or_404(Mehsullar, pk=kartric4_id)

                    print(f"mehsul_kartric1 ==> {mehsul_kartric1}")
                    print(f"mehsul_kartric2 ==> {mehsul_kartric2}")
                    print(f"mehsul_kartric3 ==> {mehsul_kartric3}")
                    print(f"mehsul_kartric4 ==> {mehsul_kartric4}")

                    print(f"servis_tarix6ay ==> {servis_tarix6ay}")
                    try:
                        stok1 = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul_kartric1)
                        stok2 = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul_kartric2)
                        stok3 = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul_kartric3)
                        stok4 = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul_kartric4)

                        print(f"Muqavile stok1 ==> {stok1}")
                        print(f"Muqavile stok2 ==> {stok2}")
                        print(f"Muqavile stok3 ==> {stok3}")
                        print(f"Muqavile stok4 ==> {stok4}")
                        print(serializer.is_valid())

                        stok1.say = stok1.say - 1
                        stok2.say = stok2.say - 1
                        stok3.say = stok3.say - 1
                        stok4.say = stok4.say - 1
                        stok1.save()
                        stok2.save()
                        stok3.save()
                        stok4.save()
                        if (stok1.say == 0):
                            stok1.delete()

                        if (stok2.say == 0):
                            stok2.delete()

                        if (stok3.say == 0):
                            stok3.delete()

                        if (stok4.say == 0):
                            stok4.delete()
                        muqavile.servis.update(servis_tarix6ay=f"{month6.year}-{month6.month}-{datetime.date.today().day}")
                        super(ServisDetailAPIView, self).update(request, *args, **kwargs)
                        return Response({"Servis müvəffəqiyyətlə yeniləndi"}, status=status.HTTP_200_OK)
                    except:
                        return Response({"Anbarın stokunda məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
                except:
                    return Response({"Bu adla məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
            if (str(servis.servis_tarix18ay) == str(indi)):
                try:
                    mehsul_kartric5 = get_object_or_404(Mehsullar, pk=kartric5_id)

                    print(f"mehsul_kartric5 ==> {mehsul_kartric5}")
                    try:
                        stok5 = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul_kartric5)

                        print(f"Muqavile stok5 ==> {stok5}")

                        stok5.say = stok5.say - 1
                        stok5.save()

                        if (stok5.say == 0):
                            stok5.delete()

                        super(ServisDetailAPIView, self).update(request, *args, **kwargs)
                        return Response({"Servis müvəffəqiyyətlə yeniləndi"}, status=status.HTTP_200_OK)
                    except:
                        return Response({"Anbarın stokunda məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
                except:
                    return Response({"Bu adla məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
            if (str(servis.servis_tarix24ay) == str(indi)):
                try:
                    mehsul_kartric6 = get_object_or_404(Mehsullar, pk=kartric6_id)

                    print(f"mehsul_kartric6 ==> {mehsul_kartric6}")
                    try:
                        stok6 = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul_kartric6)

                        print(f"Muqavile stok6 ==> {stok6}")

                        stok6.say = stok6.say - 1
                        stok6.save()

                        if (stok6.say == 0):
                            stok6.delete()
                        super(ServisDetailAPIView, self).update(request, *args, **kwargs)
                        return Response({"Servis müvəffəqiyyətlə yeniləndi"}, status=status.HTTP_200_OK)
                    except:
                        return Response({"Anbarın stokunda məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
                except:
                    return Response({"Bu adla məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"Belə bir müqavilə tapılmadı"}, status=status.HTTP_404_NOT_FOUND)

# ********************************** stok put delete post get **********************************

class StokListCreateAPIView(generics.ListCreateAPIView):
    queryset = Stok.objects.all()
    serializer_class = StokSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StokFilter
    permission_classes = [muqavile_permissions.StokPermissions]


class StokDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stok.objects.all()
    serializer_class = StokSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StokFilter
    permission_classes = [muqavile_permissions.StokPermissions]

    def update(self, request, *args, **kwargs):
        return stok_utils.stok_update(self, request, *args, **kwargs)