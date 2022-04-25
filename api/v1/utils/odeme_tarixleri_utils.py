from account.models import Musteri, User
from company.models import OfisKassa, OfisKassaMedaxil
from mehsullar.models import Muqavile, OdemeTarix
from rest_framework.exceptions import ValidationError
import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
import math
import pandas as pd

from api.v1.all_serializers.muqavile_serializers import OdemeTarixSerializer

def k_medaxil(company_kassa, daxil_edilecek_mebleg, vanleader, qeyd):
    yekun_balans = float(daxil_edilecek_mebleg) + float(company_kassa.balans)
    company_kassa.balans = yekun_balans
    company_kassa.save()
    tarix = datetime.date.today()

    medaxil = OfisKassaMedaxil.objects.create(
        medaxil_eden=vanleader,
        ofis_kassa=company_kassa,
        mebleg=daxil_edilecek_mebleg,
        medaxil_tarixi=tarix,
        qeyd=qeyd
    )
    medaxil.save()
    return medaxil

# PATCH sorgusu
def odeme_tarixi_patch(self, request, *args, **kwargs):
    indiki_ay = self.get_object()
    serializer = OdemeTarixSerializer(indiki_ay, data=request.data, partial=True) # set partial=True to update a data partially
    print(f"request.data ===> {request.data}")

    odenme_status = request.data.get("odenme_status")
    gecikdirme_status = request.data.get("gecikdirme_status")
    natamama_gore_odeme_status = request.data.get("natamam_ay_alt_status")
    sifira_gore_odeme_status = request.data.get("buraxilmis_ay_alt_status")
    artiq_odeme_alt_status = request.data.get('artiq_odeme_alt_status')
    
    odemek_istediyi_mebleg = request.data.get("qiymet")

    borcu_bagla_status = request.data.get("borcu_bagla_status")
    
    try:
        if(borcu_bagla_status == "BORCU BAĞLA"):
            muqavile = indiki_ay.muqavile

            odenmeyen_odemetarixler_qs = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
            odenmeyen_odemetarixler = list(odenmeyen_odemetarixler_qs)
            print(f"odenmeyen_odemetarixler ==> {odenmeyen_odemetarixler} -- {len(odenmeyen_odemetarixler)}")

            ay_ucun_olan_mebleg = 0
            for i in odenmeyen_odemetarixler:
                ay_ucun_olan_mebleg = ay_ucun_olan_mebleg + float(i.qiymet)
                i.qiymet = 0
                i.odenme_status = "ÖDƏNƏN"
                i.save()
            
            muqavile.muqavile_status = "DAVAM EDƏN"
            muqavile.save()
            return Response({"detail": "Borc tam bağlandı"}, status=status.HTTP_200_OK)

        # GECIKDIRME ILE BAGLI EMELIYYATLAR
        if(odenme_status == "ÖDƏNMƏYƏN" and gecikdirme_status == "GECİKDİRMƏ"):
            indiki_ay = self.get_object()
            muqavile = indiki_ay.muqavile

            my_time = datetime.datetime.min.time()

            odeme_tarixi_date = indiki_ay.tarix
            odeme_tarixi = datetime.datetime.combine(odeme_tarixi_date, my_time)
            odeme_tarixi_san = datetime.datetime.timestamp(odeme_tarixi)

            gecikdirmek_istediyi_tarix = request.data.get("tarix")
            gecikdirmek_istediyi_tarix_date = datetime.datetime.strptime(gecikdirmek_istediyi_tarix, "%Y-%m-%d")
            gecikdirmek_istediyi_tarix_san = datetime.datetime.timestamp(gecikdirmek_istediyi_tarix_date)

            odenmeyen_odemetarixler_qs = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
            odenmeyen_odemetarixler = list(odenmeyen_odemetarixler_qs)
            print(f"odenmeyen_odemetarixler ==> {odenmeyen_odemetarixler}")

            if(indiki_ay == odenmeyen_odemetarixler[-1]):
                try:
                    if(gecikdirmek_istediyi_tarix_san < odeme_tarixi_san):
                        raise ValidationError(detail={"detail": "Tarixi doğru daxil edin!"}, code=status.HTTP_400_BAD_REQUEST)
                except:
                    return Response({"detail": "Qeyd etdiyiniz tarix keçmiş tarixdir."}, status=status.HTTP_400_BAD_REQUEST)

                try:
                    if(odeme_tarixi_san < gecikdirmek_istediyi_tarix_san):
                        if serializer.is_valid():
                            print(f"request.data ===> {request.data}")
                            serializer.save()
                            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
                except:
                    return Response({"detail": "Yeni tarix hal-hazırki tarix ile növbəti ayın tarixi arasında olmalıdır"}, status=status.HTTP_400_BAD_REQUEST)
            elif(indiki_ay != odenmeyen_odemetarixler[-1]):
                novbeti_ay = OdemeTarix.objects.get(pk = indiki_ay.id+1)
                novbeti_ay_tarix_date = novbeti_ay.tarix
                novbeti_ay_tarix = datetime.datetime.combine(novbeti_ay_tarix_date, my_time)
                novbeti_ay_tarix_san = datetime.datetime.timestamp(novbeti_ay_tarix)

                try:
                    if(novbeti_ay_tarix_san == gecikdirmek_istediyi_tarix_san):
                        raise ValidationError(detail={"detail": "Tarixi doğru daxil edin!"}, code=status.HTTP_400_BAD_REQUEST)
                except:
                    return Response({"detail": "Qeyd etdiyiniz tarix növbəti ayın tarixi ilə eynidir."}, status=status.HTTP_400_BAD_REQUEST)

                try:
                    if(gecikdirmek_istediyi_tarix_san < odeme_tarixi_san):
                        raise ValidationError(detail={"detail": "Tarixi doğru daxil edin!"}, code=status.HTTP_400_BAD_REQUEST)
                except:
                    return Response({"detail": "Qeyd etdiyiniz tarix keçmiş tarixdir."}, status=status.HTTP_400_BAD_REQUEST)

                try:
                    if(gecikdirmek_istediyi_tarix_san > novbeti_ay_tarix_san):
                        raise ValidationError(detail={"detail": "Tarixi doğru daxil edin!"}, code=status.HTTP_400_BAD_REQUEST)
                except:
                    return Response({"detail": "Qeyd etdiyiniz tarix növbəti ayın tarixindən böyükdür."}, status=status.HTTP_400_BAD_REQUEST)

                try:
                    if(odeme_tarixi_san < gecikdirmek_istediyi_tarix_san < novbeti_ay_tarix_san):
                        if serializer.is_valid():
                            print(f"request.data ===> {request.data}")
                            serializer.save()
                            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi PATCH"}, status=status.HTTP_200_OK)
                except:
                    return Response({"detail": "Yeni tarix hal-hazırki tarix ile növbəti ayın tarixi arasında olmalıdır"}, status=status.HTTP_400_BAD_REQUEST)
        elif(odenme_status != "ÖDƏNMƏYƏN" and gecikdirme_status == "GECİKDİRMƏ"):
            raise ValidationError(detail={"detail": "Gecikdirmə ancaq ödənməmiş ay üçündür"}, code=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"detail": "Xəta baş verdi"}, status=status.HTTP_400_BAD_REQUEST)
    
    if(odenme_status == "ÖDƏNMƏYƏN" and float(odemek_istediyi_mebleg) == indiki_ay.qiymet):
        indiki_ay = self.get_object()
        muqavile = indiki_ay.muqavile
        odenmeyen_odemetarixler_qs = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
        odenmeyen_odemetarixler = list(odenmeyen_odemetarixler_qs)
        print(f"odenmeyen_odemetarixler ==> {odenmeyen_odemetarixler}")

        if serializer.is_valid():
            indiki_ay.odenme_status = "ÖDƏNƏN"
            indiki_ay.save()
            if(indiki_ay == odenmeyen_odemetarixler[-1]):
                muqavile.muqavile_status = "BİTMİŞ"
                muqavile.save()
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        else:
            return ValidationError(detail={"detail": "Məlumatları doğru daxil edin"}, code=status.HTTP_400_BAD_REQUEST)
    # Natamam Ay odeme statusu ile bagli emeliyyatlar
    if(odenme_status == "NATAMAM AY"):
        indiki_ay = self.get_object()
        muqavile = indiki_ay.muqavile
        ilkin_odenis = muqavile.ilkin_odenis
        ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
        ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
        print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
        mehsulun_qiymeti = muqavile.muqavile_umumi_mebleg
        print(f"mehsulun ==> {mehsulun_qiymeti}")
        indiki_ay.odenme_status = "NATAMAM AY"
        indiki_ay.save()

        odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
        odemek_istediyi_mebleg = float(request.data.get("qiymet"))
        if(natamama_gore_odeme_status == "NATAMAM DİGƏR AYLAR"):
            print(f"indiki_ay.qiymet ==> {indiki_ay.qiymet}")
            odenmeyen_pul = indiki_ay.qiymet - odemek_istediyi_mebleg
            print(f"odenmeyen_pul ==> {odenmeyen_pul}")
            odenmeyen_aylar = len(odenmeyen_odemetarixler)
            print(len(odenmeyen_odemetarixler))
            
            aylara_elave_olunacaq_mebleg = odenmeyen_pul // odenmeyen_aylar
            print(f"aylara_elave_olunacaq_mebleg ==> {aylara_elave_olunacaq_mebleg}")
            b = aylara_elave_olunacaq_mebleg * (odenmeyen_aylar-1)
            print(f"b ==> {b}")
            sonuncu_aya_elave_olunacaq_mebleg = odenmeyen_pul - b
            print(f"sonuncu_aya_elave_olunacaq_mebleg ==> {sonuncu_aya_elave_olunacaq_mebleg}")
            
            indiki_ay.qiymet = odemek_istediyi_mebleg
            indiki_ay.natamam_ay_alt_status = "NATAMAM DİGƏR AYLAR"
            indiki_ay.save()
            i = 0
            while(i<=(odenmeyen_aylar-1)):
                print(f"odenmeyen_aylar-1===>{odenmeyen_aylar-1}")
                if(i == (odenmeyen_aylar-1)):
                    odenmeyen_odemetarixler[i].qiymet = odenmeyen_odemetarixler[i].qiymet + sonuncu_aya_elave_olunacaq_mebleg
                    odenmeyen_odemetarixler[i].save()
                else:
                    odenmeyen_odemetarixler[i].qiymet = odenmeyen_odemetarixler[i].qiymet + aylara_elave_olunacaq_mebleg
                    odenmeyen_odemetarixler[i].save()
                i+=1
            if serializer.is_valid():
                print(f"request.data ===> {request.data}")
                serializer.save()
                return Response({"detail": "Əməliyyat uğurla yerinə yetirildi PATCH"}, status=status.HTTP_200_OK)
        if(natamama_gore_odeme_status == "NATAMAM NÖVBƏTİ AY"):
            indiki_ay = self.get_object()
            natamam_odemek_istediyi_mebleg = indiki_ay.qiymet - odemek_istediyi_mebleg

            novbeti_ay = get_object_or_404(OdemeTarix, pk=self.get_object().id+1)
            novbeti_ay.qiymet = novbeti_ay.qiymet + natamam_odemek_istediyi_mebleg
            novbeti_ay.save()

            indiki_ay.qiymet = odemek_istediyi_mebleg
            indiki_ay.odenme_status = "NATAMAM AY"
            indiki_ay.natamam_ay_alt_status = "NATAMAM NÖVBƏTİ AY"
            indiki_ay.save()
            if serializer.is_valid():
                print(f"request.data ===> {request.data}")
                serializer.save()
                return Response({"detail": "Əməliyyat uğurla yerinə yetirildi PATCH"}, status=status.HTTP_200_OK)
        if(natamama_gore_odeme_status == "NATAMAM SONUNCU AY"):
            indiki_ay = self.get_object()
            natamam_odemek_istediyi_mebleg = indiki_ay.qiymet - odemek_istediyi_mebleg

            sonuncu_ay = odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1]
            print(f"sonuncu_ay ===> {sonuncu_ay}")
            sonuncu_ay.qiymet = sonuncu_ay.qiymet + natamam_odemek_istediyi_mebleg
            sonuncu_ay.save()

            indiki_ay.qiymet = odemek_istediyi_mebleg
            indiki_ay.odenme_status = "NATAMAM AY"
            indiki_ay.natamam_ay_alt_status = "NATAMAM SONUNCU AY"
            indiki_ay.save()
            if serializer.is_valid():
                print(f"request.data ===> {request.data}")
                serializer.save()
                return Response({"detail": "Əməliyyat uğurla yerinə yetirildi PATCH"}, status=status.HTTP_200_OK)

    # Buraxilmis Ay odeme statusu ile bagli emeliyyatlar
    elif((odenme_status == "BURAXILMIŞ AY" and sifira_gore_odeme_status != "") or (float(odemek_istediyi_mebleg) == 0 and sifira_gore_odeme_status != "")):
        indiki_ay = self.get_object()
        muqavile = indiki_ay.muqavile
        ilkin_odenis = muqavile.ilkin_odenis
        ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
        mehsulun_qiymeti = muqavile.muqavile_umumi_mebleg
        print(f"mehsulun ==> {mehsulun_qiymeti}")
        ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
        print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
        indiki_ay.odenme_status = "BURAXILMIŞ AY"
        indiki_ay.save()
        odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
        odemek_istediyi_mebleg = float(request.data.get("qiymet"))
        
        if(sifira_gore_odeme_status == "SIFIR NÖVBƏTİ AY"):
            novbeti_ay = get_object_or_404(OdemeTarix, pk=self.get_object().id+1)
            novbeti_ay.qiymet = novbeti_ay.qiymet + indiki_ay.qiymet
            novbeti_ay.save()
            indiki_ay.qiymet = 0
            indiki_ay.odenme_status = "BURAXILMIŞ AY"
            indiki_ay.buraxilmis_ay_alt_status = "SIFIR NÖVBƏTİ AY"
            indiki_ay.save()
            if serializer.is_valid():
                print(f"request.data ===> {request.data}")
                serializer.save()
                return Response({"detail": "Əməliyyat uğurla yerinə yetirildi PATCH"}, status=status.HTTP_200_OK)
        if(sifira_gore_odeme_status == "SIFIR SONUNCU AY"):
            sonuncu_ay = odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1]
            sonuncu_ay.qiymet = sonuncu_ay.qiymet + indiki_ay.qiymet
            sonuncu_ay.save()
            indiki_ay.qiymet = 0
            indiki_ay.odenme_status = "BURAXILMIŞ AY"
            indiki_ay.buraxilmis_ay_alt_status = "SIFIR SONUNCU AY"
            indiki_ay.save()
            if serializer.is_valid():
                print(f"request.data ===> {request.data}")
                serializer.save()
                return Response({"detail": "Əməliyyat uğurla yerinə yetirildi PATCH"}, status=status.HTTP_200_OK)
        if(sifira_gore_odeme_status == "SIFIR DİGƏR AYLAR"):
            odenmeyen_pul = indiki_ay.qiymet
            print(f"odenmeyen_pul ==> {odenmeyen_pul}")
            odenmeyen_aylar = len(odenmeyen_odemetarixler)
            print(f"odenmeyen_aylar ==> {odenmeyen_aylar}")
            aylara_elave_olunacaq_mebleg = odenmeyen_pul // odenmeyen_aylar
            print(f"aylara_elave_olunacaq_mebleg ==> {aylara_elave_olunacaq_mebleg}")
            a = aylara_elave_olunacaq_mebleg * (odenmeyen_aylar-1)
            sonuncu_aya_elave_olunacaq_mebleg = odenmeyen_pul - a
            print(f"sonuncu_aya_elave_olunacaq_mebleg ==> {sonuncu_aya_elave_olunacaq_mebleg}")
            indiki_ay.qiymet = 0
            indiki_ay.buraxilmis_ay_alt_status = "SIFIR DİGƏR AYLAR"
            indiki_ay.save()
            i = 0
            while(i<=(odenmeyen_aylar-1)):
                if(i == (odenmeyen_aylar-1)):
                    odenmeyen_odemetarixler[i].qiymet = odenmeyen_odemetarixler[i].qiymet + sonuncu_aya_elave_olunacaq_mebleg
                    odenmeyen_odemetarixler[i].save()
                else:
                    odenmeyen_odemetarixler[i].qiymet = odenmeyen_odemetarixler[i].qiymet + aylara_elave_olunacaq_mebleg
                    odenmeyen_odemetarixler[i].save()
                i+=1
        if serializer.is_valid():
            print(f"request.data ===> {request.data}")
            serializer.save()
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi PATCH"}, status=status.HTTP_200_OK)

    # YENI QRAFIK ile bagli emeliyyatlar
    elif(odenme_status == "YENİ QRAFİK"):
        indiki_ay = self.get_object()
        muqavile = indiki_ay.muqavile
        m = get_object_or_404(Muqavile, pk = muqavile.id)
        print(f"m ===> {m}")
        ilkin_odenis = muqavile.ilkin_odenis
        ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
        ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
        print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
        mehsulun_qiymeti = muqavile.muqavile_umumi_mebleg
        print(f"mehsulun ==> {mehsulun_qiymeti}")

        odenen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNƏN")
        print(f"odenen_odemetarixler ==> {odenen_odemetarixler}")
        
        odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
        print(f"odenmeyen_odemetarixler ==> {odenmeyen_odemetarixler}")
        
        odemek_istediyi_mebleg = float(request.data.get("qiymet"))
        print(f"odemek_istediyi_mebleg ==> {odemek_istediyi_mebleg}")

        print(f"len(odenen_odemetarixler) ==> {len(odenen_odemetarixler)}")

        odediyi = len(odenen_odemetarixler) * indiki_ay.qiymet + ilkin_odenis_tam
        print(f"odediyi ==> {odediyi}")

        qaliq_borc = mehsulun_qiymeti - odediyi
        print(f"qaliq_borc ==> {qaliq_borc}")

        odenmeyen_aylar = len(odenmeyen_odemetarixler)
        print(f"odenmeyen_aylar ==> {odenmeyen_aylar}")

        try:
            elave_olunacaq_ay_qaliqli = qaliq_borc / odemek_istediyi_mebleg
            indiki_ay.odenme_status = "YENİ QRAFİK"
            indiki_ay.qiymet = odemek_istediyi_mebleg
            indiki_ay.save()
        except:
            return Response({"detail": "Ödəmək istədiyiniz məbləği doğru daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
        
        elave_olunacaq_ay = math.ceil(elave_olunacaq_ay_qaliqli)
        print(f"elave_olunacaq_ay == > {elave_olunacaq_ay}")
        create_olunacaq_ay = elave_olunacaq_ay - len(odenmeyen_odemetarixler)
        print(f"create_olunacaq_ay == > {create_olunacaq_ay}")
        a = odemek_istediyi_mebleg * (elave_olunacaq_ay-1)
        son_aya_elave_edilecek_mebleg = qaliq_borc - a
        print(f"son_aya_elave_edilecek_mebleg == > {son_aya_elave_edilecek_mebleg}")
        inc_month = pd.date_range(odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1].tarix, periods = create_olunacaq_ay+1, freq='M')
        print(f"inc_month == > {inc_month}")
        m.kredit_muddeti = m.kredit_muddeti + create_olunacaq_ay
        m.save()
        print(f"m.kredit_muddeti ===> {m.kredit_muddeti}")
        # Var olan aylarin qiymetini musterinin istediyi qiymet edir
        i = 1
        while(i<len(odenmeyen_odemetarixler)):
            odenmeyen_odemetarixler[i].qiymet = odemek_istediyi_mebleg
            odenmeyen_odemetarixler[i].save()
            i+=1

        # Elave olunacaq aylari create edir
        j = 1
        while(j<=create_olunacaq_ay):
            if(j == create_olunacaq_ay):
                if(datetime.date.today().day < 29):
                    OdemeTarix.objects.create(
                        muqavile = muqavile,
                        tarix = f"{inc_month[j].year}-{inc_month[j].month}-{datetime.date.today().day}",
                        qiymet = son_aya_elave_edilecek_mebleg
                    )
                elif(datetime.date.today().day == 31 or datetime.date.today().day == 30 or datetime.date.today().day == 29):
                    if(inc_month[j].day <= datetime.date.today().day):
                        OdemeTarix.objects.create(
                            muqavile = muqavile,
                            tarix = f"{inc_month[j].year}-{inc_month[j].month}-{inc_month[j].day}",
                            qiymet = son_aya_elave_edilecek_mebleg
                        )
            else:
                if(datetime.date.today().day < 29):
                    OdemeTarix.objects.create(
                        muqavile = muqavile,
                        tarix = f"{inc_month[j].year}-{inc_month[j].month}-{datetime.date.today().day}",
                        qiymet = odemek_istediyi_mebleg
                    )
                elif(datetime.date.today().day == 31 or datetime.date.today().day == 30 or datetime.date.today().day == 29):
                    if(inc_month[j].day <= datetime.date.today().day):
                        OdemeTarix.objects.create(
                            muqavile = muqavile,
                            tarix = f"{inc_month[j].year}-{inc_month[j].month}-{inc_month[j].day}",
                            qiymet = odemek_istediyi_mebleg
                        )
            j+=1
        if serializer.is_valid():
            print(f"request.data ===> {request.data}")
            serializer.save()
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi PATCH"}, status=status.HTTP_200_OK)
    
    # RAZILASDIRILMIS AZ ODEME ile bagli emeliyyatlar
    elif(odenme_status == "RAZILAŞDIRILMIŞ AZ ÖDƏMƏ"):
        indiki_ay = self.get_object()
        muqavile = indiki_ay.muqavile
        ilkin_odenis = muqavile.ilkin_odenis
        ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
        ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
        print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
        mehsulun_qiymeti = muqavile.muqavile_umumi_mebleg
        print(f"mehsulun ==> {mehsulun_qiymeti}")
        indiki_ay.odenme_status = "RAZILAŞDIRILMIŞ AZ ÖDƏMƏ"
        indiki_ay.save()

        odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
        odemek_istediyi_mebleg = float(request.data.get("qiymet"))

        print(f"indiki_ay.qiymet ==> {indiki_ay.qiymet}")
        odenmeyen_pul = indiki_ay.qiymet - odemek_istediyi_mebleg
        print(f"odenmeyen_pul ==> {odenmeyen_pul}")
        odenmeyen_aylar = len(odenmeyen_odemetarixler)
        print(len(odenmeyen_odemetarixler))
        
        aylara_elave_olunacaq_mebleg = odenmeyen_pul // odenmeyen_aylar
        print(f"aylara_elave_olunacaq_mebleg ==> {aylara_elave_olunacaq_mebleg}")
        b = aylara_elave_olunacaq_mebleg * (odenmeyen_aylar-1)
        print(f"b ==> {b}")
        sonuncu_aya_elave_olunacaq_mebleg = odenmeyen_pul - b
        print(f"sonuncu_aya_elave_olunacaq_mebleg ==> {sonuncu_aya_elave_olunacaq_mebleg}")
        
        indiki_ay.qiymet = odemek_istediyi_mebleg
        indiki_ay.save()
        i = 0
        while(i<=(odenmeyen_aylar-1)):
            print(f"odenmeyen_aylar-1===>{odenmeyen_aylar-1}")
            if(i == (odenmeyen_aylar-1)):
                odenmeyen_odemetarixler[i].qiymet = odenmeyen_odemetarixler[i].qiymet + sonuncu_aya_elave_olunacaq_mebleg
                odenmeyen_odemetarixler[i].save()
            else:
                odenmeyen_odemetarixler[i].qiymet = odenmeyen_odemetarixler[i].qiymet + aylara_elave_olunacaq_mebleg
                odenmeyen_odemetarixler[i].save()
            i+=1
        if serializer.is_valid():
            print(f"request.data ===> {request.data}")
            serializer.save()
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi PATCH"}, status=status.HTTP_200_OK)

    # ARTIQ ODEME ile bagli emeliyyatlar
    elif(odenme_status == "ARTIQ ÖDƏMƏ"):
        if(artiq_odeme_alt_status == "ARTIQ_BİR_AY"):
            indiki_ay = self.get_object()
            print(f"indiki ay ===> {indiki_ay}")
            muqavile = indiki_ay.muqavile
            print(f"muqavile ===> {muqavile}")
            odemek_istediyi_mebleg = float(request.data.get("qiymet"))
            print(f"odemek_istediyi_mebleg ===> {odemek_istediyi_mebleg}")
            normalda_odenmeli_olan = indiki_ay.qiymet
            print(f"normalda_odenmeli_olan ===> {normalda_odenmeli_olan}")

            artiqdan_normalda_odenmeli_olani_cixan_ferq = odemek_istediyi_mebleg - normalda_odenmeli_olan
            print(f"artiqdan_normalda_odenmeli_olani_cixan_ferq ===> {artiqdan_normalda_odenmeli_olani_cixan_ferq}")

            odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
            print(f"odenmeyen_odemetarixler ===> {odenmeyen_odemetarixler}")

            indiki_ay.qiymet = odemek_istediyi_mebleg
            indiki_ay.odenme_status = "ARTIQ ÖDƏMƏ"
            indiki_ay.artiq_odeme_alt_status = "ARTIQ_BİR_AY"
            indiki_ay.save()

            sonuncu_ay = odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1]
            print(f"sonuncu_ay ===> {sonuncu_ay}")
            sonuncudan_bir_evvelki_ay = odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-2]
            print(f"sonuncudan_bir_evvelki_ay ===> {sonuncudan_bir_evvelki_ay}")
            
            sonuncu_aydan_qalan = sonuncu_ay.qiymet - artiqdan_normalda_odenmeli_olani_cixan_ferq
            print(f"sonuncu_aydan_qalan ===> {sonuncu_aydan_qalan}")

            if(sonuncu_ay.qiymet > artiqdan_normalda_odenmeli_olani_cixan_ferq):
                sonuncu_ay.qiymet = sonuncu_ay.qiymet - artiqdan_normalda_odenmeli_olani_cixan_ferq
                sonuncu_ay.save()
            elif(sonuncu_ay.qiymet == artiqdan_normalda_odenmeli_olani_cixan_ferq):
                sonuncu_ay.delete()
                muqavile.kredit_muddeti = muqavile.kredit_muddeti - 1
                muqavile.save()
            elif(sonuncu_ay.qiymet < artiqdan_normalda_odenmeli_olani_cixan_ferq):
                qalan_mebleg = artiqdan_normalda_odenmeli_olani_cixan_ferq - sonuncu_ay.qiymet
                print(f"qalan_mebleg ===> {qalan_mebleg}")
                sonuncu_ay.delete()
                muqavile.kredit_muddeti = muqavile.kredit_muddeti - 1
                muqavile.save()
                if(sonuncudan_bir_evvelki_ay.qiymet > qalan_mebleg):
                    sonuncudan_bir_evvelki_ay.qiymet = sonuncudan_bir_evvelki_ay.qiymet - qalan_mebleg
                    sonuncudan_bir_evvelki_ay.save()
                if(sonuncudan_bir_evvelki_ay.qiymet == qalan_mebleg):
                    sonuncudan_bir_evvelki_ay.delete()
                    muqavile.kredit_muddeti = muqavile.kredit_muddeti - 1
                    muqavile.save()
            if serializer.is_valid():
                print(f"request.data ===> {request.data}")
                serializer.save()
                return Response({"detail": "Əməliyyat uğurla yerinə yetirildi PATCH"}, status=status.HTTP_200_OK)
        elif(artiq_odeme_alt_status == "ARTIQ_BÜTÜN_AYLAR"):
            indiki_ay = self.get_object()
            print(f"indiki ay ===> {indiki_ay}")
            muqavile = indiki_ay.muqavile
            print(f"muqavile ===> {muqavile}")
            odemek_istediyi_mebleg = float(request.data.get("qiymet"))
            print(f"odemek_istediyi_mebleg ===> {odemek_istediyi_mebleg}")
            normalda_odenmeli_olan = indiki_ay.qiymet
            print(f"normalda_odenmeli_olan ===> {normalda_odenmeli_olan}")

            ilkin_odenis = muqavile.ilkin_odenis
            ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
            ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
            print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
            mehsulun_qiymeti = muqavile.muqavile_umumi_mebleg
            print(f"mehsulun ==> {mehsulun_qiymeti}")

            odenen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status = "ÖDƏNƏN")
            print(f"odenen_odemetarixler ===> {odenen_odemetarixler}")
            odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
            print(f"odenmeyen_odemetarixler ===> {odenmeyen_odemetarixler} --- {len(odenmeyen_odemetarixler)}")

            odediyi = len(odenen_odemetarixler) * indiki_ay.qiymet
            print(f"odediyi ==> {odediyi}")

            qaliq_borc = mehsulun_qiymeti - odediyi - ilkin_odenis_tam
            print(f"qaliq_borc ==> {qaliq_borc}")

            yeni_aylar = qaliq_borc // odemek_istediyi_mebleg
            print(f"yeni_aylar ==> {yeni_aylar}")

            silinecek_ay = len(odenmeyen_odemetarixler) - yeni_aylar
            print(f"silinecek_ay ==> {silinecek_ay}")

            son_aya_elave_edilecek_mebleg = qaliq_borc - ((yeni_aylar-1) * odemek_istediyi_mebleg)
            print(f"son_aya_elave_edilecek_mebleg ==> {son_aya_elave_edilecek_mebleg}")

            indiki_ay.qiymet = odemek_istediyi_mebleg
            indiki_ay.odenme_status = "ARTIQ ÖDƏMƏ"
            indiki_ay.artiq_odeme_alt_status = "ARTIQ_BÜTÜN_AYLAR"
            indiki_ay.save()

            a = 1
            while(a <= silinecek_ay):
                odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1].delete()
                odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
                print(f"odenmeyen_odemetarixler ===> {odenmeyen_odemetarixler} --- {len(odenmeyen_odemetarixler)}")
                a += 1

            print(f"odenmeyen_odemetarixler ===> {odenmeyen_odemetarixler} --- {len(odenmeyen_odemetarixler)}")
            b = 0
            while(b < yeni_aylar):
                if(b == yeni_aylar-1):
                    odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1].qiymet = son_aya_elave_edilecek_mebleg
                    odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1].save()
                else:
                    odenmeyen_odemetarixler[b].qiymet = odemek_istediyi_mebleg
                    odenmeyen_odemetarixler[b].save()
                b += 1

            if serializer.is_valid():
                print(f"request.data ===> {request.data}")
                serializer.save()
                return Response({"detail": "Əməliyyat uğurla yerinə yetirildi PATCH"}, status=status.HTTP_200_OK)
    
    # SON AYIN BOLUNMESI
    elif(odenme_status == "SON AYIN BÖLÜNMƏSİ"):
        indiki_ay = self.get_object()
        print(f"indiki ay ===> {indiki_ay}")
        muqavile = indiki_ay.muqavile
        print(f"muqavile ===> {muqavile}")
        odemek_istediyi_mebleg = float(request.data.get("qiymet"))
        print(f"odemek_istediyi_mebleg ===> {odemek_istediyi_mebleg}")

        odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
        print(f"odenmeyen_odemetarixler ===> {odenmeyen_odemetarixler} --- {len(odenmeyen_odemetarixler)}")

        sonuncu_ay = odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1]

        try:
            if(indiki_ay != sonuncu_ay):
                raise ValidationError(detail={"detail": "Sonuncu ayda deyilsiniz!"}, code=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"detail": "Sonuncu ayda deyilsiniz"}, status=status.HTTP_400_BAD_REQUEST) 

        
        print(f"sonuncu_ay ===> {sonuncu_ay}")
        create_olunacaq_ay_qiymet = sonuncu_ay.qiymet - odemek_istediyi_mebleg
        print(f"create_olunacaq_ay_qiymet ===> {create_olunacaq_ay_qiymet}")

        sonuncu_ay.qiymet = odemek_istediyi_mebleg
        sonuncu_ay.odenme_status = "SON AYIN BÖLÜNMƏSİ"
        sonuncu_ay.save()

        inc_month = pd.date_range(sonuncu_ay.tarix, periods = 2, freq='M')
        print(f"inc_month ===> {inc_month}")

        OdemeTarix.objects.create(
            muqavile = muqavile,
            tarix = f"{inc_month[1].year}-{inc_month[1].month}-{sonuncu_ay.tarix.day}",
            qiymet = create_olunacaq_ay_qiymet
        )

        if serializer.is_valid():
            print(f"request.data ===> {request.data}")
            serializer.save()
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi PATCH"}, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "Yanlış əməliyyat"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    return Response({"detail": "Xəta baş verdi"}, status=status.HTTP_400_BAD_REQUEST)

# UPDATE SORGUSU
def odeme_tarixi_update(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    odenme_status = request.POST.get("odenme_status")
    sertli_odeme_status = request.POST.get("sertli_odeme_status")
    gecikdirme_status = request.POST.get("gecikdirme_status")
    natamama_gore_odeme_status = request.POST.get("natamam_ay_alt_status")
    sifira_gore_odeme_status = request.POST.get("buraxilmis_ay_alt_status")
    artiq_odeme_alt_status = request.POST.get('artiq_odeme_alt_status')

    indiki_ay = self.get_object()
    odemek_istediyi_mebleg = request.POST.get("qiymet")

    today = datetime.date.today()

    muqavile = indiki_ay.muqavile
    print(f"muqavile ==> {muqavile}")
    vanleader = muqavile.vanleader
    musteri = muqavile.musteri
    odenis_uslubu = muqavile.odenis_uslubu
    ofis = muqavile.ofis

    ofis_kassa = get_object_or_404(OfisKassa, ofis=ofis)
    print(f"ofis_kassa ==> {ofis_kassa}")

    print(f"sertli_odeme_status ==> {sertli_odeme_status}")

    print(f"vanleader ==> {vanleader}")
    print(f"musteri ==> {musteri}")
    print(f"odenis_uslubu ==> {odenis_uslubu}")
    print(f"ofis ==> {ofis}")
    print(f"ofis_kassa ==> {ofis_kassa}")

    borcu_bagla_status = request.data.get("borcu_bagla_status")

    def umumi_mebleg(mehsul_qiymeti, mehsul_sayi):
        muqavile_umumi_mebleg = mehsul_qiymeti * mehsul_sayi
        return muqavile_umumi_mebleg
    
    if(borcu_bagla_status == "BORCU BAĞLA"):
        odenmeyen_odemetarixler_qs = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
        odenmeyen_odemetarixler = list(odenmeyen_odemetarixler_qs)
        print(f"odenmeyen_odemetarixler ==> {odenmeyen_odemetarixler} -- {len(odenmeyen_odemetarixler)}")

        ay_ucun_olan_mebleg = 0
        for i in odenmeyen_odemetarixler:
            ay_ucun_olan_mebleg = ay_ucun_olan_mebleg + float(i.qiymet)
            i.qiymet = 0
            i.odenme_status = "ÖDƏNƏN"
            i.save()
        
        muqavile.muqavile_status = "BİTMİŞ"
        muqavile.save()

        qeyd = f"Vanleader - {vanleader.asa}, müştəri - {musteri.asa}, tarix - {today}, ödəniş üslubu - {odenis_uslubu}. Borcu tam bağlandı"
        k_medaxil(ofis_kassa, float(ay_ucun_olan_mebleg), vanleader, qeyd)

        return Response({"detail": "Borc tam bağlandı"}, status=status.HTTP_200_OK)

    # GECIKDIRME ILE BAGLI EMELIYYATLAR
    if(
        (indiki_ay.odenme_status == "ÖDƏNMƏYƏN" and gecikdirme_status == "GECİKDİRMƏ") 
        or 
        (indiki_ay.odenme_status == "ÖDƏNMƏYƏN" and request.POST.get("tarix") != "") 
        or 
        (indiki_ay.odenme_status == "ÖDƏNMƏYƏN" and request.POST.get("tarix") is not None) 
        or 
        (odenme_status == "ÖDƏNMƏYƏN" and gecikdirme_status == "GECİKDİRMƏ") 
        or 
        (odenme_status == "ÖDƏNMƏYƏN" and request.POST.get("tarix") != "")
        or 
        (odenme_status == "ÖDƏNMƏYƏN" and request.POST.get("tarix") is not None)
    ):
        my_time = datetime.datetime.min.time()

        odeme_tarixi_date = indiki_ay.tarix
        odeme_tarixi = datetime.datetime.combine(odeme_tarixi_date, my_time)
        odeme_tarixi_san = datetime.datetime.timestamp(odeme_tarixi)

        gecikdirmek_istediyi_tarix = request.POST.get("tarix")
        gecikdirmek_istediyi_tarix_date = datetime.datetime.strptime(gecikdirmek_istediyi_tarix, "%Y-%m-%d")
        gecikdirmek_istediyi_tarix_san = datetime.datetime.timestamp(gecikdirmek_istediyi_tarix_date)

        odenmeyen_odemetarixler_qs = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
        odenmeyen_odemetarixler = list(odenmeyen_odemetarixler_qs)
        print(f"odenmeyen_odemetarixler ==> {odenmeyen_odemetarixler}")

        if(indiki_ay == odenmeyen_odemetarixler[-1]):
            try:
                if(gecikdirmek_istediyi_tarix_san < odeme_tarixi_san):
                    raise ValidationError(detail={"detail": "Tarixi doğru daxil edin!"}, code=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"detail": "Qeyd etdiyiniz tarix keçmiş tarixdir."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                if(odeme_tarixi_san < gecikdirmek_istediyi_tarix_san):
                    indiki_ay.tarix = gecikdirmek_istediyi_tarix
                    indiki_ay.gecikdirme_status = "GECİKDİRMƏ"
                    indiki_ay.save()
                    return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
            except:
                return Response({"detail": "Yeni tarix hal-hazırki tarix ile növbəti ayın tarixi arasında olmalıdır"}, status=status.HTTP_400_BAD_REQUEST)
        elif(indiki_ay != odenmeyen_odemetarixler[-1]):
            novbeti_ay = OdemeTarix.objects.get(pk = indiki_ay.id+1)
            novbeti_ay_tarix_date = novbeti_ay.tarix
            novbeti_ay_tarix = datetime.datetime.combine(novbeti_ay_tarix_date, my_time)
            novbeti_ay_tarix_san = datetime.datetime.timestamp(novbeti_ay_tarix)

            try:
                if(novbeti_ay_tarix_san == gecikdirmek_istediyi_tarix_san):
                    raise ValidationError(detail={"detail": "Tarixi doğru daxil edin!"}, code=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"detail": "Qeyd etdiyiniz tarix növbəti ayın tarixi ilə eynidir."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                if(gecikdirmek_istediyi_tarix_san < odeme_tarixi_san):
                    raise ValidationError(detail={"detail": "Tarixi doğru daxil edin!"}, code=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"detail": "Qeyd etdiyiniz tarix keçmiş tarixdir."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                if(gecikdirmek_istediyi_tarix_san > novbeti_ay_tarix_san):
                    raise ValidationError(detail={"detail": "Tarixi doğru daxil edin!"}, code=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"detail": "Qeyd etdiyiniz tarix növbəti ayın tarixindən böyükdür."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                if(odeme_tarixi_san < gecikdirmek_istediyi_tarix_san < novbeti_ay_tarix_san):
                    indiki_ay.tarix = gecikdirmek_istediyi_tarix
                    indiki_ay.gecikdirme_status = "GECİKDİRMƏ"
                    indiki_ay.save()
                    return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
            except:
                return Response({"detail": "Yeni tarix hal-hazırki tarix ile növbəti ayın tarixi arasında olmalıdır"}, status=status.HTTP_400_BAD_REQUEST)
    elif(indiki_ay.odenme_status != "ÖDƏNMƏYƏN" and gecikdirme_status == "GECİKDİRMƏ"):
        raise ValidationError(detail={"detail": "Gecikdirmə ancaq ödənməmiş ay üçündür"}, code=status.HTTP_400_BAD_REQUEST)
    
    # Odenen ay ile bagli emeliyyat
    if((indiki_ay.odenme_status == "ÖDƏNMƏYƏN" and float(odemek_istediyi_mebleg) == indiki_ay.qiymet)):
        odenmeyen_odemetarixler_qs = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
        odenmeyen_odemetarixler = list(odenmeyen_odemetarixler_qs)
        print(f"odenmeyen_odemetarixler ==> {odenmeyen_odemetarixler}")

        if serializer.is_valid():
            indiki_ay.odenme_status = "ÖDƏNƏN"
            indiki_ay.save()
            if(indiki_ay == odenmeyen_odemetarixler[-1]):
                muqavile.muqavile_status = "BİTMİŞ"
                muqavile.save()
            
            qeyd = f"Vanleader - {vanleader.asa}, müştəri - {musteri.asa}, tarix - {today}, ödəniş üslubu - {odenis_uslubu}. kredit ödəməsi"
            k_medaxil(ofis_kassa, float(odemek_istediyi_mebleg), vanleader, qeyd)
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        else:
            return ValidationError(detail={"detail": "Məlumatları doğru daxil edin"}, code=status.HTTP_400_BAD_REQUEST)
    # Natamam Ay odeme statusu ile bagli emeliyyatlar
    elif(
        indiki_ay.odenme_status == "ÖDƏNMƏYƏN" 
        and 
        sertli_odeme_status == "NATAMAM AY" 
        and 
        0 < float(odemek_istediyi_mebleg) < indiki_ay.qiymet 
        and 
        natamama_gore_odeme_status != ""
        and 
        natamama_gore_odeme_status is not None
    ):
        ilkin_odenis = muqavile.ilkin_odenis
        ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
        ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
        print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
        mehsulun_qiymeti = muqavile.muqavile_umumi_mebleg
        print(f"mehsulun ==> {mehsulun_qiymeti}")
        indiki_ay.odenme_status = "ÖDƏNƏN"
        indiki_ay.sertli_odeme_status = "NATAMAM AY"
        indiki_ay.save()

        odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
        odemek_istediyi_mebleg = float(request.POST.get("qiymet"))
        
        qeyd = f"Vanleader - {vanleader.asa}, müştəri - {musteri.asa}, tarix - {today}, ödəniş üslubu - {odenis_uslubu}, şərtli ödəmə - {indiki_ay.sertli_odeme_status}"
        k_medaxil(ofis_kassa, float(odemek_istediyi_mebleg), vanleader, qeyd)
        
        if(natamama_gore_odeme_status == "NATAMAM DİGƏR AYLAR"):
            print(f"indiki_ay.qiymet ==> {indiki_ay.qiymet}")
            odenmeyen_pul = indiki_ay.qiymet - odemek_istediyi_mebleg
            print(f"odenmeyen_pul ==> {odenmeyen_pul}")
            odenmeyen_aylar = len(odenmeyen_odemetarixler)
            print(len(odenmeyen_odemetarixler))
            
            aylara_elave_olunacaq_mebleg = odenmeyen_pul // odenmeyen_aylar
            print(f"aylara_elave_olunacaq_mebleg ==> {aylara_elave_olunacaq_mebleg}")
            b = aylara_elave_olunacaq_mebleg * (odenmeyen_aylar-1)
            print(f"b ==> {b}")
            sonuncu_aya_elave_olunacaq_mebleg = odenmeyen_pul - b
            print(f"sonuncu_aya_elave_olunacaq_mebleg ==> {sonuncu_aya_elave_olunacaq_mebleg}")
            
            indiki_ay.qiymet = odemek_istediyi_mebleg
            indiki_ay.natamam_ay_alt_status = "NATAMAM DİGƏR AYLAR"
            indiki_ay.save()

            i = 0
            while(i<=(odenmeyen_aylar-1)):
                print(f"odenmeyen_aylar-1===>{odenmeyen_aylar-1}")
                if(i == (odenmeyen_aylar-1)):
                    odenmeyen_odemetarixler[i].qiymet = odenmeyen_odemetarixler[i].qiymet + sonuncu_aya_elave_olunacaq_mebleg
                    odenmeyen_odemetarixler[i].save()
                else:
                    odenmeyen_odemetarixler[i].qiymet = odenmeyen_odemetarixler[i].qiymet + aylara_elave_olunacaq_mebleg
                    odenmeyen_odemetarixler[i].save()
                i+=1
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        if(natamama_gore_odeme_status == "NATAMAM NÖVBƏTİ AY"):
            indiki_ay = self.get_object()
            natamam_odemek_istediyi_mebleg = indiki_ay.qiymet - odemek_istediyi_mebleg

            novbeti_ay = get_object_or_404(OdemeTarix, pk=self.get_object().id+1)
            novbeti_ay.qiymet = novbeti_ay.qiymet + natamam_odemek_istediyi_mebleg
            novbeti_ay.save()

            indiki_ay.qiymet = odemek_istediyi_mebleg
            indiki_ay.natamam_ay_alt_status = "NATAMAM NÖVBƏTİ AY"
            indiki_ay.save()
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        if(natamama_gore_odeme_status == "NATAMAM SONUNCU AY"):
            indiki_ay = self.get_object()
            natamam_odemek_istediyi_mebleg = indiki_ay.qiymet - odemek_istediyi_mebleg

            sonuncu_ay = odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1]
            print(f"sonuncu_ay ===> {sonuncu_ay}")
            sonuncu_ay.qiymet = sonuncu_ay.qiymet + natamam_odemek_istediyi_mebleg
            sonuncu_ay.save()

            indiki_ay.qiymet = odemek_istediyi_mebleg
            indiki_ay.natamam_ay_alt_status = "NATAMAM SONUNCU AY"
            indiki_ay.save()
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)

    # Buraxilmis Ay odeme statusu ile bagli emeliyyatlar
    elif((sertli_odeme_status == "BURAXILMIŞ AY" and sifira_gore_odeme_status != "") or (float(odemek_istediyi_mebleg) == 0 and sifira_gore_odeme_status != "")):
        indiki_ay = self.get_object()
        muqavile = indiki_ay.muqavile
        ilkin_odenis = muqavile.ilkin_odenis
        ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
        mehsulun_qiymeti = muqavile.muqavile_umumi_mebleg
        print(f"mehsulun ==> {mehsulun_qiymeti}")
        ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
        print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
        indiki_ay.sertli_odeme_status = "BURAXILMIŞ AY"
        indiki_ay.save()
        odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
        odemek_istediyi_mebleg = float(request.POST.get("qiymet"))
        
        if(sifira_gore_odeme_status == "SIFIR NÖVBƏTİ AY"):
            novbeti_ay = get_object_or_404(OdemeTarix, pk=self.get_object().id+1)
            novbeti_ay.qiymet = novbeti_ay.qiymet + indiki_ay.qiymet
            novbeti_ay.save()
            indiki_ay.qiymet = 0
            indiki_ay.sertli_odeme_status = "BURAXILMIŞ AY"
            indiki_ay.buraxilmis_ay_alt_status = "SIFIR NÖVBƏTİ AY"
            indiki_ay.save()
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        if(sifira_gore_odeme_status == "SIFIR SONUNCU AY"):
            sonuncu_ay = odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1]
            sonuncu_ay.qiymet = sonuncu_ay.qiymet + indiki_ay.qiymet
            sonuncu_ay.save()
            indiki_ay.qiymet = 0
            indiki_ay.sertli_odeme_status = "BURAXILMIŞ AY"
            indiki_ay.buraxilmis_ay_alt_status = "SIFIR SONUNCU AY"
            indiki_ay.save()
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        if(sifira_gore_odeme_status == "SIFIR DİGƏR AYLAR"):
            odenmeyen_pul = indiki_ay.qiymet
            print(f"odenmeyen_pul ==> {odenmeyen_pul}")
            odenmeyen_aylar = len(odenmeyen_odemetarixler)
            print(f"odenmeyen_aylar ==> {odenmeyen_aylar}")
            aylara_elave_olunacaq_mebleg = odenmeyen_pul // odenmeyen_aylar
            print(f"aylara_elave_olunacaq_mebleg ==> {aylara_elave_olunacaq_mebleg}")
            a = aylara_elave_olunacaq_mebleg * (odenmeyen_aylar-1)
            sonuncu_aya_elave_olunacaq_mebleg = odenmeyen_pul - a
            print(f"sonuncu_aya_elave_olunacaq_mebleg ==> {sonuncu_aya_elave_olunacaq_mebleg}")
            indiki_ay.qiymet = 0
            indiki_ay.buraxilmis_ay_alt_status = "SIFIR DİGƏR AYLAR"
            indiki_ay.save()
            i = 0
            while(i<=(odenmeyen_aylar-1)):
                if(i == (odenmeyen_aylar-1)):
                    odenmeyen_odemetarixler[i].qiymet = odenmeyen_odemetarixler[i].qiymet + sonuncu_aya_elave_olunacaq_mebleg
                    odenmeyen_odemetarixler[i].save()
                else:
                    odenmeyen_odemetarixler[i].qiymet = odenmeyen_odemetarixler[i].qiymet + aylara_elave_olunacaq_mebleg
                    odenmeyen_odemetarixler[i].save()
                i+=1
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)

    # RAZILASDIRILMIS AZ ODEME ile bagli emeliyyatlar
    elif(sertli_odeme_status == "RAZILAŞDIRILMIŞ AZ ÖDƏMƏ"):
        indiki_ay = self.get_object()
        muqavile = indiki_ay.muqavile
        ilkin_odenis = muqavile.ilkin_odenis
        ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
        ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
        print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
        mehsulun_qiymeti = muqavile.muqavile_umumi_mebleg
        print(f"mehsulun ==> {mehsulun_qiymeti}")
        indiki_ay.sertli_odeme_status = "RAZILAŞDIRILMIŞ AZ ÖDƏMƏ"
        indiki_ay.save()

        odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
        odemek_istediyi_mebleg = float(request.POST.get("qiymet"))

        print(f"indiki_ay.qiymet ==> {indiki_ay.qiymet}")
        odenmeyen_pul = indiki_ay.qiymet - odemek_istediyi_mebleg
        print(f"odenmeyen_pul ==> {odenmeyen_pul}")
        odenmeyen_aylar = len(odenmeyen_odemetarixler)
        print(len(odenmeyen_odemetarixler))
        
        aylara_elave_olunacaq_mebleg = odenmeyen_pul // odenmeyen_aylar
        print(f"aylara_elave_olunacaq_mebleg ==> {aylara_elave_olunacaq_mebleg}")
        b = aylara_elave_olunacaq_mebleg * (odenmeyen_aylar-1)
        print(f"b ==> {b}")
        sonuncu_aya_elave_olunacaq_mebleg = odenmeyen_pul - b
        print(f"sonuncu_aya_elave_olunacaq_mebleg ==> {sonuncu_aya_elave_olunacaq_mebleg}")
        
        indiki_ay.odenme_statusu = "ÖDƏNƏN"
        indiki_ay.qiymet = odemek_istediyi_mebleg
        indiki_ay.save()
        i = 0
        while(i<=(odenmeyen_aylar-1)):
            print(f"odenmeyen_aylar-1===>{odenmeyen_aylar-1}")
            if(i == (odenmeyen_aylar-1)):
                odenmeyen_odemetarixler[i].qiymet = odenmeyen_odemetarixler[i].qiymet + sonuncu_aya_elave_olunacaq_mebleg
                odenmeyen_odemetarixler[i].save()
            else:
                odenmeyen_odemetarixler[i].qiymet = odenmeyen_odemetarixler[i].qiymet + aylara_elave_olunacaq_mebleg
                odenmeyen_odemetarixler[i].save()
            i+=1
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)

    # ARTIQ ODEME ile bagli emeliyyatlar
    elif(sertli_odeme_status == "ARTIQ ÖDƏMƏ"):
        if(artiq_odeme_alt_status == "ARTIQ_BİR_AY"):
            indiki_ay = self.get_object()
            print(f"indiki ay ===> {indiki_ay}")
            muqavile = indiki_ay.muqavile
            print(f"muqavile ===> {muqavile}")
            odemek_istediyi_mebleg = float(request.POST.get("qiymet"))
            print(f"odemek_istediyi_mebleg ===> {odemek_istediyi_mebleg}")
            normalda_odenmeli_olan = indiki_ay.qiymet
            print(f"normalda_odenmeli_olan ===> {normalda_odenmeli_olan}")

            artiqdan_normalda_odenmeli_olani_cixan_ferq = odemek_istediyi_mebleg - normalda_odenmeli_olan
            print(f"artiqdan_normalda_odenmeli_olani_cixan_ferq ===> {artiqdan_normalda_odenmeli_olani_cixan_ferq}")

            odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
            print(f"odenmeyen_odemetarixler ===> {odenmeyen_odemetarixler}")

            indiki_ay.qiymet = odemek_istediyi_mebleg
            indiki_ay.odenme_statusu = "ÖDƏNƏN"
            indiki_ay.sertli_odeme_status = "ARTIQ ÖDƏMƏ"
            indiki_ay.artiq_odeme_alt_status = "ARTIQ_BİR_AY"
            indiki_ay.save()

            sonuncu_ay = odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1]
            print(f"sonuncu_ay ===> {sonuncu_ay}")
            sonuncudan_bir_evvelki_ay = odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-2]
            print(f"sonuncudan_bir_evvelki_ay ===> {sonuncudan_bir_evvelki_ay}")
            
            sonuncu_aydan_qalan = sonuncu_ay.qiymet - artiqdan_normalda_odenmeli_olani_cixan_ferq
            print(f"sonuncu_aydan_qalan ===> {sonuncu_aydan_qalan}")

            if(sonuncu_ay.qiymet > artiqdan_normalda_odenmeli_olani_cixan_ferq):
                sonuncu_ay.qiymet = sonuncu_ay.qiymet - artiqdan_normalda_odenmeli_olani_cixan_ferq
                sonuncu_ay.save()
            elif(sonuncu_ay.qiymet == artiqdan_normalda_odenmeli_olani_cixan_ferq):
                sonuncu_ay.delete()
                muqavile.kredit_muddeti = muqavile.kredit_muddeti - 1
                muqavile.save()
            elif(sonuncu_ay.qiymet < artiqdan_normalda_odenmeli_olani_cixan_ferq):
                qalan_mebleg = artiqdan_normalda_odenmeli_olani_cixan_ferq - sonuncu_ay.qiymet
                print(f"qalan_mebleg ===> {qalan_mebleg}")
                sonuncu_ay.delete()
                muqavile.kredit_muddeti = muqavile.kredit_muddeti - 1
                muqavile.save()
                if(sonuncudan_bir_evvelki_ay.qiymet > qalan_mebleg):
                    sonuncudan_bir_evvelki_ay.qiymet = sonuncudan_bir_evvelki_ay.qiymet - qalan_mebleg
                    sonuncudan_bir_evvelki_ay.save()
                if(sonuncudan_bir_evvelki_ay.qiymet == qalan_mebleg):
                    sonuncudan_bir_evvelki_ay.delete()
                    muqavile.kredit_muddeti = muqavile.kredit_muddeti - 1
                    muqavile.save()
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        elif(artiq_odeme_alt_status == "ARTIQ_BÜTÜN_AYLAR"):
            indiki_ay = self.get_object()
            print(f"indiki ay ===> {indiki_ay}")
            muqavile = indiki_ay.muqavile
            print(f"muqavile ===> {muqavile}")
            odemek_istediyi_mebleg = float(request.POST.get("qiymet"))
            print(f"odemek_istediyi_mebleg ===> {odemek_istediyi_mebleg}")
            normalda_odenmeli_olan = indiki_ay.qiymet
            print(f"normalda_odenmeli_olan ===> {normalda_odenmeli_olan}")

            ilkin_odenis = muqavile.ilkin_odenis
            ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
            ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
            print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
            mehsulun_qiymeti = muqavile.muqavile_umumi_mebleg
            print(f"mehsulun ==> {mehsulun_qiymeti}")

            odenen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status = "ÖDƏNƏN")
            print(f"odenen_odemetarixler ===> {odenen_odemetarixler}")
            odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
            print(f"odenmeyen_odemetarixler ===> {odenmeyen_odemetarixler} --- {len(odenmeyen_odemetarixler)}")

            odediyi = len(odenen_odemetarixler) * indiki_ay.qiymet
            print(f"odediyi ==> {odediyi}")

            qaliq_borc = mehsulun_qiymeti - odediyi - ilkin_odenis_tam
            print(f"qaliq_borc ==> {qaliq_borc}")

            yeni_aylar = qaliq_borc // odemek_istediyi_mebleg
            print(f"yeni_aylar ==> {yeni_aylar}")

            silinecek_ay = len(odenmeyen_odemetarixler) - yeni_aylar
            print(f"silinecek_ay ==> {silinecek_ay}")

            son_aya_elave_edilecek_mebleg = qaliq_borc - ((yeni_aylar-1) * odemek_istediyi_mebleg)
            print(f"son_aya_elave_edilecek_mebleg ==> {son_aya_elave_edilecek_mebleg}")

            indiki_ay.qiymet = odemek_istediyi_mebleg
            indiki_ay.odenme_statusu = "ÖDƏNƏN"
            indiki_ay.sertli_odeme_status = "ARTIQ ÖDƏMƏ"
            indiki_ay.artiq_odeme_alt_status = "ARTIQ_BÜTÜN_AYLAR"
            indiki_ay.save()

            a = 1
            while(a <= silinecek_ay):
                odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1].delete()
                odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
                print(f"odenmeyen_odemetarixler ===> {odenmeyen_odemetarixler} --- {len(odenmeyen_odemetarixler)}")
                a += 1

            print(f"odenmeyen_odemetarixler ===> {odenmeyen_odemetarixler} --- {len(odenmeyen_odemetarixler)}")
            b = 0
            while(b < yeni_aylar):
                if(b == yeni_aylar-1):
                    odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1].qiymet = son_aya_elave_edilecek_mebleg
                    odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1].save()
                else:
                    odenmeyen_odemetarixler[b].qiymet = odemek_istediyi_mebleg
                    odenmeyen_odemetarixler[b].save()
                b += 1

            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    
    # SON AYIN BOLUNMESI
    elif(sertli_odeme_status == "SON AYIN BÖLÜNMƏSİ"):
        indiki_ay = self.get_object()
        print(f"indiki ay ===> {indiki_ay}")
        muqavile = indiki_ay.muqavile
        print(f"muqavile ===> {muqavile}")
        odemek_istediyi_mebleg = float(request.POST.get("qiymet"))
        print(f"odemek_istediyi_mebleg ===> {odemek_istediyi_mebleg}")

        odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
        print(f"odenmeyen_odemetarixler ===> {odenmeyen_odemetarixler} --- {len(odenmeyen_odemetarixler)}")

        sonuncu_ay = odenmeyen_odemetarixler[len(odenmeyen_odemetarixler)-1]

        try:
            if(indiki_ay != sonuncu_ay):
                raise ValidationError(detail={"detail": "Sonuncu ayda deyilsiniz!"}, code=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"detail": "Sonuncu ayda deyilsiniz"}, status=status.HTTP_400_BAD_REQUEST) 

        
        print(f"sonuncu_ay ===> {sonuncu_ay}")
        create_olunacaq_ay_qiymet = sonuncu_ay.qiymet - odemek_istediyi_mebleg
        print(f"create_olunacaq_ay_qiymet ===> {create_olunacaq_ay_qiymet}")

        sonuncu_ay.qiymet = odemek_istediyi_mebleg
        sonuncu_ay.odenme_statusu = "ÖDƏNƏN"
        sonuncu_ay.sertli_odeme_status = "SON AYIN BÖLÜNMƏSİ"
        sonuncu_ay.save()

        inc_month = pd.date_range(sonuncu_ay.tarix, periods = 2, freq='M')
        print(f"inc_month ===> {inc_month}")

        OdemeTarix.objects.create(
            muqavile = muqavile,
            tarix = f"{inc_month[1].year}-{inc_month[1].month}-{sonuncu_ay.tarix.day}",
            qiymet = create_olunacaq_ay_qiymet
        )

        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "Yanlış əməliyyat"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"detail": "Xəta baş verdi"}, status=status.HTTP_400_BAD_REQUEST)