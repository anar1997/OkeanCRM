from re import I
from rest_framework import status
from rest_framework.response import Response
from api.v1.serializers import MuqavileSerializer
from mehsullar.models import (
    Anbar, 
    Mehsullar, 
    Stok
)
from rest_framework.generics import get_object_or_404

import datetime

def muqavile_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    user = self.request.user
    print(f"login olan user ==> {user}")

    my_time = datetime.datetime.min.time()

    indiki_tarix_date = datetime.date.today()
    indiki_tarix = datetime.datetime.combine(indiki_tarix_date, my_time)
    indiki_tarix_san = datetime.datetime.timestamp(indiki_tarix)
    print(f"indiki_tarix_san ===> {indiki_tarix_san}")

    if(request.POST.get("ilkin_odenis_tarixi") != ""):
        ilkin_odenis_tarixi = request.POST.get("ilkin_odenis_tarixi")
        ilkin_odenis_tarixi_date = datetime.datetime.strptime(ilkin_odenis_tarixi, "%Y-%m-%d")
        ilkin_odenis_tarixi_san = datetime.datetime.timestamp(ilkin_odenis_tarixi_date)
        print(f"ilkin_odenis_tarixi_san ===> {ilkin_odenis_tarixi_san}")
    
    if(request.POST.get("ilkin_odenis_qaliq_tarixi") != ""):
        ilkin_odenis_qaliq_tarixi = request.POST.get("ilkin_odenis_qaliq_tarixi")
        ilkin_odenis_qaliq_tarixi_date = datetime.datetime.strptime(ilkin_odenis_qaliq_tarixi, "%Y-%m-%d")
        ilkin_odenis_qaliq_tarixi_san = datetime.datetime.timestamp(ilkin_odenis_qaliq_tarixi_date)
        print(f"ilkin_odenis_qaliq_tarixi_san ===> {ilkin_odenis_qaliq_tarixi_san}")

    if(request.POST.get("negd_odenis_1_tarix") != ""):
        negd_odenis_1_tarix = request.POST.get("negd_odenis_1_tarix")
        negd_odenis_1_tarix_date = datetime.datetime.strptime(negd_odenis_1_tarix, "%Y-%m-%d")
        negd_odenis_1_tarix_san = datetime.datetime.timestamp(negd_odenis_1_tarix_date)
        print(f"negd_odenis_1_tarix_san ===> {negd_odenis_1_tarix_san}")
    
    if(request.POST.get("negd_odenis_2_tarix") != ""):
        negd_odenis_2_tarix = request.POST.get("negd_odenis_2_tarix")
        negd_odenis_2_tarix_date = datetime.datetime.strptime(negd_odenis_2_tarix, "%Y-%m-%d")
        negd_odenis_2_tarix_san = datetime.datetime.timestamp(negd_odenis_2_tarix_date)
        print(f"negd_odenis_2_tarix_san ===> {negd_odenis_2_tarix_san}")

    mehsul_id_str = request.data.get("mehsul_id")
    if(mehsul_id_str == ""):
        print("Mehsul daxil edilmeyib")
        return Response({"detail": "Müqavilə imzalamaq üçün mütləq məhsul daxil edilməlidir."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        mehsul_id = int(mehsul_id_str)
    print(f"mehsul id ==> {mehsul_id}")
    mehsul = get_object_or_404(Mehsullar, pk=mehsul_id)
    print(f"mehsul ==> {mehsul}")

    mehsul_sayi = request.data.get("mehsul_sayi")
    print(f"mehsul_sayi ==> {mehsul_sayi}")

    odenis_uslubu = request.data.get("odenis_uslubu")
    print(f"odenis_uslubu ==> {odenis_uslubu}")

    # verilecek_ilkin_odenis = request.data.get("verilecek_ilkin_odenis")
    # print(f"verilecek_ilkin_odenis ==> {verilecek_ilkin_odenis} --- {type(verilecek_ilkin_odenis)}")

    ilkin_odenis = request.data.get("ilkin_odenis")
    print(f"ilkin_odenis ==> {ilkin_odenis} --- {type(ilkin_odenis)}")
    
    ilkin_odenis_qaliq = request.data.get("ilkin_odenis_qaliq")
    print(f"ilkin_odenis_qaliq ==> {ilkin_odenis_qaliq} --- {type(ilkin_odenis_qaliq)}")

    print(f"user.is_superuser ==> {user.is_superuser} --- {type(user.is_superuser)}")


    def stok_mehsul_ciximi(stok, mehsul_sayi):
        stok.say = stok.say - int(mehsul_sayi)
        stok.save()
        if (stok.say == 0):
            stok.delete()
        return stok.say
    
    def umumi_mebleg(mehsul_qiymeti, mehsul_sayi):
        muqavile_umumi_mebleg = mehsul_qiymeti * mehsul_sayi
        return muqavile_umumi_mebleg

    try:
        anbar = get_object_or_404(Anbar, ofis=user.ofis)
    except:
        return Response({"detail": "Anbar tapılmadı"}, status=status.HTTP_400_BAD_REQUEST)

    shirket = user.shirket
    ofis = user.ofis
    shobe = user.shobe
    kredit_muddeti = request.data.get("kredit_muddeti")
    print(f"anbar ==> {anbar}")
    print(f"ofis ==> {user.ofis}")

    try:
        stok = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul)
        print(f"stok ==> {stok}")
        if (serializer.is_valid()):
            if(mehsul_sayi == ""):
                mehsul_sayi = 1
            print("Burdayam")
            if(odenis_uslubu == "KREDİT"):
                if(kredit_muddeti == ""):
                    # Kredit muddeti daxil edilmezse
                    print("Burdayam1")
                    return Response({"detail": "Ödəmə statusu kreditdir amma kredit müddəti daxil edilməyib"}, status=status.HTTP_400_BAD_REQUEST)
                elif(int(kredit_muddeti) == 0):
                    # Kredit muddeyi 0 daxil edilerse
                    print("Burdayam2")
                    return Response({"detail": "Ödəmə statusu kreditdir amma kredit müddəti 0 daxil edilib"}, status=status.HTTP_400_BAD_REQUEST)
                elif(int(kredit_muddeti) == 31):
                    # Kredit muddeti 31 ay daxil edilerse
                    print("Burdayam3")
                    return Response({"detail": "Maksimum kredit müddəti 30 aydır"}, status=status.HTTP_400_BAD_REQUEST)
                elif(int(kredit_muddeti) > 0):
                    # Kredit muddeti 0-dan boyuk olarsa

                    if((ilkin_odenis != "") and (request.POST.get("ilkin_odenis_tarixi") == "")):
                        return Response({"detail": "İlkin ödəniş məbləği qeyd olunub amma ilkin ödəniş tarixi qeyd olunmayıb"}, status=status.HTTP_400_BAD_REQUEST)
                    
                    if((ilkin_odenis_qaliq != "") and (request.POST.get("ilkin_odenis_qaliq_tarixi") == "")):
                        return Response({"detail": "Qalıq İlkin ödəniş məbləği qeyd olunub amma qalıq ilkin ödəniş tarixi qeyd olunmayıb"}, status=status.HTTP_400_BAD_REQUEST)

                    print("Burdayam4")
                    if(ilkin_odenis == "" and ilkin_odenis_qaliq == ""):
                        # Ilkin odenis daxil edilmezse
                        print("Burdayam5")
                        stok_mehsul_ciximi(stok, int(mehsul_sayi))
                        muqavile_umumi_mebleg = umumi_mebleg(mehsul.qiymet, int(mehsul_sayi))
                        print(f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg}")
                        serializer.save(vanleader=user, shirket = shirket, ofis = ofis, shobe = shobe,  muqavile_umumi_mebleg = muqavile_umumi_mebleg)
                        return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
                    elif(ilkin_odenis != "" and ilkin_odenis_qaliq == ""):
                        # Umumi ilkin odenis meblegi daxil edilerse ve qaliq ilkin odenis meblegi daxil edilmezse
                        print("Burdayam7")
                        if(indiki_tarix_san == ilkin_odenis_tarixi_san):
                            print("Burdayam8")
                            stok_mehsul_ciximi(stok, int(mehsul_sayi))
                            muqavile_umumi_mebleg = umumi_mebleg(mehsul.qiymet, int(mehsul_sayi))
                            serializer.save(vanleader=user, shirket = shirket, ofis = ofis, shobe = shobe, ilkin_odenis = ilkin_odenis, ilkin_odenis_status = "BİTMİŞ", muqavile_umumi_mebleg = muqavile_umumi_mebleg)
                            return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
                        elif(indiki_tarix_san < ilkin_odenis_tarixi_san):
                            print("Burdayam9")
                            stok_mehsul_ciximi(stok, int(mehsul_sayi))
                            muqavile_umumi_mebleg = umumi_mebleg(mehsul.qiymet, int(mehsul_sayi))
                            serializer.save(vanleader=user, shirket = shirket, ofis = ofis, shobe = shobe, ilkin_odenis = ilkin_odenis, ilkin_odenis_status = "DAVAM EDƏN", muqavile_umumi_mebleg = muqavile_umumi_mebleg)
                            
                            return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
                        elif(indiki_tarix_san > ilkin_odenis_tarixi_san):
                            print("Burdayam10")
                            return Response({"detail": "İlkin ödəniş tarixini keçmiş tarixə təyin edə bilməzsiniz"}, status=status.HTTP_400_BAD_REQUEST)
                        print("Burdayam11")
                        stok_mehsul_ciximi(stok, int(mehsul_sayi))
                        muqavile_umumi_mebleg = umumi_mebleg(mehsul.qiymet, int(mehsul_sayi))
                        return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
                    
                    elif((ilkin_odenis == "" and ilkin_odenis_qaliq != "") or (float(ilkin_odenis) == 0 and ilkin_odenis_qaliq != "")):
                        return Response({"detail": "İlkin ödəniş daxil edilmən qalıq ilkin ödəniş daxil edilə bilməz"}, status=status.HTTP_400_BAD_REQUEST)

                    elif(float(ilkin_odenis) == 0):
                        print("Burdayam17")
                        # Umumi ilkin odenis meblegi 0 olarsa
                        return Response({"detail": "İlkin ödəniş 0 azn daxil edilə bilməz"}, status=status.HTTP_400_BAD_REQUEST)
                    elif(ilkin_odenis_qaliq != ""):
                        print("Burdayam 19")
                        if((indiki_tarix_san == ilkin_odenis_tarixi_san) and (indiki_tarix_san < ilkin_odenis_qaliq_tarixi_san)):
                            print("Burdayam21")
                            stok_mehsul_ciximi(stok, int(mehsul_sayi))
                            print("Burdayam 21")
                            muqavile_umumi_mebleg = umumi_mebleg(mehsul.qiymet, int(mehsul_sayi))
                            print(f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg}")
                            serializer.save(vanleader=user, shirket = shirket, ofis = ofis, shobe = shobe, ilkin_odenis = ilkin_odenis, ilkin_odenis_qaliq = ilkin_odenis_qaliq, ilkin_odenis_status = "BİTMİŞ", qaliq_ilkin_odenis_status = "DAVAM EDƏN", muqavile_umumi_mebleg = muqavile_umumi_mebleg)
                            print("Burdayam 21")
                            return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
                        
                        elif((indiki_tarix_san == ilkin_odenis_tarixi_san) and (ilkin_odenis_tarixi_san == ilkin_odenis_qaliq_tarixi_san)):
                            print("Burdayam 22")
                            return Response({"detail": "İlkin ödəniş qalıq və ilkin ödəniş hər ikisi bu günki tarixə qeyd oluna bilməz"}, status=status.HTTP_400_BAD_REQUEST)
                        elif(indiki_tarix_san == ilkin_odenis_qaliq_tarixi_san):
                            print("Burdayam 23")
                            return Response({"detail": "İlkin ödəniş qalıq bu günki tarixə qeyd oluna bilməz"}, status=status.HTTP_400_BAD_REQUEST)
                        elif(ilkin_odenis_tarixi_san > ilkin_odenis_qaliq_tarixi_san):
                            print("Burdayam 23.5")
                            return Response({"detail": "İlkin ödəniş qalıq tarixi ilkin ödəniş tarixindən əvvəl ola bilməz"}, status=status.HTTP_400_BAD_REQUEST)
                        elif(ilkin_odenis_tarixi_san == ilkin_odenis_qaliq_tarixi_san):
                            print("Burdayam 24")
                            return Response({"detail": "İlkin ödəniş qalıq və ilkin ödəniş hər ikisi eyni tarixə qeyd oluna bilməz"}, status=status.HTTP_400_BAD_REQUEST)    
                        elif((indiki_tarix_san > ilkin_odenis_tarixi_san) or (indiki_tarix_san > ilkin_odenis_qaliq_tarixi_san)):
                            print("Burdayam 25")
                            return Response({"detail": "İlkin ödəniş tarixini keçmiş tarixə təyin edə bilməzsiniz"}, status=status.HTTP_400_BAD_REQUEST)

                        elif(indiki_tarix_san < ilkin_odenis_tarixi_san):
                            print("Burdayam 26")
                            stok_mehsul_ciximi(stok, int(mehsul_sayi))
                            print("Bura 12 ishe dushdu")
                            muqavile_umumi_mebleg = umumi_mebleg(mehsul.qiymet, int(mehsul_sayi))
                            print(f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg}")
                            serializer.save(vanleader=user, shirket = shirket, ofis = ofis, shobe = shobe, ilkin_odenis = ilkin_odenis, ilkin_odenis_qaliq = ilkin_odenis_qaliq, ilkin_odenis_status = "DAVAM EDƏN", qaliq_ilkin_odenis_status = "DAVAM EDƏN", muqavile_umumi_mebleg = muqavile_umumi_mebleg)
                            print("Burdayam 11")
                            return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
                        elif((indiki_tarix_san < ilkin_odenis_tarixi_san) and (indiki_tarix_san < ilkin_odenis_qaliq_tarixi_san)):
                            print("Burdayam 27")
                            stok_mehsul_ciximi(stok, int(mehsul_sayi))
                            print("Bura 27 ishe dushdu")
                            muqavile_umumi_mebleg = umumi_mebleg(mehsul.qiymet, int(mehsul_sayi))
                            print(f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg}")
                            serializer.save(vanleader=user, shirket = shirket, ofis = ofis, shobe = shobe, ilkin_odenis = ilkin_odenis, ilkin_odenis_qaliq = ilkin_odenis_qaliq, ilkin_odenis_status = "DAVAM EDƏN", qaliq_ilkin_odenis_status = "DAVAM EDƏN", muqavile_umumi_mebleg = muqavile_umumi_mebleg)
                            print("Burdayam 27")
                            return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
                        
                        print("Burdayam 28")
                        stok_mehsul_ciximi(stok, int(mehsul_sayi))
                        print("Bura 28 ishe dushdu")
                        muqavile_umumi_mebleg = umumi_mebleg(mehsul.qiymet, int(mehsul_sayi))
                        print(f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg}")
                        
                        return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
                    else:
                        print("Burdayam 30")
                        return Response({"detail": "Qalıq ilkin ödəniş doğru daxil edilməyib."}, status=status.HTTP_400_BAD_REQUEST)
                
            elif(odenis_uslubu == "NƏĞD"):
                if(kredit_muddeti != ""):
                    return Response({"detail": "Kredit müddəti ancaq status kredit olan müqavilələr üçündür"}, status=status.HTTP_400_BAD_REQUEST)
                if(ilkin_odenis != "" or ilkin_odenis_qaliq != ""):
                    return Response({"detail": "İlkin ödəniş ancaq status kredit olan müqavilələr üçündür"}, status=status.HTTP_400_BAD_REQUEST)
                if(mehsul_sayi == ""):
                    mehsul_sayi = 1
                
                stok_mehsul_ciximi(stok, int(mehsul_sayi))
                muqavile_umumi_mebleg = umumi_mebleg(mehsul.qiymet, int(mehsul_sayi))
                print(f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg}")
                serializer.save(vanleader=user, shirket = shirket, ofis = ofis, muqavile_status="BİTMİŞ", shobe = shobe, muqavile_umumi_mebleg = muqavile_umumi_mebleg)
                return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
            elif(odenis_uslubu == "İKİ DƏFƏYƏ NƏĞD"):
                if(mehsul_sayi == ""):
                    mehsul_sayi = 1
                print("Burdayam")
                if(kredit_muddeti != ""):
                    print("Burdayam 16")
                    return Response({"detail": "Kredit müddəti ancaq status kredit olan müqavilələr üçündür"}, status=status.HTTP_400_BAD_REQUEST)
                
                negd_odenis_1 = request.data.get("negd_odenis_1")
                print(f"negd_odenis_1 ==> {type(negd_odenis_1)}")
                negd_odenis_2 = request.data.get("negd_odenis_2")
                print(f"negd_odenis_2 ==> {type(negd_odenis_2)}")
                muqavile_umumi_mebleg = umumi_mebleg(mehsul.qiymet, int(mehsul_sayi))
                print(f"muqavile_umumi_mebleg ==> {muqavile_umumi_mebleg} --- {type(muqavile_umumi_mebleg)}")

                if(negd_odenis_1 == "" or negd_odenis_2 == "" or negd_odenis_1 == "0" or negd_odenis_2 == "0"):
                    print("In1")
                    return Response({"detail": "2 dəfəyə nəğd ödəniş statusunda hər 2 nəğd ödəniş qeyd olunmalıdır"}, status=status.HTTP_400_BAD_REQUEST)
                elif(float(negd_odenis_1) > muqavile_umumi_mebleg):
                    return Response({"detail": "Daxil etdiyiniz məbləğ müqavilənin ümumi məbləğindən daha çoxdur"}, status=status.HTTP_400_BAD_REQUEST)
                
                elif(float(negd_odenis_2) > muqavile_umumi_mebleg):
                    return Response({"detail": "Daxil etdiyiniz məbləğ müqavilənin ümumi məbləğindən daha çoxdur"}, status=status.HTTP_400_BAD_REQUEST)
                elif(float(negd_odenis_1) + float(negd_odenis_2) == muqavile_umumi_mebleg):
                    
                    if((indiki_tarix_san == negd_odenis_1_tarix_san) and (indiki_tarix_san < negd_odenis_2_tarix_san)):
                        print("In2")
                        stok_mehsul_ciximi(stok, int(mehsul_sayi))
                        serializer.save(vanleader=user, shirket = shirket, ofis = ofis, shobe = shobe, negd_odenis_1_status = "BİTMİŞ", negd_odenis_2_status = "DAVAM EDƏN", muqavile_umumi_mebleg = muqavile_umumi_mebleg)
                        return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
                    
                    elif((indiki_tarix_san == negd_odenis_1_tarix_san) and (negd_odenis_1_tarix_san == negd_odenis_2_tarix_san)):
                        print("Burdayam 22")
                        return Response({"detail": "Ödənişlərin hər ikisi bu günki tarixə qeyd oluna bilməz"}, status=status.HTTP_400_BAD_REQUEST)
                    
                    elif(indiki_tarix_san == negd_odenis_2_tarix_san):
                        print("Burdayam 23")
                        return Response({"detail": "Qalıq nəğd ödəniş bu günki tarixə qeyd oluna bilməz"}, status=status.HTTP_400_BAD_REQUEST)
                    
                    elif(negd_odenis_1_tarix_san > negd_odenis_2_tarix_san):
                        print("Burdayam 23.5")
                        return Response({"detail": "Qalıq nəğd ödəniş tarixi nəğd ödəniş tarixindən əvvəl ola bilməz"}, status=status.HTTP_400_BAD_REQUEST)
                    
                    elif(negd_odenis_1_tarix_san == negd_odenis_2_tarix_san):
                        print("Burdayam 24")
                        return Response({"detail": "Qalıq nəğd ödəniş və nəğd ödəniş hər ikisi eyni tarixə qeyd oluna bilməz"}, status=status.HTTP_400_BAD_REQUEST)    
                    
                    elif((indiki_tarix_san > negd_odenis_1_tarix_san) or (indiki_tarix_san > negd_odenis_2_tarix_san)):
                        print("Burdayam 25")
                        return Response({"detail": "Nəğd ödəniş tarixini keçmiş tarixə təyin edə bilməzsiniz"}, status=status.HTTP_400_BAD_REQUEST)

                    elif(indiki_tarix_san < negd_odenis_1_tarix_san):
                        stok_mehsul_ciximi(stok, int(mehsul_sayi))
                        serializer.save(vanleader=user, shirket = shirket, ofis = ofis, shobe = shobe, negd_odenis_1_status = "DAVAM EDƏN", negd_odenis_2_status = "DAVAM EDƏN", muqavile_umumi_mebleg = muqavile_umumi_mebleg)
                        return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
                    
                    elif((indiki_tarix_san < negd_odenis_1_tarix_san) and (indiki_tarix_san < negd_odenis_2_tarix_san)):
                        stok_mehsul_ciximi(stok, int(mehsul_sayi))
                        serializer.save(vanleader=user, shirket = shirket, ofis = ofis, shobe = shobe, negd_odenis_1_status = "DAVAM EDƏN", negd_odenis_2_status = "DAVAM EDƏN", muqavile_umumi_mebleg = muqavile_umumi_mebleg)
                        return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
                    
                elif(float(negd_odenis_1) + float(negd_odenis_2) != muqavile_umumi_mebleg):
                    print("In3")
                    return Response({"detail": "Ödəmək istədiyiniz məbləğlər məhsulun qiymətinə bərabər deyil"}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({"detail": "Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
    except:
        return Response({"detail": "Anbarın stokunda məhsul yoxdur"}, status=status.HTTP_400_BAD_REQUEST)

def muqavile_patch(self, request, *args, **kwargs):
    muqavile = self.get_object()
    serializer = MuqavileSerializer(muqavile, data=request.data, partial=True)
    print(f"request.data ===> {request.data}")
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
    print(f"odemek_istediyi_qaliq_ilkin_odenis ===> {odemek_istediyi_qaliq_ilkin_odenis}")

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
    print(f"odemek_istediyi_negd_odenis_1 ===> {odemek_istediyi_negd_odenis_1}")

    odemek_istediyi_negd_odenis_2 = request.data.get("negd_odenis_2")
    print(f"odemek_istediyi_negd_odenis_2 ===> {odemek_istediyi_negd_odenis_2}")

    my_time = datetime.datetime.min.time()

    indiki_tarix_date = datetime.date.today()
    indiki_tarix = datetime.datetime.combine(indiki_tarix_date, my_time)
    indiki_tarix_san = datetime.datetime.timestamp(indiki_tarix)
    print(f"indiki_tarix_san ===> {indiki_tarix_san}")
    
    if(muqavile.odenis_uslubu == "KREDİT"):
        if(odemek_istediyi_ilkin_odenis != None and ilkin_odenis_status == "DAVAM EDƏN"):
            if(float(odemek_istediyi_ilkin_odenis) != ilkin_odenis):
                return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
            elif(float(odemek_istediyi_ilkin_odenis) == ilkin_odenis):
                print("Burda1")
                muqavile.ilkin_odenis_status = "BİTMİŞ"
                muqavile.ilkin_odenis_tarixi = indiki_tarix_date
                muqavile.save()
                return Response({"detail": "İlkin ödəniş ödənildi"}, status=status.HTTP_200_OK)
                    
        if(odemek_istediyi_qaliq_ilkin_odenis != None and  ilkin_odenis_status == "BİTMİŞ" and qaliq_ilkin_odenis_status == "DAVAM EDƏN"):
            if(float(odemek_istediyi_qaliq_ilkin_odenis) == ilkin_odenis_qaliq):
                print("Burda2")
                muqavile.qaliq_ilkin_odenis_status = "BİTMİŞ"
                muqavile.ilkin_odenis_qaliq_tarixi = indiki_tarix_date
                muqavile.save()
                return Response({"detail": "Qalıq ilkin ödəniş ödənildi"}, status=status.HTTP_200_OK)
            elif(float(odemek_istediyi_qaliq_ilkin_odenis) != ilkin_odenis_qaliq):
                return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

    if(muqavile.odenis_uslubu == "İKİ DƏFƏYƏ NƏĞD"):
        if(odemek_istediyi_negd_odenis_1 != None and negd_odenis_1_status == "DAVAM EDƏN"):
            if(float(odemek_istediyi_negd_odenis_1) != negd_odenis_1):
                return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
            elif(float(odemek_istediyi_negd_odenis_1) == negd_odenis_1):
                print("Burda1")
                muqavile.negd_odenis_1_status = "BİTMİŞ"
                muqavile.negd_odenis_1_tarix = indiki_tarix_date
                muqavile.save()
                return Response({"detail": "1-ci ödəniş ödənildi"}, status=status.HTTP_200_OK)
                    
        if(odemek_istediyi_negd_odenis_2 != None and  negd_odenis_1_status == "BİTMİŞ" and negd_odenis_2_status == "DAVAM EDƏN"):
            if(float(odemek_istediyi_negd_odenis_2) == negd_odenis_2):
                print("Burda2")
                muqavile.negd_odenis_2_status = "BİTMİŞ"
                muqavile.negd_odenis_2_tarix = indiki_tarix_date
                muqavile.muqavile_status="BİTMİŞ"
                muqavile.save()
                return Response({"detail": "Qalıq nəğd ödəniş ödənildi"}, status=status.HTTP_200_OK)
            elif(float(odemek_istediyi_negd_odenis_2) != negd_odenis_2):
                return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

def muqavile_update(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    muqavile = self.get_object()
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
    print(f"odemek_istediyi_qaliq_ilkin_odenis ===> {odemek_istediyi_qaliq_ilkin_odenis}")

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
    print(f"odemek_istediyi_negd_odenis_1 ===> {odemek_istediyi_negd_odenis_1}")

    odemek_istediyi_negd_odenis_2 = request.data.get("negd_odenis_2")
    print(f"odemek_istediyi_negd_odenis_2 ===> {odemek_istediyi_negd_odenis_2}")

    my_time = datetime.datetime.min.time()

    indiki_tarix_date = datetime.date.today()
    indiki_tarix = datetime.datetime.combine(indiki_tarix_date, my_time)
    indiki_tarix_san = datetime.datetime.timestamp(indiki_tarix)
    print(f"indiki_tarix_san ===> {indiki_tarix_san}")
    
    if(muqavile.odenis_uslubu == "KREDİT"):
        if(odemek_istediyi_ilkin_odenis != None and ilkin_odenis_status == "DAVAM EDƏN"):
            if(float(odemek_istediyi_ilkin_odenis) != ilkin_odenis):
                return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
            elif(float(odemek_istediyi_ilkin_odenis) == ilkin_odenis):
                print("Burda1")
                muqavile.ilkin_odenis_status = "BİTMİŞ"
                muqavile.ilkin_odenis_tarixi = indiki_tarix_date
                muqavile.save()
                return Response({"detail": "İlkin ödəniş ödənildi"}, status=status.HTTP_200_OK)
                    
        if(odemek_istediyi_qaliq_ilkin_odenis != None and  ilkin_odenis_status == "BİTMİŞ" and qaliq_ilkin_odenis_status == "DAVAM EDƏN"):
            if(float(odemek_istediyi_qaliq_ilkin_odenis) == ilkin_odenis_qaliq):
                print("Burda2")
                muqavile.qaliq_ilkin_odenis_status = "BİTMİŞ"
                muqavile.ilkin_odenis_qaliq_tarixi = indiki_tarix_date
                muqavile.save()
                return Response({"detail": "Qalıq ilkin ödəniş ödənildi"}, status=status.HTTP_200_OK)
            elif(float(odemek_istediyi_qaliq_ilkin_odenis) != ilkin_odenis_qaliq):
                return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

    if(muqavile.odenis_uslubu == "İKİ DƏFƏYƏ NƏĞD"):
        if(odemek_istediyi_negd_odenis_1 != None and negd_odenis_1_status == "DAVAM EDƏN"):
            if(float(odemek_istediyi_negd_odenis_1) != negd_odenis_1):
                return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
            elif(float(odemek_istediyi_negd_odenis_1) == negd_odenis_1):
                print("Burda1")
                muqavile.negd_odenis_1_status = "BİTMİŞ"
                muqavile.negd_odenis_1_tarix = indiki_tarix_date
                muqavile.save()
                return Response({"detail": "1-ci ödəniş ödənildi"}, status=status.HTTP_200_OK)
                    
        if(odemek_istediyi_negd_odenis_2 != None and  negd_odenis_1_status == "BİTMİŞ" and negd_odenis_2_status == "DAVAM EDƏN"):
            if(float(odemek_istediyi_negd_odenis_2) == negd_odenis_2):
                print("Burda2")
                muqavile.negd_odenis_2_status = "BİTMİŞ"
                muqavile.negd_odenis_2_tarix = indiki_tarix_date
                muqavile.muqavile_status="BİTMİŞ"
                muqavile.save()
                return Response({"detail": "Qalıq nəğd ödəniş ödənildi"}, status=status.HTTP_200_OK)
            elif(float(odemek_istediyi_negd_odenis_2) != negd_odenis_2):
                return Response({"detail": "Məbləği düzgün daxil edin"}, status=status.HTTP_400_BAD_REQUEST)