from rest_framework import status

import pandas as pd

import datetime
from rest_framework.response import Response

from mehsullar.models import (
    Muqavile, 
    Anbar, 
    Mehsullar,
    Servis, 
    Stok
)

from rest_framework.generics import get_object_or_404


def servis_update(self, request, *args, **kwargs):
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