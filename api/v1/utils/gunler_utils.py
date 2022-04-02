from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from account.models import User
from api.v1.all_serializers.gunler_serializers import (
    HoldingIstisnaIsciSerializer,
    IsciGunlerSerializer,
    HoldingGunlerSerializer,
    KomandaGunlerSerializer, 
    OfisGunlerSerializer,
    ShirketGunlerSerializer,
    ShobeGunlerSerializer,
    VezifeGunlerSerializer
)
from gunler.models import (
    HoldingGunler,
    IsciGunler,
    KomandaGunler,
    OfisGunler,
    ShirketGunler,
    ShobeGunler,
    VezifeGunler
)

# --------------------------------------------------------------------------------------------------------------------------

def company_isci_tetil_hesablama(company, company_name, tarix, tetil_gunleri, is_gunleri_count, qeyri_is_gunu_count, istisna_isciler):
    if(company=="holding"):
        isciler = User.objects.all()
    elif(company=="shirket"):
        isciler = User.objects.filter(shirket=company_name)
    elif(company=="shobe"):
        isciler = User.objects.filter(shobe=company_name)
    elif(company=="ofis"):
        isciler = User.objects.filter(ofis=company_name)
    elif(company=="komanda"):
        isciler = User.objects.filter(komanda=company_name)
    elif(company=="vezife"):
        isciler = User.objects.filter(vezife=company_name)

    print(f"company ==> {company}")
    print(f"company_name ==> {company_name}")
    print(f"isciler ==> {isciler}")
    print(f"tarix ==> {tarix}")

    for isci in isciler:
        if istisna_isciler != None:
            if isci in istisna_isciler:
                continue
        isci_gunler = IsciGunler.objects.get(isci=isci, tarix=tarix)
        isci_gunler.tetil_gunleri = tetil_gunleri
        isci_gunler.is_gunleri_count = is_gunleri_count
        isci_gunler.qeyri_is_gunu_count = qeyri_is_gunu_count
        isci_gunler.save()
    return True

def instisna_isci_create(serializer, company, company_name, obj_gunler):
    print(f"obj_gunler==>{obj_gunler}----{type(obj_gunler)}")

    tarix = obj_gunler.tarix
    print(f"tarix==>{tarix}----{type(tarix)}")

    date_list = []
    tetil_gunleri = serializer.validated_data.get("tetil_gunleri")
    print(f"tetil_gunleri==>{tetil_gunleri}----{type(tetil_gunleri)}")
    tetil_gunleri_l = tetil_gunleri.rstrip("]").lstrip("[").split(",")
    print(f"tetil_gunleri_l==>{tetil_gunleri_l}----{type(tetil_gunleri_l)} -- {len(tetil_gunleri_l)}")
    for i in tetil_gunleri_l:
        new_el = i.strip().strip("'").strip('"')
        date_list.append(new_el)
    print(f"date_list==>{date_list}----{type(date_list)}")

    k_qeyri_is_gunleri = obj_gunler.qeyri_is_gunu_count
    print(f"k_qeyri_is_gunleri==>{k_qeyri_is_gunleri}----{type(k_qeyri_is_gunleri)}")

    qeyri_is_gunu_count = len(date_list)
    print(f"qeyri_is_gunu_count==>{qeyri_is_gunu_count}----{type(qeyri_is_gunu_count)}")

    is_gunleri_count = obj_gunler.is_gunleri_count
    is_gunleri_count = float(is_gunleri_count) - abs((float(k_qeyri_is_gunleri) - float(qeyri_is_gunu_count)))
    print(f"is_gunleri_count==>{is_gunleri_count}----{type(is_gunleri_count)}")

    istisna_isciler = serializer.validated_data.get("istisna_isciler")
    print(f"istisna_isciler==>{istisna_isciler}----{type(istisna_isciler)} -- {len(istisna_isciler)}")

    company_isci_tetil_hesablama(
        company=company, 
        company_name=company_name, 
        tarix=tarix, 
        tetil_gunleri=date_list, 
        is_gunleri_count=is_gunleri_count, 
        qeyri_is_gunu_count=qeyri_is_gunu_count, 
        istisna_isciler=istisna_isciler
    )

    serializer.save(obj_gunler=obj_gunler, tetil_gunleri=date_list, istisna_isciler=istisna_isciler)


def isci_tetil_gunleri_calc(serializer, obj):
    date_list = []
    odenisli_icaze_date_list = []
    odenissiz_icaze_date_list = []

    tetil_gunleri = serializer.validated_data.get("tetil_gunleri")
    print(f"tetil_gunleri==>{tetil_gunleri}----{type(tetil_gunleri)}")
    tetil_gunleri_l = tetil_gunleri.rstrip("]").lstrip("[").split(",")
    print(f"tetil_gunleri_l==>{tetil_gunleri_l}----{type(tetil_gunleri_l)} -- {len(tetil_gunleri_l)}")
    for i in tetil_gunleri_l:
        new_el = i.strip().strip("'").strip('"')
        date_list.append(new_el)

    icaze_gunleri_odenisli = serializer.validated_data.get("icaze_gunleri_odenisli")
    icaze_gunleri_odenissiz = serializer.validated_data.get("icaze_gunleri_odenissiz")
    print(f"icaze_gunleri_odenisli==>{icaze_gunleri_odenisli}----{type(icaze_gunleri_odenisli)}")
    print(f"icaze_gunleri_odenissiz==>{icaze_gunleri_odenissiz}----{type(icaze_gunleri_odenissiz)}")

    icaze_gunleri_odenisli_l = icaze_gunleri_odenisli.rstrip("]").lstrip("[").split(",")
    icaze_gunleri_odenissiz_l = icaze_gunleri_odenissiz.rstrip("]").lstrip("[").split(",")
    print(f"icaze_gunleri_odenisli_l==>{icaze_gunleri_odenisli_l}----{len(icaze_gunleri_odenisli_l)}")
    print(f"icaze_gunleri_odenissiz_l==>{icaze_gunleri_odenissiz_l}----{len(icaze_gunleri_odenissiz_l)}")

    for i in icaze_gunleri_odenisli_l:
        new_elm = i.strip().strip("'").strip('"')
        odenisli_icaze_date_list.append(new_elm)

    for i in icaze_gunleri_odenissiz_l:
        new_elm1 = i.strip().strip("'").strip('"')
        odenissiz_icaze_date_list.append(new_elm1)

    k_qeyri_is_gunleri = obj.qeyri_is_gunu_count
    print(f"k_qeyri_is_gunleri==>{k_qeyri_is_gunleri}----{type(k_qeyri_is_gunleri)}")

    print(f"date_list==>{date_list}----{type(date_list)}")
    print(f"odenisli_icaze_date_list==>{odenisli_icaze_date_list}----{type(odenisli_icaze_date_list)}")
    print(f"odenissiz_icaze_date_list==>{odenissiz_icaze_date_list}----{type(odenissiz_icaze_date_list)}")
    qeyri_is_gunu_count = float(len(date_list)) + float(len(odenisli_icaze_date_list)) + float(len(odenissiz_icaze_date_list))
    print(f"qeyri_is_gunu_count==>{qeyri_is_gunu_count}----{type(qeyri_is_gunu_count)}")

    is_gunleri_count = serializer.validated_data.get("is_gunleri_count")
    is_gunleri_count = float(is_gunleri_count) - abs((float(k_qeyri_is_gunleri) - float(qeyri_is_gunu_count)))
    serializer.save(tetil_gunleri=date_list, is_gunleri_count=is_gunleri_count, qeyri_is_gunu_count=qeyri_is_gunu_count)
    return True


# --------------------------------------------------------------------------------------------------------------------------

def holding_istisna_isci_gunler_update(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    
    print(f"holding_gunler==>{holding_gunler}")
    if serializer.is_valid():
        holding_gunler = serializer.validated_data.get("holding_gunler")

        instisna_isci_create(serializer=serializer, company="holding", company_name=holding_gunler.holding, obj_gunler=holding_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def holding_istisna_isci_gunler_patch(self, request, *args, **kwargs):
    holding_gunler = self.get_object()
    serializer = HoldingGunlerSerializer(holding_gunler, data=request.data)
    
    print(f"holding_gunler==>{holding_gunler}")
    if serializer.is_valid():
        holding_gunler = serializer.validated_data.get("holding_gunler")
        instisna_isci_create(serializer=serializer, company="holding", company_name=holding_gunler.holding, obj_gunler=holding_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------------------------------------------------------

def ofis_gunler_update(self, request, *args, **kwargs):
    ofis_gunler = self.get_object()
    serializer = OfisGunlerSerializer(ofis_gunler, data=request.data)
    print(f"ofis_gunler==>{ofis_gunler}")
    if serializer.is_valid():
        ofis_gunler = serializer.validated_data.get("ofis_gunler")

        instisna_isci_create(serializer=serializer, company="ofis", company_name=ofis_gunler.holding, obj_gunler=ofis_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def ofis_gunler_patch(self, request, *args, **kwargs):
    ofis_gunler = self.get_object()
    serializer = OfisGunlerSerializer(ofis_gunler, data=request.data)
    print(f"ofis_gunler==>{ofis_gunler}")
    if serializer.is_valid():
        ofis_gunler = serializer.validated_data.get("ofis_gunler")

        instisna_isci_create(serializer=serializer, company="ofis", company_name=ofis_gunler.holding, obj_gunler=ofis_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------------------------------------------------------

def shirket_gunler_update(self, request, *args, **kwargs):
    shirket_gunler = self.get_object()
    serializer = ShirketGunlerSerializer(shirket_gunler, data=request.data)
    print(f"shirket_gunler==>{shirket_gunler}")
    if serializer.is_valid():
        ofis_gunler = serializer.validated_data.get("ofis_gunler")

        instisna_isci_create(serializer=serializer, company="ofis", company_name=ofis_gunler.holding, obj_gunler=ofis_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def shirket_gunler_patch(self, request, *args, **kwargs):
    shirket_gunler = self.get_object()
    serializer = ShirketGunlerSerializer(shirket_gunler, data=request.data)
    print(f"shirket_gunler==>{shirket_gunler}")
    if serializer.is_valid():
        tetil_gunleri_calc(shirket_gunler, serializer, "shirket", shirket_gunler.shirket, shirket_gunler.tarix)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------------------------------------------------------

def shobe_gunler_update(self, request, *args, **kwargs):
    shobe_gunler = self.get_object()
    serializer = ShobeGunlerSerializer(shobe_gunler, data=request.data)
    print(f"shobe_gunler==>{shobe_gunler}")
    if serializer.is_valid():
        tetil_gunleri_calc(shobe_gunler, serializer, "shobe", shobe_gunler.shobe, shobe_gunler.tarix)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def shobe_gunler_patch(self, request, *args, **kwargs):
    shobe_gunler = self.get_object()
    serializer = ShobeGunlerSerializer(shobe_gunler, data=request.data)
    print(f"shobe_gunler==>{shobe_gunler}")
    if serializer.is_valid():
        tetil_gunleri_calc(shobe_gunler, serializer, "shobe", shobe_gunler.shobe, shobe_gunler.tarix)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------------------------------------------------------

def komanda_gunler_update(self, request, *args, **kwargs):
    komanda_gunler = self.get_object()
    serializer = KomandaGunlerSerializer(komanda_gunler, data=request.data)
    print(f"komanda_gunler==>{komanda_gunler}")
    if serializer.is_valid():
        tetil_gunleri_calc(komanda_gunler, serializer, "komanda", komanda_gunler.komanda, komanda_gunler.tarix)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def komanda_gunler_patch(self, request, *args, **kwargs):
    komanda_gunler = self.get_object()
    serializer = KomandaGunlerSerializer(komanda_gunler, data=request.data)
    print(f"komanda_gunler==>{komanda_gunler}")
    if serializer.is_valid():
        tetil_gunleri_calc(komanda_gunler, serializer, "komanda", komanda_gunler.komanda, komanda_gunler.tarix)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------------------------------------------------------

def vezife_gunler_update(self, request, *args, **kwargs):
    vezife_gunler = self.get_object()
    serializer = VezifeGunlerSerializer(vezife_gunler, data=request.data)
    print(f"vezife_gunler==>{vezife_gunler}")
    if serializer.is_valid():
        tetil_gunleri_calc(vezife_gunler, serializer, "vezife", vezife_gunler.vezife, vezife_gunler.tarix)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def vezife_gunler_patch(self, request, *args, **kwargs):
    vezife_gunler = self.get_object()
    serializer = VezifeGunlerSerializer(vezife_gunler, data=request.data)
    print(f"vezife_gunler==>{vezife_gunler}")
    if serializer.is_valid():
        tetil_gunleri_calc(vezife_gunler, serializer, "vezife", vezife_gunler.vezife, vezife_gunler.tarix)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------------------------------------------------------

def user_gunler_update(self, request, *args, **kwargs):
    user_gunler = self.get_object()
    serializer = IsciGunlerSerializer(user_gunler, data=request.data)
    print(f"user_gunler==>{user_gunler}")
    if serializer.is_valid():
        isci_tetil_gunleri_calc(serializer, user_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def user_gunler_patch(self, request, *args, **kwargs):
    user_gunler = self.get_object()
    serializer = IsciGunlerSerializer(user_gunler, data=request.data)
    print(f"user_gunler==>{user_gunler}")
    if serializer.is_valid():
        isci_tetil_gunleri_calc(serializer, user_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------------------------------------------------------

def holding_istisna_isci_update(self, request, *args, **kwargs):
    holding_istisna_isci = self.get_object()
    serializer = HoldingIstisnaIsciSerializer(holding_istisna_isci, data=request.data)
    print(f"holding_istisna_isci==>{holding_istisna_isci}")
    if serializer.is_valid():
        
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def holding_istisna_isci_patch(self, request, *args, **kwargs):
    holding_istisna_isci = self.get_object()
    serializer = HoldingIstisnaIsciSerializer(holding_istisna_isci, data=request.data)
    print(f"holding_istisna_isci==>{holding_istisna_isci}")
    if serializer.is_valid():
        
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

