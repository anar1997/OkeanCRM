from rest_framework import status

import pandas as pd

import datetime
from rest_framework.response import Response
from company.models import MuqavileKreditor
from maas.models import KreditorPrim, MaasGoruntuleme

from mehsullar.models import (
    Muqavile, 
    Anbar, 
    Mehsullar,
    Servis,
    ServisOdeme, 
    Stok
)

import traceback

from rest_framework.generics import get_object_or_404

def servis_update(self, request, *args, **kwargs):
    servis = self.get_object()
    serializer = self.get_serializer(servis, data=request.data, partial=True)
    
    print(f"{servis=}")

    if serializer.is_valid():
        muqavile = servis.muqavile
        print(f"{muqavile=}")
        servis_tarix = serializer.validated_data.get("servis_tarix")
        print(f"{servis_tarix=}")
        mehsullar = serializer.validated_data.get("mehsullar")
        print(f"{mehsullar=}")
        
        kredit = serializer.validated_data.get("kredit")
        print(f"{kredit=}")

        kredit_muddeti = serializer.validated_data.get("kredit_muddeti")
        print(f"{kredit_muddeti=}")

        ilkin_odenis = serializer.validated_data.get("ilkin_odenis")
        print(f"{ilkin_odenis=}")

        u_yerine_yetirildi = serializer.validated_data.get("yerine_yetirildi")
        print(f"{u_yerine_yetirildi=}")
        
        yerine_yetirildi = servis.yerine_yetirildi
        print(f"{yerine_yetirildi=}")

        indi_d = datetime.date.today()
        print(f"{indi_d=}")
        indi = f"{indi_d.year}-{indi_d.month}-{1}"
        
        d = pd.to_datetime(f"{indi_d.year}-{indi_d.month}-{1}")
        print(f"d ==> {d}")

        month6 = d + pd.offsets.MonthBegin(6)
        print(f"month6 ==> {month6}")

        month12 = d + pd.offsets.MonthBegin(12)
        print(f"month12 ==> {month12}")

        month18 = d + pd.offsets.MonthBegin(18)
        print(f"month18 ==> {month18}")

        month24 = d + pd.offsets.MonthBegin(24)
        print(f"month24 ==> {month24}")

        anbar = get_object_or_404(Anbar, ofis=muqavile.ofis)
        print(f"Muqavile anbar ==> {anbar}")

        indi = datetime.datetime.today().strftime('%Y-%m-%d')
        print(f"INDI ====> {indi} --- {type(indi)}")
        inc_month = pd.date_range(indi, periods = int(kredit_muddeti)+1, freq='M')
        print(f"inc_month ==> {inc_month} --- {type(inc_month)}")

        if bool(kredit) == True:
            servis_odemeler = ServisOdeme.objects.filter(servis=servis, odendi=False)
            print(f"{servis_odemeler=}")
            for s_o in servis_odemeler:
                s_o.delete()
            
            odenilecek_yeni_mebleg = 0
            if ilkin_odenis is not None:
                if float(ilkin_odenis) > 0:
                    odenilecek_yeni_mebleg = float(servis.servis_qiymeti) - float(ilkin_odenis)

            for i in int(kredit_muddeti):
                if(datetime.date.today().day < 29):
                    servis_odeme = ServisOdeme.objects.create(
                        servis = servis,
                        odeme_tarix = f"{inc_month[i].year}-{inc_month[i].month}-{datetime.date.today().day}",
                        servis_qiymeti = servis.servis_qiymeti,
                        odenilecek_mebleg = odenilecek_yeni_mebleg / int(kredit_muddeti),
                        qeyd = serializer.validated_data.get("qeyd")
                    ).save()
                elif(datetime.date.today().day == 31 or datetime.date.today().day == 30 or datetime.date.today().day == 29):
                    if(inc_month[i].day <= datetime.date.today().day):
                        servis_odeme = ServisOdeme.objects.create(
                            servis = servis,
                            odeme_tarix = f"{inc_month[i].year}-{inc_month[i].month}-{inc_month[i].day}",
                            servis_qiymeti = servis.servis_qiymeti,
                            odenilecek_mebleg = odenilecek_yeni_mebleg / int(kredit_muddeti),
                            qeyd = serializer.validated_data.get("qeyd") 
                        ).save()

        if bool(u_yerine_yetirildi) == True:
            for i in servis.mehsullar.all():
                print(f"{i=}")
                try:
                    stok = get_object_or_404(Stok, anbar=anbar, mehsul=i)
                    print(f'stok --> {stok}')
                    stok.say = stok.say - 1
                    stok.save()
                except Exception:
                    traceback.print_exc()
                    return Response({"detail":"Anbarın stokunda məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
                if i.kartric_novu == "KARTRIC6AY":
                    serializer.save(yerine_yetirildi = True, servis_tarix = month6)
                if i.kartric_novu == "KARTRIC12AY":
                    serializer.save(yerine_yetirildi = True, servis_tarix = month12)
                if i.kartric_novu == "KARTRIC18AY":
                    serializer.save(yerine_yetirildi = True, servis_tarix = month18)
                if i.kartric_novu == "KARTRIC24AY":
                    serializer.save(yerine_yetirildi = True, servis_tarix = month24)

            servis_odemeleri = ServisOdeme.objects.filter(servis=servis)
            print(f"{servis_odemeleri=}")
            for s in servis_odemeleri:
                s.odendi = True
                s.save()
        serializer.save()   
        return Response({"detail":"Servis müvəffəqiyyətlə yeniləndi"}, status=status.HTTP_200_OK)

def servis_odeme_update(self, request, *args, **kwargs):
    servis_odeme = self.get_object()
    print(f"{servis_odeme=}")
    serializer = self.get_serializer(servis_odeme, data=request.data, partial=True)

    if serializer.is_valid():
        endrim = serializer.validated_data.get("endrim")
        print(f"{endrim=}")

        odendi = serializer.validated_data.get("odendi")
        print(f"{odendi=}")

        muqavile = servis_odeme.servis.muqavile
        print(f"{muqavile=}")

        muqavile_kreditor = MuqavileKreditor.objects.get(muqavile=muqavile)
        print(f"{muqavile_kreditor=}")

        kreditor = muqavile_kreditor.kreditor
        print(f"{kreditor=}")

        kreditor_prim_all = KreditorPrim.objects.all()
        print(f"{kreditor_prim_all=}")

        kreditor_prim = kreditor_prim_all[0]
        print(f"{kreditor_prim=}")

        prim_faizi = kreditor_prim.prim_faizi
        print(f"{prim_faizi=}")

        indi = datetime.date.today()
        print(f"Indi ==> {indi}")

        bu_ay = f"{indi.year}-{indi.month}-{1}"

        maas_goruntulenme_kreditor = MaasGoruntuleme.objects.get(isci=kreditor, tarix=bu_ay)
        print(f"{maas_goruntulenme_kreditor=}")


        if endrim is not None:
            if float(endrim) > 0:
                if float(endrim) < float(servis_odeme.odenilecek_mebleg):
                    servis_odeme.odenilecek_mebleg = float(servis_odeme.odenilecek_mebleg) - endrim
                    servis_odeme.save()
                else:
                   return Response({"detail":"Endrim miqdarı ödəniləcək məbləğdən daha çox ola bilməz"}, status=status.HTTP_400_BAD_REQUEST) 

                serializer.save()
                return Response({"detail":"Endrim tətbiq olundu"}, status=status.HTTP_200_OK)
        if odendi is not None:
            if bool(odendi) == True:
                servisler_qs = ServisOdeme.objects.filter(servis=servis_odeme.servis, odendi=False)
                servisler = list(servisler_qs)
                print(f"{servisler=}")
                if servis_odeme == servisler[-1]:
                    servis_odeme.servis.yerine_yetirildi = True
                    servis_odeme.servis.save()
                    servis_odeme.odendi = True
                    servis_odeme.save()
                    print(f"{servis_odeme.odenilecek_mebleg=}")
                    kreditorun_servisden_alacagi_mebleg = (float(servis_odeme.odenilecek_mebleg) * int(prim_faizi)) / 100
                    print(f"{kreditorun_servisden_alacagi_mebleg=}")

                    maas_goruntulenme_kreditor.yekun_maas = maas_goruntulenme_kreditor.yekun_maas + kreditorun_servisden_alacagi_mebleg
                    print(f"{maas_goruntulenme_kreditor.yekun_maas=}")
                    maas_goruntulenme_kreditor.save()
                return Response({"detail":"Servis məbləği ödəndi"}, status=status.HTTP_200_OK)
        serializer.save()
        return Response({"detail":"Servis Ödəmə müvəffəqiyyətlə yeniləndi"}, status=status.HTTP_200_OK)