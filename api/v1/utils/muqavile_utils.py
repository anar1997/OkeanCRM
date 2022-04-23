import math
from rest_framework import status
from rest_framework.response import Response
from account.models import User, Musteri
from api.v1.all_serializers.muqavile_serializers import MuqavileSerializer
from company.models import Ofis, OfisKassa, OfisKassaMedaxil, OfisKassaMexaric, Shirket, Shobe, Vezifeler
from maas.models import DealerPrim, MaasGoruntuleme, OfficeLeaderPrim, VanLeaderPrim
from mehsullar.models import (
    Anbar,
    Mehsullar,
    Muqavile,
    OdemeTarix,
    Servis,
    ServisOdeme,
    Stok
)
from rest_framework.generics import get_object_or_404
import pandas as pd
import datetime
import traceback
from mehsullar.signals import create_services

# ----------------------------------------------------------------------------------------------------------------------

def stok_mehsul_ciximi(stok, mehsul_sayi):
    stok.say = stok.say - int(mehsul_sayi)
    stok.save()
    if (stok.say == 0):
        stok.delete()
    return stok.say


def stok_mehsul_elave(stok, mehsul_sayi):
    stok.say = stok.say + int(mehsul_sayi)
    stok.save()
    return stok.say


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


def k_mexaric(company_kassa, daxil_edilecek_mebleg, vanleader, qeyd):
    yekun_balans = float(company_kassa.balans) - float(daxil_edilecek_mebleg)
    company_kassa.balans = yekun_balans
    company_kassa.save()
    tarix = datetime.date.today()

    mexaric = OfisKassaMexaric.objects.create(
        mexaric_eden=vanleader,
        ofis_kassa=company_kassa,
        mebleg=daxil_edilecek_mebleg,
        mexaric_tarixi=tarix,
        qeyd=qeyd
    )
    mexaric.save()
    return mexaric


# ----------------------------------------------------------------------------------------------------------------------

def muqavile_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    user = None
    print(f"login olan user ==> {user}")
    print(f"**********************************{request.data=}**********************************")

    vanleader_id = request.data.get("vanleader_id")
    print(f"vanleader_id ==> {vanleader_id}")

    if (vanleader_id == None):
        user = self.request.user
    else:
        user = get_object_or_404(User, pk=vanleader_id)

    dealer_id = request.data.get("dealer_id")
    print(f"dealer_id ==> {dealer_id}")
    canvesser_id = request.data.get("canvesser_id")
    print(f"canvesser_id ==> {canvesser_id}")

    musteri_id = request.data.get("musteri_id")
    if musteri_id == None:
        return Response({"detail": "Müştəri qeyd olunmayıb"}, status=status.HTTP_400_BAD_REQUEST)
    musteri = get_object_or_404(Musteri, pk=musteri_id)
    print(f"musteri ==> {musteri}")

    dealer = None
    canvesser = None

    if (dealer_id is not None):
        try:
            dealer = get_object_or_404(User, pk=dealer_id)
            print(f"dealer ==> {dealer}")
            if (canvesser_id == None):
                canvesser = dealer
                print(f"canvesser ==> {canvesser}")
        except:
            return Response({"detail": "Dealer tapılmadı"}, status=status.HTTP_400_BAD_REQUEST)

    if (canvesser_id is not None):
        try:
            canvesser = get_object_or_404(User, pk=canvesser_id)
            print(f"canvesser ==> {canvesser}")
            if (dealer_id == None):
                dealer = canvesser
                print(f"dealer ==> {dealer}")
        except:
            return Response({"detail": "Canvesser tapılmadı"}, status=status.HTTP_400_BAD_REQUEST)

    my_time = datetime.datetime.min.time()

    indiki_tarix_date = datetime.date.today()
    indiki_tarix = datetime.datetime.combine(indiki_tarix_date, my_time)
    indiki_tarix_san = datetime.datetime.timestamp(indiki_tarix)
    print(f"indiki_tarix_san ===> {indiki_tarix_san}")

    if (request.data.get("ilkin_odenis_tarixi") is not None):
        ilkin_odenis_tarixi = request.data.get("ilkin_odenis_tarixi")
        ilkin_odenis_tarixi_date = datetime.datetime.strptime(
            ilkin_odenis_tarixi, "%Y-%m-%d")
        ilkin_odenis_tarixi_san = datetime.datetime.timestamp(
            ilkin_odenis_tarixi_date)
        print(f"ilkin_odenis_tarixi_san ===> {ilkin_odenis_tarixi_san}")

    if (request.data.get("ilkin_odenis_qaliq_tarixi") is not None):
        ilkin_odenis_qaliq_tarixi = request.data.get(
            "ilkin_odenis_qaliq_tarixi")
        ilkin_odenis_qaliq_tarixi_date = datetime.datetime.strptime(
            ilkin_odenis_qaliq_tarixi, "%Y-%m-%d")
        ilkin_odenis_qaliq_tarixi_san = datetime.datetime.timestamp(
            ilkin_odenis_qaliq_tarixi_date)
        print(
            f"ilkin_odenis_qaliq_tarixi_san ===> {ilkin_odenis_qaliq_tarixi_san}")

    if (request.data.get("negd_odenis_1_tarix") is not None):
        negd_odenis_1_tarix = request.data.get("negd_odenis_1_tarix")
        negd_odenis_1_tarix_date = datetime.datetime.strptime(
            negd_odenis_1_tarix, "%Y-%m-%d")
        negd_odenis_1_tarix_san = datetime.datetime.timestamp(
            negd_odenis_1_tarix_date)
        print(f"negd_odenis_1_tarix_san ===> {negd_odenis_1_tarix_san}")

    if (request.data.get("negd_odenis_2_tarix") is not None):
        negd_odenis_2_tarix = request.data.get("negd_odenis_2_tarix")
        negd_odenis_2_tarix_date = datetime.datetime.strptime(
            negd_odenis_2_tarix, "%Y-%m-%d")
        negd_odenis_2_tarix_san = datetime.datetime.timestamp(
            negd_odenis_2_tarix_date)
        print(f"negd_odenis_2_tarix_san ===> {negd_odenis_2_tarix_san}")

    mehsul_id_str = request.data.get("mehsul_id")
    if (mehsul_id_str == None):
        print("Mehsul daxil edilmeyib")
        return Response({"detail": "Müqavilə imzalamaq üçün mütləq məhsul daxil edilməlidir."},
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        mehsul_id = int(mehsul_id_str)

    print(f"mehsul id ==> {mehsul_id}")
    mehsul = get_object_or_404(Mehsullar, pk=mehsul_id)
    print(f"mehsul ==> {mehsul}")

    mehsul_sayi = request.data.get("mehsul_sayi")
    if (mehsul_sayi == None):
        mehsul_sayi = 1
    print(f"mehsul_sayi ==> {mehsul_sayi}")

    odenis_uslubu = request.data.get("odenis_uslubu")
    print(f"odenis_uslubu ==> {odenis_uslubu}")

    ilkin_odenis = request.data.get("ilkin_odenis")
    print(f"ilkin_odenis ==> {ilkin_odenis} --- {type(ilkin_odenis)}")

    ilkin_odenis_qaliq = request.data.get("ilkin_odenis_qaliq")
    print(
        f"ilkin_odenis_qaliq ==> {ilkin_odenis_qaliq} --- {type(ilkin_odenis_qaliq)}")

    def umumi_mebleg(mehsul_qiymeti, mehsul_sayi):
        muqavile_umumi_mebleg = mehsul_qiymeti * mehsul_sayi
        return muqavile_umumi_mebleg

    if (mehsul_sayi == None):
        mehsul_sayi = 1

    muqavile_umumi_mebleg = umumi_mebleg(mehsul.qiymet, int(mehsul_sayi))

    ofis_id = request.data.get("ofis_id") 
    print(f"{ofis_id}")

    shirket_id = request.data.get("shirket_id") 
    print(f"{shirket_id}")

    shobe_id = request.data.get("shobe_id") 
    print(f"{shobe_id}")

    kredit_muddeti = request.data.get("kredit_muddeti")

    if (user.ofis == None):
        ofis = Ofis.objects.get(pk=ofis_id)
    else:
        ofis = user.ofis
    print(f"************************************** {ofis=}")
    if (user.shirket == None):
        shirket = mehsul.shirket
    else:
        shirket = user.shirket

    if (shobe_id is not None):
        shobe = Shobe.objects.get(pk=shobe_id)
    else:
        shobe = user.shobe

    try:
        anbar = get_object_or_404(Anbar, ofis=ofis)
        print(f"{anbar=}")
    except:
        traceback.print_exc()
        return Response({"detail": "Anbar tapılmadı"}, status=status.HTTP_400_BAD_REQUEST)

    print(f"anbar ==> {anbar}")
    print(f"ofis ==> {ofis}")

    ofis_kassa = get_object_or_404(OfisKassa, ofis=ofis)
    print(f"ofis_kassa ==> {ofis_kassa}")

    ofis_kassa_balans = ofis_kassa.balans
    print(f"ofis_kassa_balans ==> {ofis_kassa_balans}")

    try:
        try:
            stok = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul)
            print(f"{stok.say} {type(stok.say)}")
        except:
            return Response({"detail": "Stokda yetəri qədər məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
        print(f"{mehsul_sayi} {type(mehsul_sayi)}")
        if (stok.say < int(mehsul_sayi)):
            return Response({"detail": "Stokda yetəri qədər məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)

        print(serializer.is_valid())
        if (serializer.is_valid()):
            if (mehsul_sayi == None):
                mehsul_sayi = 1
            print("Burdayam")
            # Kredit
            if (odenis_uslubu == "KREDİT"):
                if (kredit_muddeti == None):
                    # Kredit muddeti daxil edilmezse
                    print("Burdayam1")
                    return Response({"detail": "Ödəmə statusu kreditdir amma kredit müddəti daxil edilməyib"},
                                    status=status.HTTP_400_BAD_REQUEST)
                elif (int(kredit_muddeti) == 0):
                    # Kredit muddeyi 0 daxil edilerse
                    print("Burdayam2")
                    return Response({"detail": "Ödəmə statusu kreditdir amma kredit müddəti 0 daxil edilib"},
                                    status=status.HTTP_400_BAD_REQUEST)
                elif (int(kredit_muddeti) == 31):
                    # Kredit muddeti 31 ay daxil edilerse
                    print("Burdayam3")
                    return Response({"detail": "Maksimum kredit müddəti 30 aydır"}, status=status.HTTP_400_BAD_REQUEST)
                elif (int(kredit_muddeti) > 0):
                    # Kredit muddeti 0-dan boyuk olarsa

                    if ((ilkin_odenis is not None) and (request.data.get("ilkin_odenis_tarixi") == None)):
                        return Response(
                            {"detail": "İlkin ödəniş məbləği qeyd olunub amma ilkin ödəniş tarixi qeyd olunmayıb"},
                            status=status.HTTP_400_BAD_REQUEST)

                    if ((ilkin_odenis_qaliq is not None) and (request.data.get("ilkin_odenis_qaliq_tarixi") == None)):
                        return Response({
                            "detail": "Qalıq İlkin ödəniş məbləği qeyd olunub amma qalıq ilkin ödəniş tarixi qeyd olunmayıb"},
                            status=status.HTTP_400_BAD_REQUEST)

                    print("Burdayam4")
                    if (ilkin_odenis == None and ilkin_odenis_qaliq == None):
                        # Ilkin odenis daxil edilmezse
                        print("Burdayam5")
                        stok_mehsul_ciximi(stok, int(mehsul_sayi))
                        muqavile_umumi_mebleg = umumi_mebleg(
                            mehsul.qiymet, int(mehsul_sayi))
                        print(
                            f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg}")

                        serializer.save(vanleader=user, dealer=dealer, canvesser=canvesser, shirket=shirket, ofis=ofis,
                                        shobe=shobe, muqavile_umumi_mebleg=muqavile_umumi_mebleg)
                        return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"},
                                        status=status.HTTP_201_CREATED)
                    elif (ilkin_odenis is not None and ilkin_odenis_qaliq == None):
                        # Umumi ilkin odenis meblegi daxil edilerse ve qaliq ilkin odenis meblegi daxil edilmezse
                        print("Burdayam7")
                        if (indiki_tarix_san == ilkin_odenis_tarixi_san):
                            print("Burdayam8")
                            stok_mehsul_ciximi(stok, int(mehsul_sayi))
                            muqavile_umumi_mebleg = umumi_mebleg(
                                mehsul.qiymet, int(mehsul_sayi))

                            qeyd = f"Vanleader - {user.asa}, müştəri - {musteri.asa}, tarix - {ilkin_odenis_tarixi}, ödəniş üslubu - {odenis_uslubu}, tam ilkin ödəniş"
                            k_medaxil(ofis_kassa, float(
                                ilkin_odenis), user, qeyd)

                            serializer.save(vanleader=user, dealer=dealer, canvesser=canvesser, shirket=shirket,
                                            ofis=ofis, shobe=shobe, ilkin_odenis=ilkin_odenis,
                                            ilkin_odenis_status="BİTMİŞ", muqavile_umumi_mebleg=muqavile_umumi_mebleg)
                            return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"},
                                            status=status.HTTP_201_CREATED)
                        elif (indiki_tarix_san < ilkin_odenis_tarixi_san):
                            print("Burdayam9")
                            stok_mehsul_ciximi(stok, int(mehsul_sayi))
                            muqavile_umumi_mebleg = umumi_mebleg(
                                mehsul.qiymet, int(mehsul_sayi))

                            serializer.save(vanleader=user, dealer=dealer, canvesser=canvesser, shirket=shirket,
                                            ofis=ofis, shobe=shobe, ilkin_odenis=ilkin_odenis,
                                            ilkin_odenis_status="DAVAM EDƏN",
                                            muqavile_umumi_mebleg=muqavile_umumi_mebleg)
                            return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"},
                                            status=status.HTTP_201_CREATED)
                        elif (indiki_tarix_san > ilkin_odenis_tarixi_san):
                            print("Burdayam10")
                            return Response({"detail": "İlkin ödəniş tarixini keçmiş tarixə təyin edə bilməzsiniz"},
                                            status=status.HTTP_400_BAD_REQUEST)

                        return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"},
                                        status=status.HTTP_201_CREATED)

                    elif ((ilkin_odenis == None and ilkin_odenis_qaliq is not None) or (
                            float(ilkin_odenis) == 0 and ilkin_odenis_qaliq is not None)):
                        return Response({"detail": "İlkin ödəniş daxil edilmən qalıq ilkin ödəniş daxil edilə bilməz"},
                                        status=status.HTTP_400_BAD_REQUEST)

                    elif (float(ilkin_odenis) == 0):
                        print("Burdayam17")
                        # Umumi ilkin odenis meblegi 0 olarsa
                        return Response({"detail": "İlkin ödəniş 0 azn daxil edilə bilməz"},
                                        status=status.HTTP_400_BAD_REQUEST)
                    elif (ilkin_odenis_qaliq is not None):
                        print("Burdayam 19")
                        if ((indiki_tarix_san == ilkin_odenis_tarixi_san) and (
                                indiki_tarix_san < ilkin_odenis_qaliq_tarixi_san)):
                            print("Burdayam21")
                            stok_mehsul_ciximi(stok, int(mehsul_sayi))
                            print("Burdayam 21")
                            muqavile_umumi_mebleg = umumi_mebleg(
                                mehsul.qiymet, int(mehsul_sayi))
                            print(
                                f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg}")

                            qeyd = f"Vanleader - {user.asa}, müştəri - {musteri.asa}, tarix - {ilkin_odenis_tarixi}, ödəniş üslubu - {odenis_uslubu}, 2-dəfəyə ilkin ödənişin birincisi."
                            k_medaxil(ofis_kassa, float(
                                ilkin_odenis), user, qeyd)

                            serializer.save(vanleader=user, dealer=dealer, canvesser=canvesser, shirket=shirket,
                                            ofis=ofis, shobe=shobe, ilkin_odenis=ilkin_odenis,
                                            ilkin_odenis_qaliq=ilkin_odenis_qaliq, ilkin_odenis_status="BİTMİŞ",
                                            qaliq_ilkin_odenis_status="DAVAM EDƏN",
                                            muqavile_umumi_mebleg=muqavile_umumi_mebleg)
                            print("Burdayam 21")
                            return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"},
                                            status=status.HTTP_201_CREATED)

                        elif ((indiki_tarix_san == ilkin_odenis_tarixi_san) and (
                                ilkin_odenis_tarixi_san == ilkin_odenis_qaliq_tarixi_san)):
                            print("Burdayam 22")
                            return Response({
                                "detail": "İlkin ödəniş qalıq və ilkin ödəniş hər ikisi bu günki tarixə qeyd oluna bilməz"},
                                status=status.HTTP_400_BAD_REQUEST)
                        elif (indiki_tarix_san == ilkin_odenis_qaliq_tarixi_san):
                            print("Burdayam 23")
                            return Response({"detail": "İlkin ödəniş qalıq bu günki tarixə qeyd oluna bilməz"},
                                            status=status.HTTP_400_BAD_REQUEST)
                        elif (ilkin_odenis_tarixi_san > ilkin_odenis_qaliq_tarixi_san):
                            print("Burdayam 23.5")
                            return Response(
                                {"detail": "İlkin ödəniş qalıq tarixi ilkin ödəniş tarixindən əvvəl ola bilməz"},
                                status=status.HTTP_400_BAD_REQUEST)
                        elif (ilkin_odenis_tarixi_san == ilkin_odenis_qaliq_tarixi_san):
                            print("Burdayam 24")
                            return Response({
                                "detail": "İlkin ödəniş qalıq və ilkin ödəniş hər ikisi eyni tarixə qeyd oluna bilməz"},
                                status=status.HTTP_400_BAD_REQUEST)
                        elif ((indiki_tarix_san > ilkin_odenis_tarixi_san) or (
                                indiki_tarix_san > ilkin_odenis_qaliq_tarixi_san)):
                            print("Burdayam 25")
                            return Response({"detail": "İlkin ödəniş tarixini keçmiş tarixə təyin edə bilməzsiniz"},
                                            status=status.HTTP_400_BAD_REQUEST)

                        elif (indiki_tarix_san < ilkin_odenis_tarixi_san):
                            print("Burdayam 26")
                            stok_mehsul_ciximi(stok, int(mehsul_sayi))
                            print("Bura 12 ishe dushdu")
                            muqavile_umumi_mebleg = umumi_mebleg(
                                mehsul.qiymet, int(mehsul_sayi))
                            print(
                                f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg}")

                            serializer.save(vanleader=user, dealer=dealer, canvesser=canvesser, shirket=shirket,
                                            ofis=ofis, shobe=shobe, ilkin_odenis=ilkin_odenis,
                                            ilkin_odenis_qaliq=ilkin_odenis_qaliq, ilkin_odenis_status="DAVAM EDƏN",
                                            qaliq_ilkin_odenis_status="DAVAM EDƏN",
                                            muqavile_umumi_mebleg=muqavile_umumi_mebleg)
                            print("Burdayam 11")
                            return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"},
                                            status=status.HTTP_201_CREATED)
                        elif ((indiki_tarix_san < ilkin_odenis_tarixi_san) and (
                                indiki_tarix_san < ilkin_odenis_qaliq_tarixi_san)):
                            print("Burdayam 27")
                            stok_mehsul_ciximi(stok, int(mehsul_sayi))
                            print("Bura 27 ishe dushdu")
                            muqavile_umumi_mebleg = umumi_mebleg(
                                mehsul.qiymet, int(mehsul_sayi))
                            print(
                                f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg}")

                            serializer.save(vanleader=user, dealer=dealer, canvesser=canvesser, shirket=shirket,
                                            ofis=ofis, shobe=shobe, ilkin_odenis=ilkin_odenis,
                                            ilkin_odenis_qaliq=ilkin_odenis_qaliq, ilkin_odenis_status="DAVAM EDƏN",
                                            qaliq_ilkin_odenis_status="DAVAM EDƏN",
                                            muqavile_umumi_mebleg=muqavile_umumi_mebleg)
                            print("Burdayam 27")
                            return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"},
                                            status=status.HTTP_201_CREATED)

                        return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"},
                                        status=status.HTTP_201_CREATED)
                    else:
                        print("Burdayam 30")
                        return Response({"detail": "Qalıq ilkin ödəniş doğru daxil edilməyib."},
                                        status=status.HTTP_400_BAD_REQUEST)

            # Negd odenis
            elif (odenis_uslubu == "NƏĞD" and request.data.get("negd_odenis_1") == None and request.data.get(
                    "negd_odenis_2") == None):
                if (kredit_muddeti is not None):
                    return Response({"detail": "Kredit müddəti ancaq status kredit olan müqavilələr üçündür"},
                                    status=status.HTTP_400_BAD_REQUEST)
                if (ilkin_odenis is not None or ilkin_odenis_qaliq is not None):
                    return Response({"detail": "İlkin ödəniş ancaq status kredit olan müqavilələr üçündür"},
                                    status=status.HTTP_400_BAD_REQUEST)
                if (mehsul_sayi == None):
                    mehsul_sayi = 1

                stok_mehsul_ciximi(stok, int(mehsul_sayi))
                muqavile_umumi_mebleg = umumi_mebleg(
                    mehsul.qiymet, int(mehsul_sayi))
                print(f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg}")
                print(f"user asa ---> {user.asa}")
                print(f"musteri asa ---> {musteri.asa}")

                qeyd = f"Vanleader - {user.asa}, müştəri - {musteri.asa}, tarix - {indiki_tarix_date}, ödəniş üslubu - {odenis_uslubu}"
                print(qeyd)
                k_medaxil(ofis_kassa, float(muqavile_umumi_mebleg), user, qeyd)

                serializer.save(vanleader=user, dealer=dealer, canvesser=canvesser, shirket=shirket, ofis=ofis,
                                muqavile_status="BİTMİŞ", shobe=shobe, muqavile_umumi_mebleg=muqavile_umumi_mebleg)
                return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)

            # 2 defeye negd odenis
            elif (request.data.get("negd_odenis_1") is not None and request.data.get("negd_odenis_2") is not None):
                if (float(request.data.get("negd_odenis_1")) < muqavile_umumi_mebleg):
                    if (mehsul_sayi == None):
                        mehsul_sayi = 1
                    print("Burdayam")
                    if (kredit_muddeti is not None):
                        print("Burdayam 16")
                        return Response({"detail": "Kredit müddəti ancaq status kredit olan müqavilələr üçündür"},
                                        status=status.HTTP_400_BAD_REQUEST)

                    negd_odenis_1 = request.data.get("negd_odenis_1")
                    print(
                        f"negd_odenis_1 ==> {negd_odenis_1} {type(negd_odenis_1)}")
                    negd_odenis_2 = request.data.get("negd_odenis_2")
                    print(
                        f"negd_odenis_2 ==> {negd_odenis_1} {type(negd_odenis_2)}")
                    muqavile_umumi_mebleg = umumi_mebleg(
                        mehsul.qiymet, int(mehsul_sayi))
                    print(
                        f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg} --- {type(muqavile_umumi_mebleg)}")

                    if (negd_odenis_1 == None or negd_odenis_2 == None or negd_odenis_1 == "0" or negd_odenis_2 == "0"):
                        print("In1")
                        return Response(
                            {"detail": "2 dəfəyə nəğd ödəniş statusunda hər 2 nəğd ödəniş qeyd olunmalıdır"},
                            status=status.HTTP_400_BAD_REQUEST)
                    elif float(negd_odenis_1) > muqavile_umumi_mebleg or float(negd_odenis_2) > muqavile_umumi_mebleg:
                        return Response({"detail": "Daxil etdiyiniz məbləğ müqavilənin ümumi məbləğindən daha çoxdur"},
                                        status=status.HTTP_400_BAD_REQUEST)
                    elif float(negd_odenis_1) + float(negd_odenis_2) == muqavile_umumi_mebleg:
                        if ((indiki_tarix_san == negd_odenis_1_tarix_san) and (
                                indiki_tarix_san < negd_odenis_2_tarix_san)):
                            print("In2")
                            stok_mehsul_ciximi(stok, int(mehsul_sayi))

                            qeyd = f"Vanleader - {user.asa}, müştəri - {musteri.asa}, tarix - {negd_odenis_1_tarix}, ödəniş üslubu - {odenis_uslubu}, 1-ci nəğd ödəniş"
                            k_medaxil(ofis_kassa, float(
                                negd_odenis_1), user, qeyd)

                            serializer.save(vanleader=user, dealer=dealer, canvesser=canvesser, shirket=shirket,
                                            ofis=ofis, shobe=shobe, odenis_uslubu="İKİ DƏFƏYƏ NƏĞD",
                                            negd_odenis_1_status="BİTMİŞ", negd_odenis_2_status="DAVAM EDƏN",
                                            muqavile_umumi_mebleg=muqavile_umumi_mebleg)
                            return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"},
                                            status=status.HTTP_201_CREATED)

                        elif ((indiki_tarix_san == negd_odenis_1_tarix_san) and (
                                negd_odenis_1_tarix_san == negd_odenis_2_tarix_san)):
                            print("Burdayam 22")
                            return Response({"detail": "Ödənişlərin hər ikisi bu günki tarixə qeyd oluna bilməz"},
                                            status=status.HTTP_400_BAD_REQUEST)

                        elif (indiki_tarix_san == negd_odenis_2_tarix_san):
                            print("Burdayam 23")
                            return Response({"detail": "Qalıq nəğd ödəniş bu günki tarixə qeyd oluna bilməz"},
                                            status=status.HTTP_400_BAD_REQUEST)

                        elif (negd_odenis_1_tarix_san > negd_odenis_2_tarix_san):
                            print("Burdayam 23.5")
                            return Response(
                                {"detail": "Qalıq nəğd ödəniş tarixi nəğd ödəniş tarixindən əvvəl ola bilməz"},
                                status=status.HTTP_400_BAD_REQUEST)

                        elif (negd_odenis_1_tarix_san == negd_odenis_2_tarix_san):
                            print("Burdayam 24")
                            return Response(
                                {"detail": "Qalıq nəğd ödəniş və nəğd ödəniş hər ikisi eyni tarixə qeyd oluna bilməz"},
                                status=status.HTTP_400_BAD_REQUEST)

                        elif ((indiki_tarix_san > negd_odenis_1_tarix_san) or (
                                indiki_tarix_san > negd_odenis_2_tarix_san)):
                            print("Burdayam 25")
                            return Response({"detail": "Nəğd ödəniş tarixini keçmiş tarixə təyin edə bilməzsiniz"},
                                            status=status.HTTP_400_BAD_REQUEST)

                        elif ((indiki_tarix_san < negd_odenis_1_tarix_san) and (
                                indiki_tarix_san < negd_odenis_2_tarix_san)):
                            stok_mehsul_ciximi(stok, int(mehsul_sayi))

                            serializer.save(vanleader=user, dealer=dealer, canvesser=canvesser, shirket=shirket,
                                            ofis=ofis, shobe=shobe, odenis_uslubu="İKİ DƏFƏYƏ NƏĞD",
                                            negd_odenis_1_status="DAVAM EDƏN", negd_odenis_2_status="DAVAM EDƏN",
                                            muqavile_umumi_mebleg=muqavile_umumi_mebleg)
                            return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"},
                                            status=status.HTTP_201_CREATED)

                    elif (float(negd_odenis_1) + float(negd_odenis_2) != muqavile_umumi_mebleg):
                        print("In3")
                        return Response({"detail": "Ödəmək istədiyiniz məbləğlər məhsulun qiymətinə bərabər deyil"},
                                        status=status.HTTP_400_BAD_REQUEST)

            elif (request.data.get("negd_odenis_1") is not None and request.data.get("negd_odenis_2") == None):
                return Response({"detail": "Nəğd ödəniş 2 daxil edilməyib"}, status=status.HTTP_400_BAD_REQUEST)

            elif (odenis_uslubu == "İKİ DƏFƏYƏ NƏĞD"):
                if (mehsul_sayi == None):
                    mehsul_sayi = 1
                print("Burdayam")
                if (kredit_muddeti is not None):
                    print("Burdayam 16")
                    return Response({"detail": "Kredit müddəti ancaq status kredit olan müqavilələr üçündür"},
                                    status=status.HTTP_400_BAD_REQUEST)

                negd_odenis_1 = request.data.get("negd_odenis_1")
                print(
                    f"negd_odenis_1 ==> {negd_odenis_1} {type(negd_odenis_1)}")
                negd_odenis_2 = request.data.get("negd_odenis_2")
                print(
                    f"negd_odenis_2 ==> {negd_odenis_2} {type(negd_odenis_2)}")
                muqavile_umumi_mebleg = umumi_mebleg(
                    mehsul.qiymet, int(mehsul_sayi))
                print(
                    f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg} --- {type(muqavile_umumi_mebleg)}")

                if (negd_odenis_1 == None or negd_odenis_2 == None or negd_odenis_1 == "0" or negd_odenis_2 == "0"):
                    print("In1")
                    return Response({"detail": "2 dəfəyə nəğd ödəniş statusunda hər 2 nəğd ödəniş qeyd olunmalıdır"},
                                    status=status.HTTP_400_BAD_REQUEST)
                elif (float(negd_odenis_1) > muqavile_umumi_mebleg):
                    return Response({"detail": "Daxil etdiyiniz məbləğ müqavilənin ümumi məbləğindən daha çoxdur"},
                                    status=status.HTTP_400_BAD_REQUEST)

                elif (float(negd_odenis_2) > muqavile_umumi_mebleg):
                    return Response({"detail": "Daxil etdiyiniz məbləğ müqavilənin ümumi məbləğindən daha çoxdur"},
                                    status=status.HTTP_400_BAD_REQUEST)
                elif (float(negd_odenis_1) + float(negd_odenis_2) == muqavile_umumi_mebleg):

                    if ((indiki_tarix_san == negd_odenis_1_tarix_san) and (indiki_tarix_san < negd_odenis_2_tarix_san)):
                        print("In2")
                        stok_mehsul_ciximi(stok, int(mehsul_sayi))

                        qeyd = f"Vanleader - {user.asa}, müştəri - {musteri.asa}, tarix - {negd_odenis_1_tarix}, ödəniş üslubu - {odenis_uslubu}, 1-ci nəğd ödəniş"
                        k_medaxil(ofis_kassa, float(negd_odenis_1), user, qeyd)

                        serializer.save(vanleader=user, dealer=dealer, canvesser=canvesser, shirket=shirket, ofis=ofis,
                                        shobe=shobe, negd_odenis_1_status="BİTMİŞ", negd_odenis_2_status="DAVAM EDƏN",
                                        muqavile_umumi_mebleg=muqavile_umumi_mebleg)
                        return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"},
                                        status=status.HTTP_201_CREATED)

                    elif ((indiki_tarix_san == negd_odenis_1_tarix_san) and (
                            negd_odenis_1_tarix_san == negd_odenis_2_tarix_san)):
                        print("Burdayam 22")
                        return Response({"detail": "Ödənişlərin hər ikisi bu günki tarixə qeyd oluna bilməz"},
                                        status=status.HTTP_400_BAD_REQUEST)

                    elif (indiki_tarix_san == negd_odenis_2_tarix_san):
                        print("Burdayam 23")
                        return Response({"detail": "Qalıq nəğd ödəniş bu günki tarixə qeyd oluna bilməz"},
                                        status=status.HTTP_400_BAD_REQUEST)

                    elif (negd_odenis_1_tarix_san > negd_odenis_2_tarix_san):
                        print("Burdayam 23.5")
                        return Response({"detail": "Qalıq nəğd ödəniş tarixi nəğd ödəniş tarixindən əvvəl ola bilməz"},
                                        status=status.HTTP_400_BAD_REQUEST)

                    elif (negd_odenis_1_tarix_san == negd_odenis_2_tarix_san):
                        print("Burdayam 24")
                        return Response(
                            {"detail": "Qalıq nəğd ödəniş və nəğd ödəniş hər ikisi eyni tarixə qeyd oluna bilməz"},
                            status=status.HTTP_400_BAD_REQUEST)

                    elif ((indiki_tarix_san > negd_odenis_1_tarix_san) or (indiki_tarix_san > negd_odenis_2_tarix_san)):
                        print("Burdayam 25")
                        return Response({"detail": "Nəğd ödəniş tarixini keçmiş tarixə təyin edə bilməzsiniz"},
                                        status=status.HTTP_400_BAD_REQUEST)

                    elif ((indiki_tarix_san < negd_odenis_1_tarix_san) and (
                            indiki_tarix_san < negd_odenis_2_tarix_san)):
                        stok_mehsul_ciximi(stok, int(mehsul_sayi))

                        serializer.save(vanleader=user, dealer=dealer, canvesser=canvesser, shirket=shirket, ofis=ofis,
                                        shobe=shobe, negd_odenis_1_status="DAVAM EDƏN",
                                        negd_odenis_2_status="DAVAM EDƏN", muqavile_umumi_mebleg=muqavile_umumi_mebleg)
                        return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"},
                                        status=status.HTTP_201_CREATED)

                elif (float(negd_odenis_1) + float(negd_odenis_2) != muqavile_umumi_mebleg):
                    print("In3")
                    return Response({"detail": "Ödəmək istədiyiniz məbləğlər məhsulun qiymətinə bərabər deyil"},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"detail": "Məlumatları doğru daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        traceback.print_exc()
        return Response({"detail": "Xəta baş verdi, məlumatları doğru daxil etdiyinizdən əmin olun"}, status=status.HTTP_400_BAD_REQUEST)
        

def muqavile_patch(self, request, *args, **kwargs):
    try:
        muqavile = self.get_object()
        serializer = MuqavileSerializer(muqavile, data=request.data, partial=True)
        print(f"muqavile ===> {muqavile}")

        ilkin_odenis = muqavile.ilkin_odenis
        print(f"ilkin_odenis ===> {ilkin_odenis}")
        ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
        print(f"ilkin_odenis_qaliq ===> {ilkin_odenis_qaliq}")

        ilkin_odenis_status = muqavile.ilkin_odenis_status
        print(f"ilkin_odenis_status ===> {ilkin_odenis_status}")

        qaliq_ilkin_odenis_status = muqavile.qaliq_ilkin_odenis_status
        print(f"qaliq_ilkin_odenis_status ===> {qaliq_ilkin_odenis_status}")

        odemek_istediyi_ilkin_odenis = request.data.get("ilkin_odenis")
        print(f"odemek_istediyi_ilkin_odenis ===> {odemek_istediyi_ilkin_odenis}")

        odemek_istediyi_qaliq_ilkin_odenis = request.data.get("ilkin_odenis_qaliq")
        print(
            f"odemek_istediyi_qaliq_ilkin_odenis ===> {odemek_istediyi_qaliq_ilkin_odenis}")

        negd_odenis_1 = muqavile.negd_odenis_1
        print(f"negd_odenis_1 ===> {negd_odenis_1}")
        negd_odenis_2 = muqavile.negd_odenis_2
        print(f"negd_odenis_2 ===> {negd_odenis_2}")

        negd_odenis_1_status = muqavile.negd_odenis_1_status
        print(f"negd_odenis_1_status ===> {negd_odenis_1_status}")

        negd_odenis_2_status = muqavile.negd_odenis_2_status
        print(f"negd_odenis_2_status ===> {negd_odenis_2_status}")

        muqavile_status = muqavile.muqavile_status
        print(f"muqavile_status ===> {muqavile_status}")

        odemek_istediyi_negd_odenis_1 = request.data.get("negd_odenis_1")
        print(
            f"odemek_istediyi_negd_odenis_1 ===> {odemek_istediyi_negd_odenis_1}")

        odemek_istediyi_negd_odenis_2 = request.data.get("negd_odenis_2")
        print(
            f"odemek_istediyi_negd_odenis_2 ===> {odemek_istediyi_negd_odenis_2}")

        my_time = datetime.datetime.min.time()

        indiki_tarix_date = datetime.date.today()
        indiki_tarix = datetime.datetime.combine(indiki_tarix_date, my_time)
        indiki_tarix_san = datetime.datetime.timestamp(indiki_tarix)
        print(f"indiki_tarix_san ===> {indiki_tarix_san}")

        dusen_muqavile_status = request.data.get("muqavile_status")
        print(f"dusen_muqavile_status ===> {dusen_muqavile_status}")

        mehsul = muqavile.mehsul
        print(f"mehsul ==> {mehsul}")

        mehsul_sayi = muqavile.mehsul_sayi
        print(f"mehsul_sayi ==> {mehsul_sayi}")

        muqavile_vanleader = muqavile.vanleader
        print(f"muqavile_vanleader ===> {muqavile_vanleader}")

        musteri_id = request.data.get("musteri_id")
        if (musteri_id is not None):
            musteri = get_object_or_404(Musteri, pk=musteri_id)
            print(f"musteri ==> {musteri}")
        

        muqavile_dealer = muqavile.dealer
        print(f"muqavile_dealer ===> {muqavile_dealer}")

        yeni_qrafik = request.data.get("yeni_qrafik_status")
        print(f"yeni_qrafik ===> {yeni_qrafik}")

        # YENI QRAFIK ile bagli emeliyyatlar
        if(yeni_qrafik == "YENİ QRAFİK"):
            print(f"muqavile ===> {muqavile}")
            ilkin_odenis = muqavile.ilkin_odenis
            ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
            ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
            print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
            mehsulun_qiymeti = muqavile.muqavile_umumi_mebleg
            print(f"mehsulun ==> {mehsulun_qiymeti}")

            odenen_odemetarixler = OdemeTarix.objects.filter(
                muqavile=muqavile, odenme_status="ÖDƏNƏN")
            print(
                f"odenen_odemetarixler ==> {odenen_odemetarixler} ==> {len(odenen_odemetarixler)}")

            odenmeyen_odemetarixler = OdemeTarix.objects.filter(
                muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
            print(f"odenmeyen_odemetarixler ==> {odenmeyen_odemetarixler}")

            odemek_istediyi_mebleg = float(request.data.get("yeni_qrafik_mebleg"))
            print(f"odemek_istediyi_mebleg ==> {odemek_istediyi_mebleg}")

            odenen_mebleg = 0
            for i in odenen_odemetarixler:
                odenen_mebleg += float(i.qiymet)
            print(f"odenen_mebleg ==> {odenen_mebleg}")

            odediyi = float(odenen_mebleg) + ilkin_odenis_tam
            print(f"odediyi ==> {odediyi}")

            qaliq_borc = mehsulun_qiymeti - odediyi
            print(f"qaliq_borc ==> {qaliq_borc}")

            odenmeyen_aylar = len(odenmeyen_odemetarixler)
            print(f"odenmeyen_aylar ==> {odenmeyen_aylar}")

            try:
                elave_olunacaq_ay_qaliqli = qaliq_borc / odemek_istediyi_mebleg
                # muqavile.yeni_qrafik_status = "YENİ QRAFİK"
                muqavile.save()
            except:
                return Response({"detail": "Ödəmək istədiyiniz məbləği doğru daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

            elave_olunacaq_ay = math.ceil(elave_olunacaq_ay_qaliqli)
            print(f"elave_olunacaq_ay == > {elave_olunacaq_ay}")
            create_olunacaq_ay = elave_olunacaq_ay - len(odenmeyen_odemetarixler)
            print(f"create_olunacaq_ay == > {create_olunacaq_ay}")
            a = odemek_istediyi_mebleg * (elave_olunacaq_ay-1)
            son_aya_elave_edilecek_mebleg = qaliq_borc - a
            print(
                f"son_aya_elave_edilecek_mebleg == > {son_aya_elave_edilecek_mebleg}")
            inc_month = pd.date_range(odenmeyen_odemetarixler[len(
                odenmeyen_odemetarixler)-1].tarix, periods=create_olunacaq_ay+1, freq='M')
            print(f"inc_month == > {inc_month}")
            muqavile.kredit_muddeti = muqavile.kredit_muddeti + create_olunacaq_ay
            muqavile.save()
            print(f"muqavile.kredit_muddeti ===> {muqavile.kredit_muddeti}")
            # Var olan aylarin qiymetini musterinin istediyi qiymet edir
            i = 0
            while(i < len(odenmeyen_odemetarixler)):
                odenmeyen_odemetarixler[i].qiymet = odemek_istediyi_mebleg
                odenmeyen_odemetarixler[i].save()
                i += 1

            # Elave olunacaq aylari create edir
            j = 1
            while(j <= create_olunacaq_ay):
                if(j == create_olunacaq_ay):
                    if(datetime.date.today().day < 29):
                        OdemeTarix.objects.create(
                            muqavile=muqavile,
                            tarix=f"{inc_month[j].year}-{inc_month[j].month}-{datetime.date.today().day}",
                            qiymet=son_aya_elave_edilecek_mebleg
                        )
                    elif(datetime.date.today().day == 31 or datetime.date.today().day == 30 or datetime.date.today().day == 29):
                        if(inc_month[j].day <= datetime.date.today().day):
                            OdemeTarix.objects.create(
                                muqavile=muqavile,
                                tarix=f"{inc_month[j].year}-{inc_month[j].month}-{inc_month[j].day}",
                                qiymet=son_aya_elave_edilecek_mebleg
                            )
                else:
                    if(datetime.date.today().day < 29):
                        OdemeTarix.objects.create(
                            muqavile=muqavile,
                            tarix=f"{inc_month[j].year}-{inc_month[j].month}-{datetime.date.today().day}",
                            qiymet=odemek_istediyi_mebleg
                        )
                    elif(datetime.date.today().day == 31 or datetime.date.today().day == 30 or datetime.date.today().day == 29):
                        if(inc_month[j].day <= datetime.date.today().day):
                            OdemeTarix.objects.create(
                                muqavile=muqavile,
                                tarix=f"{inc_month[j].year}-{inc_month[j].month}-{inc_month[j].day}",
                                qiymet=odemek_istediyi_mebleg
                            )
                j += 1
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)

        if (muqavile.muqavile_status == "DÜŞƏN" and request.data.get("muqavile_status") == "DAVAM EDƏN"):
            """
            Müqavilə düşən statusundan davam edən statusuna qaytarılarkən bu hissə işə düşür
            """
            muqavile.muqavile_status = "DAVAM EDƏN"
            muqavile.save()

            try:
                anbar = get_object_or_404(Anbar, ofis=muqavile_vanleader.ofis)
            except:
                return Response({"detail": "Anbar tapılmadı"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                stok = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul)
                print(f"{stok.say} {type(stok.say)}")
            except:
                return Response({"detail": "Anbarın stokunda məhsul yoxdur"}, status=status.HTTP_400_BAD_REQUEST)

            if (stok.say < int(mehsul_sayi)):
                return Response({"detail": "Stokda yetəri qədər məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)

            stok_mehsul_ciximi(stok, mehsul_sayi)

            muqavile_tarixi = muqavile.muqavile_tarixi
            print(
                f"muqavile_tarixi ==> {muqavile_tarixi} -- {type(muqavile_tarixi)}")

            year = muqavile_tarixi.year
            month = muqavile_tarixi.month
            print(f"year ==> {year} -- {type(year)}")
            print(f"month ==> {month} -- {type(month)}")

            tarix = datetime.date(year=year, month=month, day=1)
            print(f"tarix ==> {tarix} -- {type(tarix)}")

            odenmeyen_odemetarixler_qs = OdemeTarix.objects.filter(
                muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
            odenmeyen_odemetarixler = list(odenmeyen_odemetarixler_qs)
            print(
                f"odenmeyen_odemetarixler ==> {odenmeyen_odemetarixler} -- {len(odenmeyen_odemetarixler)}")

            indi = datetime.datetime.today().strftime('%Y-%m-%d')
            print(f"INDI ====> {indi} --- {type(indi)}")
            inc_month = pd.date_range(indi, periods=len(
                odenmeyen_odemetarixler), freq='M')
            print(f"inc_month ==> {inc_month} --- {type(inc_month)}")

            i = 0
            while (i < len(odenmeyen_odemetarixler)):
                if (datetime.date.today().day < 29):
                    odenmeyen_odemetarixler[
                        i].tarix = f"{inc_month[i].year}-{inc_month[i].month}-{datetime.date.today().day}"
                    odenmeyen_odemetarixler[i].save()
                elif (
                        datetime.date.today().day == 31 or datetime.date.today().day == 30 or datetime.date.today().day == 29):
                    odenmeyen_odemetarixler[i].tarix = f"{inc_month[i].year}-{inc_month[i].month}-{inc_month[i].day}",
                    odenmeyen_odemetarixler[i].save()
                i += 1

            create_services(muqavile, muqavile, True)

            return Response({"detail": "Müqavilə düşən statusundan davam edən statusuna keçirildi"},
                            status=status.HTTP_200_OK)

        if (muqavile.muqavile_status == "DAVAM EDƏN" and request.data.get("muqavile_status") == "DÜŞƏN"):
            """
            Müqavilə düşən statusuna keçərkən bu hissə işə düşür
            """
            muqavile_tarixi = muqavile.muqavile_tarixi
            print(
                f"muqavile_tarixi ==> {muqavile_tarixi} -- {type(muqavile_tarixi)}")

            year = muqavile_tarixi.year
            month = muqavile_tarixi.month
            print(f"year ==> {year} -- {type(year)}")
            print(f"month ==> {month} -- {type(month)}")

            tarix = datetime.date(year=year, month=month, day=1)
            print(f"tarix ==> {tarix} -- {type(tarix)}")

            kompensasiya_medaxil = request.data.get("kompensasiya_medaxil")
            kompensasiya_mexaric = request.data.get("kompensasiya_mexaric")

            muqavile_vanleader = muqavile.vanleader
            muqavile_dealer = muqavile.dealer

            ofis_kassa = get_object_or_404(OfisKassa, ofis=muqavile.ofis)
            print(f"ofis_kassa ==> {ofis_kassa}")

            ofis_kassa_balans = ofis_kassa.balans
            print(f"ofis_kassa_balans ==> {ofis_kassa_balans}")

            if (kompensasiya_medaxil is not None and kompensasiya_mexaric is not None):
                return Response({"detail": "Kompensasiya məxaric və mədaxil eyni anda edilə bilməz"},
                                status=status.HTTP_400_BAD_REQUEST)

            if (kompensasiya_medaxil is not None):
                qeyd = f"Vanleader - {muqavile_vanleader.asa}, müştəri - {musteri.asa}, tarix - {indiki_tarix_date}, müqavilə düşən statusuna keçirildiyi üçün."
                k_medaxil(ofis_kassa, float(kompensasiya_medaxil),
                        muqavile_vanleader, qeyd)

                muqavile.muqavile_status = "DÜŞƏN"
                muqavile.save()

            elif (kompensasiya_mexaric is not None):
                if (ofis_kassa_balans < float(kompensasiya_mexaric)):
                    return Response({"detail": "Kompensasiya məxaric məbləği Ofisin balansından çox ola bilməz"},
                                    status=status.HTTP_400_BAD_REQUEST)
                qeyd = f"Vanleader - {muqavile_vanleader.asa}, müştəri - {musteri.asa}, tarix - {indiki_tarix_date}, müqavilə düşən statusuna keçirildiyi üçün."
                k_mexaric(ofis_kassa, float(kompensasiya_mexaric),
                        muqavile_vanleader, qeyd)

                muqavile.muqavile_status = "DÜŞƏN"
                muqavile.save()

            if (kompensasiya_medaxil == "" and kompensasiya_mexaric == ""):
                muqavile.muqavile_status = "DÜŞƏN"
                muqavile.save()

            muqavile_vanleader = muqavile.vanleader
            muqavile_dealer = muqavile.dealer

            try:
                anbar = get_object_or_404(Anbar, ofis=muqavile.ofis)
            except:
                return Response({"detail": "Anbar tapılmadı"}, status=status.HTTP_400_BAD_REQUEST)

            stok = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul)
            print(f"{stok.say} {type(stok.say)}")

            stok_mehsul_elave(stok, mehsul_sayi)

            print(f"muqavile_vanleader ==> {muqavile_vanleader.id}")

            indi = datetime.date.today()
            print(f"Celery indi ==> {indi}")
            d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
            print(f"d ==> {d}")
            next_m = d + pd.offsets.MonthBegin(1)
            print(f"next_m ==> {next_m}")

            all_servis = Servis.objects.filter(muqavile=self.get_object())
            print(f"{all_servis=}")

            for servis in all_servis:
                all_servis_odeme = ServisOdeme.objects.filter(servis=servis, odendi=False)
                if len(all_servis_odeme) == 1:
                    servis_odeme = all_servis_odeme[0]
                    servis_odeme.delete()
                    servis.delete()
                for servis_odeme in all_servis_odeme:
                    print(f"{servis_odeme=}")
                    servis_odeme.delete()

            # -------------------- Maaslarin geri qaytarilmasi --------------------
            muqavile_odenis_uslubu = muqavile.odenis_uslubu
            print(f"{muqavile_odenis_uslubu=}") 

            vanleader = muqavile.vanleader
            print(f"{vanleader=}")
            if vanleader is not None:
                vanleader_status = vanleader.isci_status
                print(f"{vanleader_status=}")
                try:
                    vanleader_vezife_all = vanleader.vezife.all()
                    vanleader_vezife = vanleader_vezife_all[0].vezife_adi
                except:
                    vanleader_vezife = None
                print(f"{vanleader_vezife=} -- {type(vanleader_vezife)}")
                if (vanleader_status is not None):
                    vanleader_prim = VanLeaderPrim.objects.get(prim_status=vanleader_status, odenis_uslubu=muqavile_odenis_uslubu)
                    print(f"{vanleader_prim=}")

                    vanleader_mg_indiki_ay = MaasGoruntuleme.objects.get(isci=muqavile_vanleader, tarix=f"{indi.year}-{indi.month}-{1}")
                    vanleader_mg_novbeti_ay = MaasGoruntuleme.objects.get(isci=muqavile_vanleader, tarix=next_m)

                    vanleader_mg_indiki_ay.satis_sayi = float(vanleader_mg_indiki_ay.satis_sayi) - float(mehsul_sayi)
                    vanleader_mg_indiki_ay.satis_meblegi = float(vanleader_mg_indiki_ay.satis_meblegi) - float(muqavile.mehsul.qiymet)

                    vanleader_mg_novbeti_ay.yekun_maas = float(vanleader_mg_novbeti_ay.yekun_maas) - float(vanleader_prim.komandaya_gore_prim)

                    vanleader_mg_indiki_ay.save()
                    vanleader_mg_novbeti_ay.save()
            
            dealer = muqavile.dealer
            print(f"{dealer=}")
            if dealer is not None:
                dealer_status = dealer.isci_status
                print(f"{dealer_status=}")
                try:
                    dealer_vezife_all = dealer.vezife.all()
                    dealer_vezife = dealer_vezife_all[0].vezife_adi
                    print(f"{dealer_vezife=} -- {type(dealer_vezife)}")
                except:
                    dealer_vezife = None
                if (dealer_vezife == "DEALER"):
                    dealer_prim = DealerPrim.objects.get(prim_status=dealer_status, odenis_uslubu=muqavile_odenis_uslubu)
                    print(f"{dealer_prim=}")

                    dealer_mg_indiki_ay = MaasGoruntuleme.objects.get(isci=muqavile_dealer, tarix=f"{indi.year}-{indi.month}-{1}")
                    dealer_mg_novbeti_ay = MaasGoruntuleme.objects.get(isci=muqavile_dealer, tarix=next_m)

                    dealer_mg_indiki_ay.satis_sayi = float(dealer_mg_indiki_ay.satis_sayi) - float(mehsul_sayi)
                    dealer_mg_indiki_ay.satis_meblegi = float(dealer_mg_indiki_ay.satis_meblegi) - float(muqavile.mehsul.qiymet)
                    dealer_mg_novbeti_ay.yekun_maas = float(dealer_mg_novbeti_ay.yekun_maas) - float(dealer_prim.komandaya_gore_prim)

                    dealer_mg_indiki_ay.save()
                    dealer_mg_novbeti_ay.save()

            ofis = muqavile.ofis
            print(f"{ofis=}")
            if ofis is not None:
                officeLeaderVezife = Vezifeler.objects.get(vezife_adi="OFFICE LEADER")
                print(f"{officeLeaderVezife=}")
                officeLeaders = User.objects.filter(ofis=ofis, vezife=officeLeaderVezife)
                print(f"{officeLeaders=}")
                for officeLeader in officeLeaders:
                    officeLeader_status = officeLeader.isci_status
                    print(f"{officeLeader_status=}")
                    ofisleader_prim = OfficeLeaderPrim.objects.get(prim_status=officeLeader_status)
                    print(f"{ofisleader_prim=}")

                    officeLeader_maas_goruntulenme_bu_ay = MaasGoruntuleme.objects.get(isci=officeLeader, tarix=f"{indi.year}-{indi.month}-{1}")
                    officeLeader_maas_goruntulenme_novbeti_ay = MaasGoruntuleme.objects.get(isci=officeLeader, tarix=next_m)
                    print(f"{officeLeader_maas_goruntulenme_bu_ay=}")
                    print(f"{officeLeader_maas_goruntulenme_novbeti_ay=}")

                    officeLeader_maas_goruntulenme_bu_ay.satis_sayi = float(officeLeader_maas_goruntulenme_bu_ay.satis_sayi) - float(mehsul_sayi)
                    officeLeader_maas_goruntulenme_bu_ay.satis_meblegi = float(officeLeader_maas_goruntulenme_bu_ay.satis_meblegi) - float(muqavile.mehsul.qiymet)
                    print(f"{officeLeader_maas_goruntulenme_bu_ay.satis_sayi=}")
                    print(f"{officeLeader_maas_goruntulenme_bu_ay.satis_meblegi=}")
                    officeLeader_maas_goruntulenme_bu_ay.save()

                    officeLeader_maas_goruntulenme_novbeti_ay.yekun_maas = float(officeLeader_maas_goruntulenme_novbeti_ay.yekun_maas) - float(ofisleader_prim.komandaya_gore_prim)
                    print(f"{officeLeader_maas_goruntulenme_novbeti_ay.yekun_maas=}")
                    officeLeader_maas_goruntulenme_novbeti_ay.save()
            # -------------------- -------------------- --------------------
            muqavile.muqavile_status = "DÜŞƏN"
            muqavile.save()
            return Response({"detail": "Müqavilə düşən statusuna keçirildi"}, status=status.HTTP_200_OK)

        if (muqavile.odenis_uslubu == "KREDİT"):
            if (odemek_istediyi_ilkin_odenis != None and ilkin_odenis_status == "DAVAM EDƏN"):
                if (float(odemek_istediyi_ilkin_odenis) != ilkin_odenis):
                    return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
                elif (float(odemek_istediyi_ilkin_odenis) == ilkin_odenis):
                    print("Burda1")
                    muqavile.ilkin_odenis_status = "BİTMİŞ"
                    muqavile.ilkin_odenis_tarixi = indiki_tarix_date
                    muqavile.save()
                    return Response({"detail": "İlkin ödəniş ödənildi"}, status=status.HTTP_200_OK)

            if (
                    odemek_istediyi_qaliq_ilkin_odenis != None and ilkin_odenis_status == "BİTMİŞ" and qaliq_ilkin_odenis_status == "DAVAM EDƏN"):
                if (float(odemek_istediyi_qaliq_ilkin_odenis) == ilkin_odenis_qaliq):
                    print("Burda2")
                    muqavile.qaliq_ilkin_odenis_status = "BİTMİŞ"
                    muqavile.ilkin_odenis_qaliq_tarixi = indiki_tarix_date
                    muqavile.save()
                    return Response({"detail": "Qalıq ilkin ödəniş ödənildi"}, status=status.HTTP_200_OK)
                elif (float(odemek_istediyi_qaliq_ilkin_odenis) != ilkin_odenis_qaliq):
                    return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

        if (muqavile.odenis_uslubu == "İKİ DƏFƏYƏ NƏĞD"):
            if (odemek_istediyi_negd_odenis_1 != None and negd_odenis_1_status == "DAVAM EDƏN"):
                if (float(odemek_istediyi_negd_odenis_1) != negd_odenis_1):
                    return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
                elif (float(odemek_istediyi_negd_odenis_1) == negd_odenis_1):
                    print("Burda1")
                    muqavile.negd_odenis_1_status = "BİTMİŞ"
                    muqavile.negd_odenis_1_tarix = indiki_tarix_date
                    muqavile.save()
                    return Response({"detail": "1-ci ödəniş ödənildi"}, status=status.HTTP_200_OK)

            if (
                    odemek_istediyi_negd_odenis_2 != None and negd_odenis_1_status == "BİTMİŞ" and negd_odenis_2_status == "DAVAM EDƏN"):
                if (float(odemek_istediyi_negd_odenis_2) == negd_odenis_2):
                    print("Burda2")
                    muqavile.negd_odenis_2_status = "BİTMİŞ"
                    muqavile.negd_odenis_2_tarix = indiki_tarix_date
                    muqavile.muqavile_status = "BİTMİŞ"
                    muqavile.save()
                    return Response({"detail": "Qalıq nəğd ödəniş ödənildi"}, status=status.HTTP_200_OK)
                elif (float(odemek_istediyi_negd_odenis_2) != negd_odenis_2):
                    return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        traceback.print_exc()

def muqavile_update(self, request, *args, **kwargs):
    try:
        muqavile = self.get_object()
        serializer = MuqavileSerializer(muqavile, data=request.data, partial=True)
        print(f"muqavile ===> {muqavile}")

        ilkin_odenis = muqavile.ilkin_odenis
        print(f"ilkin_odenis ===> {ilkin_odenis}")
        ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
        print(f"ilkin_odenis_qaliq ===> {ilkin_odenis_qaliq}")

        ilkin_odenis_status = muqavile.ilkin_odenis_status
        print(f"ilkin_odenis_status ===> {ilkin_odenis_status}")

        qaliq_ilkin_odenis_status = muqavile.qaliq_ilkin_odenis_status
        print(f"qaliq_ilkin_odenis_status ===> {qaliq_ilkin_odenis_status}")

        odemek_istediyi_ilkin_odenis = request.data.get("ilkin_odenis")
        print(f"odemek_istediyi_ilkin_odenis ===> {odemek_istediyi_ilkin_odenis}")

        odemek_istediyi_qaliq_ilkin_odenis = request.data.get("ilkin_odenis_qaliq")
        print(
            f"odemek_istediyi_qaliq_ilkin_odenis ===> {odemek_istediyi_qaliq_ilkin_odenis}")

        negd_odenis_1 = muqavile.negd_odenis_1
        print(f"negd_odenis_1 ===> {negd_odenis_1}")
        negd_odenis_2 = muqavile.negd_odenis_2
        print(f"negd_odenis_2 ===> {negd_odenis_2}")

        negd_odenis_1_status = muqavile.negd_odenis_1_status
        print(f"negd_odenis_1_status ===> {negd_odenis_1_status}")

        negd_odenis_2_status = muqavile.negd_odenis_2_status
        print(f"negd_odenis_2_status ===> {negd_odenis_2_status}")

        muqavile_status = muqavile.muqavile_status
        print(f"muqavile_status ===> {muqavile_status}")

        odemek_istediyi_negd_odenis_1 = request.data.get("negd_odenis_1")
        print(
            f"odemek_istediyi_negd_odenis_1 ===> {odemek_istediyi_negd_odenis_1}")

        odemek_istediyi_negd_odenis_2 = request.data.get("negd_odenis_2")
        print(
            f"odemek_istediyi_negd_odenis_2 ===> {odemek_istediyi_negd_odenis_2}")

        my_time = datetime.datetime.min.time()

        indiki_tarix_date = datetime.date.today()
        indiki_tarix = datetime.datetime.combine(indiki_tarix_date, my_time)
        indiki_tarix_san = datetime.datetime.timestamp(indiki_tarix)
        print(f"indiki_tarix_san ===> {indiki_tarix_san}")

        dusen_muqavile_status = request.data.get("muqavile_status")
        print(f"dusen_muqavile_status ===> {dusen_muqavile_status}")

        mehsul = muqavile.mehsul
        print(f"mehsul ==> {mehsul}")

        mehsul_sayi = muqavile.mehsul_sayi
        print(f"mehsul_sayi ==> {mehsul_sayi}")

        muqavile_vanleader = muqavile.vanleader
        print(f"muqavile_vanleader ===> {muqavile_vanleader}")

        musteri_id = request.data.get("musteri_id")
        if (musteri_id is not None):
            musteri = get_object_or_404(Musteri, pk=musteri_id)
            print(f"musteri ==> {musteri}")
        

        muqavile_dealer = muqavile.dealer
        print(f"muqavile_dealer ===> {muqavile_dealer}")

        yeni_qrafik = request.data.get("yeni_qrafik_status")
        print(f"yeni_qrafik ===> {yeni_qrafik}")

        # YENI QRAFIK ile bagli emeliyyatlar
        if(yeni_qrafik == "YENİ QRAFİK"):
            print(f"muqavile ===> {muqavile}")
            ilkin_odenis = muqavile.ilkin_odenis
            ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
            ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
            print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
            mehsulun_qiymeti = muqavile.muqavile_umumi_mebleg
            print(f"mehsulun ==> {mehsulun_qiymeti}")

            odenen_odemetarixler = OdemeTarix.objects.filter(
                muqavile=muqavile, odenme_status="ÖDƏNƏN")
            print(
                f"odenen_odemetarixler ==> {odenen_odemetarixler} ==> {len(odenen_odemetarixler)}")

            odenmeyen_odemetarixler = OdemeTarix.objects.filter(
                muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
            print(f"odenmeyen_odemetarixler ==> {odenmeyen_odemetarixler}")

            odemek_istediyi_mebleg = float(request.data.get("yeni_qrafik_mebleg"))
            print(f"odemek_istediyi_mebleg ==> {odemek_istediyi_mebleg}")

            odenen_mebleg = 0
            for i in odenen_odemetarixler:
                odenen_mebleg += float(i.qiymet)
            print(f"odenen_mebleg ==> {odenen_mebleg}")

            odediyi = float(odenen_mebleg) + ilkin_odenis_tam
            print(f"odediyi ==> {odediyi}")

            qaliq_borc = mehsulun_qiymeti - odediyi
            print(f"qaliq_borc ==> {qaliq_borc}")

            odenmeyen_aylar = len(odenmeyen_odemetarixler)
            print(f"odenmeyen_aylar ==> {odenmeyen_aylar}")

            try:
                elave_olunacaq_ay_qaliqli = qaliq_borc / odemek_istediyi_mebleg
                # muqavile.yeni_qrafik_status = "YENİ QRAFİK"
                muqavile.save()
            except:
                return Response({"detail": "Ödəmək istədiyiniz məbləği doğru daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

            elave_olunacaq_ay = math.ceil(elave_olunacaq_ay_qaliqli)
            print(f"elave_olunacaq_ay == > {elave_olunacaq_ay}")
            create_olunacaq_ay = elave_olunacaq_ay - len(odenmeyen_odemetarixler)
            print(f"create_olunacaq_ay == > {create_olunacaq_ay}")
            a = odemek_istediyi_mebleg * (elave_olunacaq_ay-1)
            son_aya_elave_edilecek_mebleg = qaliq_borc - a
            print(
                f"son_aya_elave_edilecek_mebleg == > {son_aya_elave_edilecek_mebleg}")
            inc_month = pd.date_range(odenmeyen_odemetarixler[len(
                odenmeyen_odemetarixler)-1].tarix, periods=create_olunacaq_ay+1, freq='M')
            print(f"inc_month == > {inc_month}")
            muqavile.kredit_muddeti = muqavile.kredit_muddeti + create_olunacaq_ay
            muqavile.save()
            print(f"muqavile.kredit_muddeti ===> {muqavile.kredit_muddeti}")
            # Var olan aylarin qiymetini musterinin istediyi qiymet edir
            i = 0
            while(i < len(odenmeyen_odemetarixler)):
                odenmeyen_odemetarixler[i].qiymet = odemek_istediyi_mebleg
                odenmeyen_odemetarixler[i].save()
                i += 1

            # Elave olunacaq aylari create edir
            j = 1
            while(j <= create_olunacaq_ay):
                if(j == create_olunacaq_ay):
                    if(datetime.date.today().day < 29):
                        OdemeTarix.objects.create(
                            muqavile=muqavile,
                            tarix=f"{inc_month[j].year}-{inc_month[j].month}-{datetime.date.today().day}",
                            qiymet=son_aya_elave_edilecek_mebleg
                        )
                    elif(datetime.date.today().day == 31 or datetime.date.today().day == 30 or datetime.date.today().day == 29):
                        if(inc_month[j].day <= datetime.date.today().day):
                            OdemeTarix.objects.create(
                                muqavile=muqavile,
                                tarix=f"{inc_month[j].year}-{inc_month[j].month}-{inc_month[j].day}",
                                qiymet=son_aya_elave_edilecek_mebleg
                            )
                else:
                    if(datetime.date.today().day < 29):
                        OdemeTarix.objects.create(
                            muqavile=muqavile,
                            tarix=f"{inc_month[j].year}-{inc_month[j].month}-{datetime.date.today().day}",
                            qiymet=odemek_istediyi_mebleg
                        )
                    elif(datetime.date.today().day == 31 or datetime.date.today().day == 30 or datetime.date.today().day == 29):
                        if(inc_month[j].day <= datetime.date.today().day):
                            OdemeTarix.objects.create(
                                muqavile=muqavile,
                                tarix=f"{inc_month[j].year}-{inc_month[j].month}-{inc_month[j].day}",
                                qiymet=odemek_istediyi_mebleg
                            )
                j += 1
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)

        if (muqavile.muqavile_status == "DÜŞƏN" and request.data.get("muqavile_status") == "DAVAM EDƏN"):
            """
            Müqavilə düşən statusundan davam edən statusuna qaytarılarkən bu hissə işə düşür
            """
            muqavile.muqavile_status = "DAVAM EDƏN"
            muqavile.save()

            try:
                anbar = get_object_or_404(Anbar, ofis=muqavile_vanleader.ofis)
            except:
                return Response({"detail": "Anbar tapılmadı"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                stok = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul)
                print(f"{stok.say} {type(stok.say)}")
            except:
                return Response({"detail": "Anbarın stokunda məhsul yoxdur"}, status=status.HTTP_400_BAD_REQUEST)

            if (stok.say < int(mehsul_sayi)):
                return Response({"detail": "Stokda yetəri qədər məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)

            stok_mehsul_ciximi(stok, mehsul_sayi)

            muqavile_tarixi = muqavile.muqavile_tarixi
            print(
                f"muqavile_tarixi ==> {muqavile_tarixi} -- {type(muqavile_tarixi)}")

            year = muqavile_tarixi.year
            month = muqavile_tarixi.month
            print(f"year ==> {year} -- {type(year)}")
            print(f"month ==> {month} -- {type(month)}")

            tarix = datetime.date(year=year, month=month, day=1)
            print(f"tarix ==> {tarix} -- {type(tarix)}")

            odenmeyen_odemetarixler_qs = OdemeTarix.objects.filter(
                muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
            odenmeyen_odemetarixler = list(odenmeyen_odemetarixler_qs)
            print(
                f"odenmeyen_odemetarixler ==> {odenmeyen_odemetarixler} -- {len(odenmeyen_odemetarixler)}")

            indi = datetime.datetime.today().strftime('%Y-%m-%d')
            print(f"INDI ====> {indi} --- {type(indi)}")
            inc_month = pd.date_range(indi, periods=len(
                odenmeyen_odemetarixler), freq='M')
            print(f"inc_month ==> {inc_month} --- {type(inc_month)}")

            i = 0
            while (i < len(odenmeyen_odemetarixler)):
                if (datetime.date.today().day < 29):
                    odenmeyen_odemetarixler[
                        i].tarix = f"{inc_month[i].year}-{inc_month[i].month}-{datetime.date.today().day}"
                    odenmeyen_odemetarixler[i].save()
                elif (
                        datetime.date.today().day == 31 or datetime.date.today().day == 30 or datetime.date.today().day == 29):
                    odenmeyen_odemetarixler[i].tarix = f"{inc_month[i].year}-{inc_month[i].month}-{inc_month[i].day}",
                    odenmeyen_odemetarixler[i].save()
                i += 1

            create_services(muqavile, muqavile, True)

            return Response({"detail": "Müqavilə düşən statusundan davam edən statusuna keçirildi"},
                            status=status.HTTP_200_OK)

        if (muqavile.muqavile_status == "DAVAM EDƏN" and request.data.get("muqavile_status") == "DÜŞƏN"):
            """
            Müqavilə düşən statusuna keçərkən bu hissə işə düşür
            """
            muqavile_tarixi = muqavile.muqavile_tarixi
            print(
                f"muqavile_tarixi ==> {muqavile_tarixi} -- {type(muqavile_tarixi)}")

            year = muqavile_tarixi.year
            month = muqavile_tarixi.month
            print(f"year ==> {year} -- {type(year)}")
            print(f"month ==> {month} -- {type(month)}")

            tarix = datetime.date(year=year, month=month, day=1)
            print(f"tarix ==> {tarix} -- {type(tarix)}")

            kompensasiya_medaxil = request.data.get("kompensasiya_medaxil")
            kompensasiya_mexaric = request.data.get("kompensasiya_mexaric")

            muqavile_vanleader = muqavile.vanleader
            muqavile_dealer = muqavile.dealer

            ofis_kassa = get_object_or_404(OfisKassa, ofis=muqavile.ofis)
            print(f"ofis_kassa ==> {ofis_kassa}")

            ofis_kassa_balans = ofis_kassa.balans
            print(f"ofis_kassa_balans ==> {ofis_kassa_balans}")

            if (kompensasiya_medaxil is not None and kompensasiya_mexaric is not None):
                return Response({"detail": "Kompensasiya məxaric və mədaxil eyni anda edilə bilməz"},
                                status=status.HTTP_400_BAD_REQUEST)

            if (kompensasiya_medaxil is not None):
                qeyd = f"Vanleader - {muqavile_vanleader.asa}, müştəri - {musteri.asa}, tarix - {indiki_tarix_date}, müqavilə düşən statusuna keçirildiyi üçün."
                k_medaxil(ofis_kassa, float(kompensasiya_medaxil),
                        muqavile_vanleader, qeyd)

                muqavile.muqavile_status = "DÜŞƏN"
                muqavile.save()

            elif (kompensasiya_mexaric is not None):
                if (ofis_kassa_balans < float(kompensasiya_mexaric)):
                    return Response({"detail": "Kompensasiya məxaric məbləği Ofisin balansından çox ola bilməz"},
                                    status=status.HTTP_400_BAD_REQUEST)
                qeyd = f"Vanleader - {muqavile_vanleader.asa}, müştəri - {musteri.asa}, tarix - {indiki_tarix_date}, müqavilə düşən statusuna keçirildiyi üçün."
                k_mexaric(ofis_kassa, float(kompensasiya_mexaric),
                        muqavile_vanleader, qeyd)

                muqavile.muqavile_status = "DÜŞƏN"
                muqavile.save()

            if (kompensasiya_medaxil == "" and kompensasiya_mexaric == ""):
                muqavile.muqavile_status = "DÜŞƏN"
                muqavile.save()

            muqavile_vanleader = muqavile.vanleader
            muqavile_dealer = muqavile.dealer

            try:
                anbar = get_object_or_404(Anbar, ofis=muqavile.ofis)
            except:
                return Response({"detail": "Anbar tapılmadı"}, status=status.HTTP_400_BAD_REQUEST)

            stok = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul)
            print(f"{stok.say} {type(stok.say)}")

            stok_mehsul_elave(stok, mehsul_sayi)

            print(f"muqavile_vanleader ==> {muqavile_vanleader.id}")

            indi = datetime.date.today()
            print(f"Celery indi ==> {indi}")
            d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
            print(f"d ==> {d}")
            next_m = d + pd.offsets.MonthBegin(1)
            print(f"next_m ==> {next_m}")

            all_servis = Servis.objects.filter(muqavile=muqavile)
            for servis in all_servis:
                all_servis_odeme = ServisOdeme.objects.filter(servis=servis, odendi=False)
                if len(all_servis_odeme) == 1:
                    all_servis_odeme[0].delete()
                    servis.delete()
                for servis_odeme in all_servis_odeme:
                    servis_odeme.delete()

            # -------------------- Maaslarin geri qaytarilmasi --------------------
            muqavile_odenis_uslubu = muqavile.odenis_uslubu
            print(f"{muqavile_odenis_uslubu=}") 

            vanleader = muqavile.vanleader
            print(f"{vanleader=}")
            if vanleader is not None:
                vanleader_status = vanleader.isci_status
                print(f"{vanleader_status=}")
                try:
                    vanleader_vezife_all = vanleader.vezife.all()
                    vanleader_vezife = vanleader_vezife_all[0].vezife_adi
                except:
                    vanleader_vezife = None
                print(f"{vanleader_vezife=} -- {type(vanleader_vezife)}")
                if (vanleader_status is not None):
                    vanleader_prim = VanLeaderPrim.objects.get(prim_status=vanleader_status, odenis_uslubu=muqavile_odenis_uslubu)
                    print(f"{vanleader_prim=}")

                    vanleader_mg_indiki_ay = MaasGoruntuleme.objects.get(isci=muqavile_vanleader, tarix=f"{indi.year}-{indi.month}-{1}")
                    vanleader_mg_novbeti_ay = MaasGoruntuleme.objects.get(isci=muqavile_vanleader, tarix=next_m)

                    vanleader_mg_indiki_ay.satis_sayi = float(vanleader_mg_indiki_ay.satis_sayi) - float(mehsul_sayi)
                    vanleader_mg_indiki_ay.satis_meblegi = float(vanleader_mg_indiki_ay.satis_meblegi) - float(muqavile.mehsul.qiymet)

                    vanleader_mg_novbeti_ay.yekun_maas = float(vanleader_mg_novbeti_ay.yekun_maas) - float(vanleader_prim.komandaya_gore_prim)

                    vanleader_mg_indiki_ay.save()
                    vanleader_mg_novbeti_ay.save()
            
            dealer = muqavile.dealer
            print(f"{dealer=}")
            if dealer is not None:
                dealer_status = dealer.isci_status
                print(f"{dealer_status=}")
                try:
                    dealer_vezife_all = dealer.vezife.all()
                    dealer_vezife = dealer_vezife_all[0].vezife_adi
                    print(f"{dealer_vezife=} -- {type(dealer_vezife)}")
                except:
                    dealer_vezife = None
                if (dealer_vezife == "DEALER"):
                    dealer_prim = DealerPrim.objects.get(prim_status=dealer_status, odenis_uslubu=muqavile_odenis_uslubu)
                    print(f"{dealer_prim=}")

                    dealer_mg_indiki_ay = MaasGoruntuleme.objects.get(isci=muqavile_dealer, tarix=f"{indi.year}-{indi.month}-{1}")
                    dealer_mg_novbeti_ay = MaasGoruntuleme.objects.get(isci=muqavile_dealer, tarix=next_m)

                    dealer_mg_indiki_ay.satis_sayi = float(dealer_mg_indiki_ay.satis_sayi) - float(mehsul_sayi)
                    dealer_mg_indiki_ay.satis_meblegi = float(dealer_mg_indiki_ay.satis_meblegi) - float(muqavile.mehsul.qiymet)
                    dealer_mg_novbeti_ay.yekun_maas = float(dealer_mg_novbeti_ay.yekun_maas) - float(dealer_prim.komandaya_gore_prim)

                    dealer_mg_indiki_ay.save()
                    dealer_mg_novbeti_ay.save()

            ofis = muqavile.ofis
            print(f"{ofis=}")
            if ofis is not None:
                officeLeaderVezife = Vezifeler.objects.get(vezife_adi="OFFICE LEADER")
                print(f"{officeLeaderVezife=}")
                officeLeaders = User.objects.filter(ofis=ofis, vezife=officeLeaderVezife)
                print(f"{officeLeaders=}")
                for officeLeader in officeLeaders:
                    officeLeader_status = officeLeader.isci_status
                    print(f"{officeLeader_status=}")
                    ofisleader_prim = OfficeLeaderPrim.objects.get(prim_status=officeLeader_status)
                    print(f"{ofisleader_prim=}")

                    officeLeader_maas_goruntulenme_bu_ay = MaasGoruntuleme.objects.get(isci=officeLeader, tarix=f"{indi.year}-{indi.month}-{1}")
                    officeLeader_maas_goruntulenme_novbeti_ay = MaasGoruntuleme.objects.get(isci=officeLeader, tarix=next_m)
                    print(f"{officeLeader_maas_goruntulenme_bu_ay=}")
                    print(f"{officeLeader_maas_goruntulenme_novbeti_ay=}")

                    officeLeader_maas_goruntulenme_bu_ay.satis_sayi = float(officeLeader_maas_goruntulenme_bu_ay.satis_sayi) - float(mehsul_sayi)
                    officeLeader_maas_goruntulenme_bu_ay.satis_meblegi = float(officeLeader_maas_goruntulenme_bu_ay.satis_meblegi) - float(muqavile.mehsul.qiymet)
                    print(f"{officeLeader_maas_goruntulenme_bu_ay.satis_sayi=}")
                    print(f"{officeLeader_maas_goruntulenme_bu_ay.satis_meblegi=}")
                    officeLeader_maas_goruntulenme_bu_ay.save()

                    officeLeader_maas_goruntulenme_novbeti_ay.yekun_maas = float(officeLeader_maas_goruntulenme_novbeti_ay.yekun_maas) - float(ofisleader_prim.komandaya_gore_prim)
                    print(f"{officeLeader_maas_goruntulenme_novbeti_ay.yekun_maas=}")
                    officeLeader_maas_goruntulenme_novbeti_ay.save()
            # -------------------- -------------------- --------------------

            return Response({"detail": "Müqavilə düşən statusuna keçirildi"}, status=status.HTTP_200_OK)

        if (muqavile.odenis_uslubu == "KREDİT"):
            if (odemek_istediyi_ilkin_odenis != None and ilkin_odenis_status == "DAVAM EDƏN"):
                if (float(odemek_istediyi_ilkin_odenis) != ilkin_odenis):
                    return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
                elif (float(odemek_istediyi_ilkin_odenis) == ilkin_odenis):
                    print("Burda1")
                    muqavile.ilkin_odenis_status = "BİTMİŞ"
                    muqavile.ilkin_odenis_tarixi = indiki_tarix_date
                    muqavile.save()
                    return Response({"detail": "İlkin ödəniş ödənildi"}, status=status.HTTP_200_OK)

            if (
                    odemek_istediyi_qaliq_ilkin_odenis != None and ilkin_odenis_status == "BİTMİŞ" and qaliq_ilkin_odenis_status == "DAVAM EDƏN"):
                if (float(odemek_istediyi_qaliq_ilkin_odenis) == ilkin_odenis_qaliq):
                    print("Burda2")
                    muqavile.qaliq_ilkin_odenis_status = "BİTMİŞ"
                    muqavile.ilkin_odenis_qaliq_tarixi = indiki_tarix_date
                    muqavile.save()
                    return Response({"detail": "Qalıq ilkin ödəniş ödənildi"}, status=status.HTTP_200_OK)
                elif (float(odemek_istediyi_qaliq_ilkin_odenis) != ilkin_odenis_qaliq):
                    return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

        if (muqavile.odenis_uslubu == "İKİ DƏFƏYƏ NƏĞD"):
            if (odemek_istediyi_negd_odenis_1 != None and negd_odenis_1_status == "DAVAM EDƏN"):
                if (float(odemek_istediyi_negd_odenis_1) != negd_odenis_1):
                    return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
                elif (float(odemek_istediyi_negd_odenis_1) == negd_odenis_1):
                    print("Burda1")
                    muqavile.negd_odenis_1_status = "BİTMİŞ"
                    muqavile.negd_odenis_1_tarix = indiki_tarix_date
                    muqavile.save()
                    return Response({"detail": "1-ci ödəniş ödənildi"}, status=status.HTTP_200_OK)

            if (
                    odemek_istediyi_negd_odenis_2 != None and negd_odenis_1_status == "BİTMİŞ" and negd_odenis_2_status == "DAVAM EDƏN"):
                if (float(odemek_istediyi_negd_odenis_2) == negd_odenis_2):
                    print("Burda2")
                    muqavile.negd_odenis_2_status = "BİTMİŞ"
                    muqavile.negd_odenis_2_tarix = indiki_tarix_date
                    muqavile.muqavile_status = "BİTMİŞ"
                    muqavile.save()
                    return Response({"detail": "Qalıq nəğd ödəniş ödənildi"}, status=status.HTTP_200_OK)
                elif (float(odemek_istediyi_negd_odenis_2) != negd_odenis_2):
                    return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        traceback.print_exc()