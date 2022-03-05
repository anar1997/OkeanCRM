from rest_framework import generics
from django.contrib.auth import user_logged_in
from rest_framework import status
from rest_framework.exceptions import ValidationError

import math
import pandas as pd

import datetime
from dateutil.relativedelta import relativedelta

from rest_framework.response import Response
from rest_framework import generics
from .serializers import (
    AnbarSerializer,
    HoldingSerializer,
    KomandaSerializer,
    EmeliyyatSerializer,
    OdemeTarixSerializer,
    HediyyeSerializer,
    MehsullarSerializer,
    OfisSerializer,
    MuqavileSerializer,
    MusteriQeydlerSerializer,
    ShirketSerializer,
    ShobeSerializer,
    UserSerializer,
    MusteriSerializer,
    VezifelerSerializer,
    AnbarQeydlerSerializer,
    RegisterSerializer,
    ServisSerializer,
    StokSerializer,
    HoldingdenShirketlereTransferSerializer,
    ShirketdenHoldingeTransferSerializer,
    OfisdenShirketeTransferSerializer,
    ShirketdenOfislereTransferSerializer,
    OfisKassaSerializer,
    ShirketKassaSerializer,
    HoldingKassaSerializer,
    MaasSerializer,
    BonusSerializer,
)
from mehsullar.models import (
    Emeliyyat, 
    Hediyye, 
    Muqavile, 
    OdemeTarix, 
    Anbar, 
    Mehsullar, 
    AnbarQeydler, 
    Servis, 
    Stok
)
from account.models import (
    MusteriQeydler, 
    Shirket, 
    Shobe, 
    User, 
    Musteri, 
    Vezifeler, 
    Ofis, 
    Komanda, 
    Holding, 
    ShirketKassa, 
    OfisKassa,
    HoldingKassa,
    HoldingdenShirketlereTransfer,
    OfisdenShirketeTransfer,
    ShirketdenHoldingeTransfer,
    ShirketdenOfislereTransfer,
    Maas,
    Bonus,
)
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import jwt_decode_handler

from django_filters.rest_framework import DjangoFilterBackend

from .filters import (
    OdemeTarixFilter,
    MuqavileFilter,
)

import datetime
from rest_framework.generics import get_object_or_404


# ********************************** user get post put delete **********************************


class RegisterApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)

        data = data.data

        acces_token = jwt_decode_handler(data.get("access"))

        if not User.objects.filter(id=acces_token.get("user_id")).last():
            return Response({"error": True, "message": "No such a user"}, status=status.HTTP_404_NOT_FOUND)

        user = User.objects.filter(id=acces_token.get("user_id")).last()
        user_logged_in.send(sender=type(user), request=request, user=user)

        user_details = UserSerializer(user)

        data["user_details"] = user_details.data
        return Response(data)


# ********************************** musteri get post put delete **********************************
class MusteriListCreateAPIView(generics.ListCreateAPIView):
    queryset = Musteri.objects.all()
    serializer_class = MusteriSerializer


class MusteriDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musteri.objects.all()
    serializer_class = MusteriSerializer


# ********************************** musteriqeydlerin put delete post get **********************************

class MusteriQeydlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = MusteriQeydler.objects.all()
    serializer_class = MusteriQeydlerSerializer


class MusteriQeydlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MusteriQeydler.objects.all()
    serializer_class = MusteriQeydlerSerializer


# ********************************** muqavile get post put delete **********************************


class MuqavileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Muqavile.objects.all()
    serializer_class = MuqavileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MuqavileFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = self.request.user
        print(f"login olan user ==> {user}")

        mehsul_id = int(request.POST["mehsul_id"])
        print(f"mehsul id ==> {mehsul_id}")
        mehsul = get_object_or_404(Mehsullar, pk=mehsul_id)
        print(f"mehsul ==> {mehsul}")

        verilecek_ilkin_odenis = request.POST["verilecek_ilkin_odenis"]
        print(f"verilecek_ilkin_odenis ==> {verilecek_ilkin_odenis}")

        ilkin_odenis = request.POST["ilkin_odenis"]
        print(f"ilkin_odenis ==> {ilkin_odenis}")
        
        ilkin_odenis_qaliq = request.POST["ilkin_odenis_qaliq"]
        print(f"ilkin_odenis_qaliq ==> {ilkin_odenis_qaliq}")


        if (user.is_superuser == True or user.vezife.vezife_adi == "VANLEADER"):
            anbar = get_object_or_404(Anbar, ofis=user.ofis)
            print(f"anbar ==> {anbar}")
            print(f"ofis ==> {user.ofis}")
            stok = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul)
            print(f"stok ==> {stok}")

            try:
                stok = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul)
                print(f"stok ==> {stok}")
                if (serializer.is_valid()):
                    stok.say = stok.say - 1
                    stok.save()
                    if (stok.say == 0):
                        stok.delete()
                    print(f"stok say ==> {stok.say}")
                    print(float(verilecek_ilkin_odenis) == float(ilkin_odenis))

                    if(float(verilecek_ilkin_odenis) == float(ilkin_odenis)):
                        serializer.save(vanleader=user, ilkin_odenis_status=True)
                        print("Bura 1 ishe dushdu")
                    elif(ilkin_odenis_qaliq != ""):
                        if(float(verilecek_ilkin_odenis) == (float(ilkin_odenis) + float(ilkin_odenis_qaliq))):
                            serializer.save(vanleader=user, ilkin_odenis_status=True)
                            print("Bura 2 ishe dushdu")
                    else:
                        serializer.save(vanleader=user)
                    
                    return Response({"Müqavilə müvəffəqiyyətlə imzalandı"}, status=status.HTTP_201_CREATED)
            except:
                return Response({"Anbarın stokunda məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)


class MuqavileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Muqavile.objects.all()
    serializer_class = MuqavileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MuqavileFilter

    # def update(self, request, *args, **kwargs):
    #     mehsul_id = int(request.POST["mehsul_id"])
    #     print(f"mehsul id ==> {mehsul_id}")

    #     mehsul = get_object_or_404(Mehsullar, pk=mehsul_id)
    #     print(f"mehsul ==> {mehsul}")

    #     ilkin_odenis = request.POST["ilkin_odenis"]
    #     print(f"ilkin_odenis ==> {ilkin_odenis}")

    #     serializer = self.get_serializer(data=request.data)
    #     if (serializer.is_valid()):
    #         if(ilkin_odenis != ""):
    #                     serializer.save(ilkin_odenis_status=True)


# ********************************** komanda get post put delete **********************************


class KomandaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Komanda.objects.all()
    serializer_class = KomandaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"detail": "Komanda müvəffəqiyyətlə düzəldildi"}, status=status.HTTP_201_CREATED, headers=headers)


class KomandaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Komanda.objects.all()
    serializer_class = KomandaSerializer

# ********************************** odeme tarixi put get post delete **********************************


class OdemeTarixListCreateAPIView(generics.ListCreateAPIView):
    queryset = OdemeTarix.objects.all()
    serializer_class = OdemeTarixSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OdemeTarixFilter

class OdemeTarixDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OdemeTarix.objects.all()
    serializer_class = OdemeTarixSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['muqavile']
    filterset_class = OdemeTarixFilter
    
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        odenme_status = request.POST.get("odenme_status")
        natamama_gore_odeme_status = request.POST.get("natamama_gore_odeme_status")
        sifira_gore_odeme_status = request.POST.get("sifira_gore_odeme_status")

        # Natamam Ay odeme statusu ile bagli emeliyyatlar
        if(odenme_status == "NATAMAM AY"):
            indiki_ay = self.get_object()
            muqavile = indiki_ay.muqavile
            ilkin_odenis = muqavile.ilkin_odenis
            ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
            ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
            print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
            mehsulun_qiymeti = muqavile.mehsul.qiymet
            print(f"mehsulun ==> {mehsulun_qiymeti}")
            indiki_ay = self.get_object()
            indiki_ay.odenme_status = "NATAMAM AY"
            indiki_ay.save()

            odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
            odemek_istediyi_mebleg = float(request.POST.get("qiymet"))
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
                indiki_ay.natamama_gore_odeme_status = "NATAMAM DİGƏR AYLAR"
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
                indiki_ay.odenme_status = "NATAMAM AY"
                indiki_ay.natamama_gore_odeme_status = "NATAMAM NÖVBƏTİ AY"
                indiki_ay.save()
                return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
            if(natamama_gore_odeme_status == "NATAMAM SONUNCU AY"):
                indiki_ay = self.get_object()
                natamam_odemek_istediyi_mebleg = indiki_ay.qiymet - odemek_istediyi_mebleg

                sonuncu_ay = self.get_queryset()[len(self.get_queryset())-1]
                sonuncu_ay.qiymet = sonuncu_ay.qiymet + natamam_odemek_istediyi_mebleg
                sonuncu_ay.save()

                indiki_ay.qiymet = odemek_istediyi_mebleg
                indiki_ay.odenme_status = "NATAMAM AY"
                indiki_ay.natamama_gore_odeme_status = "NATAMAM SONUNCU AY"
                indiki_ay.save()
                return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        # Buraxilmis Ay odeme statusu ile bagli emeliyyatlar
        elif(odenme_status == "BURAXILMIŞ AY"):
            indiki_ay = self.get_object()
            muqavile = indiki_ay.muqavile
            ilkin_odenis = muqavile.ilkin_odenis
            ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
            mehsulun_qiymeti = muqavile.mehsul.qiymet
            print(f"mehsulun ==> {mehsulun_qiymeti}")
            ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
            print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
            indiki_ay.odenme_status = "BURAXILMIŞ AY"
            indiki_ay.save()
            odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
            odemek_istediyi_mebleg = float(request.POST.get("qiymet"))
            
            if(sifira_gore_odeme_status == "SIFIR NÖVBƏTİ AY"):
                novbeti_ay = get_object_or_404(OdemeTarix, pk=self.get_object().id+1)
                novbeti_ay.qiymet = novbeti_ay.qiymet + indiki_ay.qiymet
                novbeti_ay.save()
                indiki_ay.qiymet = 0
                indiki_ay.odenme_status = "BURAXILMIŞ AY"
                indiki_ay.sifira_gore_odeme_status = "SIFIR NÖVBƏTİ AY"
                indiki_ay.save()
                return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
            if(sifira_gore_odeme_status == "SIFIR SONUNCU AY"):
                sonuncu_ay = self.get_queryset()[len(self.get_queryset())-1]
                sonuncu_ay.qiymet = sonuncu_ay.qiymet + indiki_ay.qiymet
                sonuncu_ay.save()
                indiki_ay.qiymet = 0
                indiki_ay.odenme_status = "BURAXILMIŞ AY"
                indiki_ay.sifira_gore_odeme_status = "SIFIR SONUNCU AY"
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
                indiki_ay.sifira_gore_odeme_status = "SIFIR DİGƏR AYLAR"
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
        elif(odenme_status == "YENİ QRAFİK"):
            indiki_ay = self.get_object()
            muqavile = indiki_ay.muqavile
            m = get_object_or_404(Muqavile, pk = muqavile.id)
            print(f"m ===> {m}")
            ilkin_odenis = muqavile.ilkin_odenis
            ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
            ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
            print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
            mehsulun_qiymeti = muqavile.mehsul.qiymet
            print(f"mehsulun ==> {mehsulun_qiymeti}")

            odenen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNƏN")
            print(f"odenen_odemetarixler ==> {odenen_odemetarixler}")
            
            odenmeyen_odemetarixler = OdemeTarix.objects.filter(muqavile=muqavile, odenme_status="ÖDƏNMƏYƏN")
            print(f"odenmeyen_odemetarixler ==> {odenmeyen_odemetarixler}")
            
            odemek_istediyi_mebleg = float(request.POST.get("qiymet"))
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
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        elif(odenme_status == "RAZILAŞDIRILMIŞ AZ ÖDƏMƏ"):
            indiki_ay = self.get_object()
            muqavile = indiki_ay.muqavile
            ilkin_odenis = muqavile.ilkin_odenis
            ilkin_odenis_qaliq = muqavile.ilkin_odenis_qaliq
            ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
            print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam}")
            mehsulun_qiymeti = muqavile.mehsul.qiymet
            print(f"mehsulun ==> {mehsulun_qiymeti}")
            indiki_ay.odenme_status = "RAZILAŞDIRILMIŞ AZ ÖDƏMƏ"
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
        elif(odenme_status == "ARTIQ ÖDƏMƏ"):
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
            indiki_ay.odenme_status = "ARTIQ ÖDƏMƏ"
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

        # Odenen statusu ile bagli emeliyyatlar
        elif(odenme_status == "ÖDƏNƏN"):
            indiki_ay = self.get_object()
            indiki_ay.odenme_status = "ÖDƏNƏN"
            indiki_ay.sifira_gore_odeme_status = None
            indiki_ay.natamama_gore_odeme_status = None
            indiki_ay.save()
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        else:
            if(serializer.is_valid()):
                super(OdemeTarixDetailAPIView, self).update(request, *args, **kwargs)
                return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        return Response({"detail": "Xəta baş verdi"}, status=status.HTTP_400_BAD_REQUEST)


# ********************************** anbar put get post delete **********************************


class AnbarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Anbar.objects.all()
    serializer_class = AnbarSerializer


class AnbarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anbar.objects.all()
    serializer_class = AnbarSerializer


# ********************************** mehsullar put get post delete **********************************


class MehsullarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mehsullar.objects.all()
    serializer_class = MehsullarSerializer


class MehsullarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mehsullar.objects.all()
    serializer_class = MehsullarSerializer


# ********************************** merkezler put delete post get **********************************


class OfisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ofis.objects.all()
    serializer_class = OfisSerializer


class OfisDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ofis.objects.all()
    serializer_class = OfisSerializer


# ********************************** vezifeler put delete post get **********************************


class VezifelerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vezifeler.objects.all()
    serializer_class = VezifelerSerializer


class VezifelerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vezifeler.objects.all()
    serializer_class = VezifelerSerializer


# ********************************** anbar put delete post get **********************************


class AnbarQeydlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = AnbarQeydler.objects.all()
    serializer_class = AnbarQeydlerSerializer


class AnbarQeydlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnbarQeydler.objects.all()
    serializer_class = AnbarQeydlerSerializer


# ********************************** shirket put delete post get **********************************
class ShirketListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shirket.objects.all()
    serializer_class = ShirketSerializer


class ShirketDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shirket.objects.all()
    serializer_class = ShirketSerializer


# ********************************** shobe put delete post get **********************************


class ShobeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shobe.objects.all()
    serializer_class = ShobeSerializer


class ShobeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shobe.objects.all()
    serializer_class = ShobeSerializer


# ********************************** emeliyyat put delete post get **********************************


class EmeliyyatListCreateAPIView(generics.ListCreateAPIView):
    queryset = Emeliyyat.objects.all()
    serializer_class = EmeliyyatSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        gonderen = int(request.POST["gonderen_id"])
        print(f"Gonderen id ==> {gonderen}")
        gonderen_anbar = get_object_or_404(Anbar, pk=gonderen)
        print(f"Gonderen anbar ==> {gonderen_anbar}")
        qebul_eden_id = int(request.POST["qebul_eden_id"])
        print(f"qebul_eden id ==> {qebul_eden_id}")
        qebul_eden = get_object_or_404(Anbar, pk=qebul_eden_id)
        print(f"qebul_eden anbar ==> {qebul_eden}")

        gonderilen_mehsul_id = int(request.POST["gonderilen_mehsul_id"])
        print(f"Gonderilen mehsul id ==> {gonderilen_mehsul_id}")
        gonderilen_mehsul = get_object_or_404(Mehsullar, pk=gonderilen_mehsul_id)
        print(f"Gonderilen mehsul ==> {gonderilen_mehsul}")
        say = int(request.POST["mehsulun_sayi"])
        print(f"say ==> {say}")

        qeyd = request.POST["qeyd"]
        print(f"qeyd ==> {qeyd}")

        try:
            stok1 = get_object_or_404(Stok, anbar=gonderen_anbar, mehsul=gonderilen_mehsul)
            print(f"Stok1 ==> {stok1}")
            print(f"stok1.say ==> {stok1.say}")
            if (say > stok1.say):
                return Response({"Göndərən anbarda yetəri qədər məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
            try:
                stok2 = get_object_or_404(Stok, anbar=qebul_eden)
                print(f"stok2 ==> {stok2}")
                if (stok1 == stok2):
                    print("307 ISE DUSDU")
                    return Response({"Göndərən və göndərilən anbar eynidir!"}, status=status.HTTP_404_NOT_FOUND)
                stok1.say = stok1.say - say
                print(f"stok1.say ==> {stok1.say}")
                stok1.save()
                print("1 calisdi **********")
                if (stok1.say == 0):
                    stok1.delete()
                    print(f"stok1.say ==> {stok1.say}")
                    print("2 calisdi **********")
                print("322 ishe DUSDU")
                print(f"stok2 ==> {stok2}")
                print(f"stok2.say ==> {stok2.say}")
                stok2.say = stok2.say + say
                stok2.save()
                print(f"stok2.say ==> {stok2.say}")
                print("3 calisdi **********")
                if (serializer.is_valid()):
                    serializer.save(gonderen=gonderen_anbar)
                return Response({"Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
            except:
                stok2 = Stok.objects.create(anbar=qebul_eden, mehsul=gonderilen_mehsul, say=say)
                if (stok1 == stok2):
                    print("BURA DAAAA ISE DUSDU")
                    return Response({"Göndərən və göndərilən anbar eynidir!"}, status=status.HTTP_404_NOT_FOUND)
                stok2.save()
                print(f"stok2.say ==> {stok2.say}")
                print("4 calisdi **********")
                if (serializer.is_valid()):
                    serializer.save(gonderen=gonderen_anbar)
                return Response({"Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        except:
            print("5 calisdi **********")
            return Response({"Göndərən anbarda məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)


class EmeliyyatDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emeliyyat.objects.all()
    serializer_class = EmeliyyatSerializer


# ********************************** hediyye put delete post get **********************************


class HediyyeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hediyye.objects.all()
    serializer_class = HediyyeSerializer


class HediyyeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hediyye.objects.all()
    serializer_class = HediyyeSerializer


# ********************************** servis put delete post get **********************************

class ServisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Servis.objects.all()
    serializer_class = ServisSerializer

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


class StokDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stok.objects.all()
    serializer_class = StokSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        mehsul_id = int(request.POST["mehsul_id"])
        say = int(request.POST["say"])
        anbar_id = int(request.POST["anbar_id"])
        print(f"mehsul id ==> {mehsul_id}")
        print(f"anbar id ==> {anbar_id}")
        print(f"say ==> {say}")

        mehsul = get_object_or_404(Mehsullar, pk = mehsul_id)
        print(f"Mehsul ==> {mehsul}")
        anbar = get_object_or_404(Anbar, pk=anbar_id)
        print(f"anbar ==> {anbar}")
        try:
            stok = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul)
            print(f"stok ==> {stok}")

            print(f"evvel mehsul_sayi ==> {stok.say}")
            stok.say = stok.say + say
            print(f"sonra mehsul_sayi ==> {stok.say}")
            print("1 ishe dushdu ***********")
            stok.save()
            # super(StokSerializer, self).update(request, *args, **kwargs)
            print("2 ishe dushdu ***********")
            return Response({f"Anbardakı {mehsul} adlı məhsulun sayı artırıldı."}, status=status.HTTP_200_OK)
        except:
            print("3 ishe dushdu ***********")
            return Response({"Problem"}, status=status.HTTP_404_NOT_FOUND)


# ********************************** holding put delete post get **********************************

class HoldingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Holding.objects.all()
    serializer_class = HoldingSerializer


class HoldingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Holding.objects.all()
    serializer_class = HoldingSerializer

# ********************************** kassa put delete post get **********************************

class HoldingKassaListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingKassa.objects.all()
    serializer_class = HoldingKassaSerializer


class HoldingKassaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingKassa.objects.all()
    serializer_class = HoldingKassaSerializer

# **********************************

class ShirketKassaListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketKassa.objects.all()
    serializer_class = ShirketKassaSerializer


class ShirketKassaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketKassa.objects.all()
    serializer_class = ShirketKassaSerializer

# **********************************

class OfisKassaListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisKassa.objects.all()
    serializer_class = OfisKassaSerializer


class OfisKassaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisKassa.objects.all()
    serializer_class = OfisKassaSerializer

# ********************************** transfer put delete post get **********************************

class HoldingdenShirketlereTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = HoldingdenShirketlereTransfer.objects.all()
    serializer_class = HoldingdenShirketlereTransferSerializer


class HoldingdenShirketlereTransferDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HoldingdenShirketlereTransfer.objects.all()
    serializer_class = HoldingdenShirketlereTransferSerializer

# **********************************

class ShirketdenHoldingeTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketdenHoldingeTransfer.objects.all()
    serializer_class = ShirketdenHoldingeTransferSerializer


class ShirketdenHoldingeTransferDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketdenHoldingeTransfer.objects.all()
    serializer_class = ShirketdenHoldingeTransferSerializer

# **********************************

class OfisdenShirketeTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = OfisdenShirketeTransfer.objects.all()
    serializer_class = OfisdenShirketeTransferSerializer


class OfisdenShirketeTransferDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfisdenShirketeTransfer.objects.all()
    serializer_class = OfisdenShirketeTransferSerializer

# **********************************

class ShirketdenOfislereTransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShirketdenOfislereTransfer.objects.all()
    serializer_class = ShirketdenOfislereTransferSerializer


class ShirketdenOfislereTransferDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShirketdenOfislereTransfer.objects.all()
    serializer_class = ShirketdenOfislereTransferSerializer

# ********************************** ishci maas put delete post get **********************************

class MaasListCreateAPIView(generics.ListCreateAPIView):
    queryset = Maas.objects.all()
    serializer_class = MaasSerializer

class MaasDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Maas.objects.all()
    serializer_class = MaasSerializer

# ********************************** ishci elave bonus put delete post get **********************************

class BonusListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

class BonusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer