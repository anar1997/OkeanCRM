import datetime
from django.shortcuts import get_object_or_404
import pandas as pd
from rest_framework import status
from rest_framework.response import Response
from account.models import User
from api.v1.all_serializers.gunler_serializers import (
    HoldingIstisnaIsciSerializer,
    IsciGunlerSerializer,
    HoldingGunlerSerializer,
    KomandaGunlerSerializer,
    KomandaIstisnaIsciSerializer, 
    OfisGunlerSerializer,
    OfisIstisnaIsciSerializer,
    ShirketGunlerSerializer,
    ShirketIstisnaIsciSerializer,
    ShobeGunlerSerializer,
    ShobeIstisnaIsciSerializer,
    VezifeGunlerSerializer,
    VezifeIstisnaIsciSerializer
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

def company_isci_tetil_hesablama(company, company_name, tarix, tetil_gunleri, is_gunleri_count, qeyri_is_gunu_count, istisna_isciler=list()):
    """
    Bu method holding, shirket, ofis, shobe, komanda ve vezife-nin is ve qeyri is gunleri hesablanan zaman onlarla elaqeli olan
    iscilerin is ve qeyri is gunlerini hesablamaq ucundur. Hemcinin eger holding-in is ve qeyri is gunleri hesablanirsa bu zaman yuxarida
    sadaladigim digeer obyektlerinde is ve qeyri is gunleri uygun olaraq deyisir.
    """
    if(company=="holding"):
        isciler = list(User.objects.all())
        ofis_gunler = OfisGunler.objects.filter(tarix=tarix)
        for o in ofis_gunler:
            o.is_gunleri_count = is_gunleri_count
            o.qeyri_is_gunu_count = qeyri_is_gunu_count
            o.tetil_gunleri = tetil_gunleri
            o.save()
        shirket_gunler = ShirketGunler.objects.filter(tarix=tarix)
        for s in shirket_gunler:
            s.is_gunleri_count = is_gunleri_count
            s.qeyri_is_gunu_count = qeyri_is_gunu_count
            s.tetil_gunleri = tetil_gunleri
            s.save()
        shobe_gunler = ShobeGunler.objects.filter(tarix=tarix)
        for sh in shobe_gunler:
            sh.is_gunleri_count = is_gunleri_count
            sh.qeyri_is_gunu_count = qeyri_is_gunu_count
            sh.tetil_gunleri = tetil_gunleri
            sh.save()
        vezife_gunler = VezifeGunler.objects.filter(tarix=tarix)
        for v in vezife_gunler:
            v.is_gunleri_count = is_gunleri_count
            v.qeyri_is_gunu_count = qeyri_is_gunu_count
            v.tetil_gunleri = tetil_gunleri
            v.save()
        komanda_gunler = KomandaGunler.objects.filter(tarix=tarix)
        for k in komanda_gunler:
            k.is_gunleri_count = is_gunleri_count
            k.qeyri_is_gunu_count = qeyri_is_gunu_count
            k.tetil_gunleri = tetil_gunleri
            k.save()
    elif(company=="shirket"):
        isciler = list(User.objects.filter(shirket=company_name))
    elif(company=="shobe"):
        isciler = list(User.objects.filter(shobe=company_name))
    elif(company=="ofis"):
        isciler = list(User.objects.filter(ofis=company_name))
    elif(company=="komanda"):
        isciler = list(User.objects.filter(komanda=company_name))
    elif(company=="vezife"):
        isciler = list(User.objects.filter(vezife=company_name))

    print(f"company ==> {company}")
    print(f"company_name ==> {company_name}")
    print(f"isciler ==> {isciler}")
    print(f"tarix ==> {tarix}")

    for isci in isciler:
        print(f"{isci=}")
        print(f"{istisna_isciler=}")
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

    obj_gunler_tetil_gunleri = obj_gunler.tetil_gunleri
    print(f"{obj_gunler_tetil_gunleri=}")

    date_list = []
    k_date_list = []
    
    tetil_gunleri = serializer.validated_data.get("tetil_gunleri")
    print(f"tetil_gunleri==>{tetil_gunleri}----{type(tetil_gunleri)}")
    tetil_gunleri_l = tetil_gunleri.rstrip("]").lstrip("[").split(",")
    print(f"tetil_gunleri_l==>{tetil_gunleri_l}----{type(tetil_gunleri_l)} -- {len(tetil_gunleri_l)}")
    for i in tetil_gunleri_l:
        new_el = i.strip().strip("'").strip('"')
        date_list.append(new_el)
    print(f"date_list==>{date_list}----{type(date_list)}")

    istisna_isciler = serializer.validated_data.get("istisna_isciler")
    print(f"istisna_isciler==>{istisna_isciler}----{type(istisna_isciler)} -- {len(istisna_isciler)}")

    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    for isci in istisna_isciler:
        isci_gunler = IsciGunler.objects.get(isci=isci, tarix=tarix)
        print(f"{isci_gunler=} --- {type(isci_gunler)=}")
        print(f"{isci_gunler.tetil_gunleri} -- {type(isci_gunler.tetil_gunleri)=}")
        if isci_gunler.tetil_gunleri is not None:
            isci_gunler_tetil_gunleri = obj_gunler_tetil_gunleri.rstrip("]").lstrip("[").split(",")
            print(f"{isci_gunler_tetil_gunleri=}----{type(isci_gunler_tetil_gunleri)=} -- {len(isci_gunler_tetil_gunleri)=}")
            for i in isci_gunler_tetil_gunleri:
                new_el = i.strip().strip("'").strip('"')
                k_date_list.append(new_el)
            print(f"{k_date_list=}----{type(k_date_list)=}")

            for i in date_list:
                print(f"{i=}")
                if i in k_date_list:
                    print(f"silinen i - {i}")
                    k_date_list.remove(i)
        isci_gunler.tetil_gunleri = k_date_list
        isci_gunler.is_gunleri_count = float(days_in_mont) - len(date_list)
        isci_gunler.qeyri_is_gunu_count = len(date_list)
        isci_gunler.save()

    serializer.save(tetil_gunleri=date_list, istisna_isciler=istisna_isciler)

def istisna_isci_update(serializer, company, company_name, obj_gunler, obj_istisna_isci):
    print(f"obj_gunler==>{obj_gunler}----{type(obj_gunler)}")

    tarix = obj_gunler.tarix
    print(f"tarix==>{tarix}----{type(tarix)}")

    obj_gunler_tetil_gunleri = obj_gunler.tetil_gunleri
    print(f"{obj_gunler_tetil_gunleri=}")

    date_list = []
    k_date_list = []
    q_date_list = []

    k_tetil_gunleri = obj_istisna_isci.tetil_gunleri
    print(f"{k_tetil_gunleri=} -- {type(k_tetil_gunleri)}")
    k_tetil_gunleri_l = k_tetil_gunleri.rstrip("]").lstrip("[").split(",")
    print(f"{k_tetil_gunleri_l=}----{type(k_tetil_gunleri_l)=} -- {len(k_tetil_gunleri_l)=}")
    for i in k_tetil_gunleri_l:
        new_el = i.strip().strip("'").strip('"')
        k_date_list.append(new_el)
    print(f"{k_date_list=}----{type(k_date_list)=}")

    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    tetil_gunleri = serializer.validated_data.get("tetil_gunleri")
    if tetil_gunleri == None:
        tetil_gunleri = k_date_list
        tetil_gunleri_l = tetil_gunleri
        date_list = k_date_list
    else:
        print(f"tetil_gunleri==>{tetil_gunleri}----{type(tetil_gunleri)}")
        tetil_gunleri_l = tetil_gunleri.rstrip("]").lstrip("[").split(",")
        print(f"tetil_gunleri_l==>{tetil_gunleri_l}----{type(tetil_gunleri_l)} -- {len(tetil_gunleri_l)}")
        for i in tetil_gunleri_l:
            new_el = i.strip().strip("'").strip('"')
            date_list.append(new_el)

    print(f"date_list==>{date_list}----{type(date_list)}")

    u_istisna_isciler = []

    istisna_isciler = serializer.validated_data.get("istisna_isciler")
    if istisna_isciler == None:
        istisna_isciler = list(obj_istisna_isci.istisna_isciler.all())
    
    print(f"istisna_isciler==>{istisna_isciler}----{type(istisna_isciler)} -- {len(istisna_isciler)}")

    k_istisna_isciler = list(obj_istisna_isci.istisna_isciler.all())
    print(f"{k_istisna_isciler=} -- {type(k_istisna_isciler)} -- {len(k_istisna_isciler)}")

    for i in k_istisna_isciler:
        print(f"{i=}")
        u_istisna_isciler.append(i)

    for j in istisna_isciler:
        if j in u_istisna_isciler:
            continue
        else:
            u_istisna_isciler.append(j)
    
    print(f"{u_istisna_isciler=}----{type(u_istisna_isciler)=} -- {len(u_istisna_isciler)=}")

    if (
        (serializer.validated_data.get("istisna_isciler") == None or serializer.validated_data.get("istisna_isciler") == "") 
        and 
        (serializer.validated_data.get("tetil_gunleri") != None)
    ):
        for isci in u_istisna_isciler:
            isci_gunler = IsciGunler.objects.get(isci=isci, tarix=tarix)
            print(f"{isci_gunler=} --- {type(isci_gunler)=}")
            if isci_gunler.tetil_gunleri is not None:
                isci_gunler_tetil_gunleri = obj_gunler_tetil_gunleri.rstrip("]").lstrip("[").split(",")
                print(f"{isci_gunler_tetil_gunleri=}----{type(isci_gunler_tetil_gunleri)=} -- {len(isci_gunler_tetil_gunleri)=}")
                for i in isci_gunler_tetil_gunleri:
                    new_el = i.strip().strip("'").strip('"')
                    q_date_list.append(new_el)
                print(f"{q_date_list=}----{type(q_date_list)=}")

                if len(date_list) == len(q_date_list):
                    isci_gunler.tetil_gunleri = list(q_date_list)
                    isci_gunler.is_gunleri_count = float(days_in_mont)
                    isci_gunler.qeyri_is_gunu_count = 0
                    isci_gunler.save()
                else:
                    for i in date_list:
                        print(f"{i=}")
                        if i in q_date_list:
                            print(f"silinen i - {i}")
                            q_date_list.remove(i)
                        isci_gunler.tetil_gunleri = list(q_date_list)
                        isci_gunler.is_gunleri_count = float(days_in_mont) - len(date_list)
                        isci_gunler.qeyri_is_gunu_count = len(date_list)
                        isci_gunler.save()
    elif(
        (serializer.validated_data.get("istisna_isciler") != None) 
        and 
        (serializer.validated_data.get("tetil_gunleri") == None)
    ):
        for isci in istisna_isciler:
            isci_gunler = IsciGunler.objects.get(isci=isci, tarix=tarix)
            print(f"{isci_gunler=} --- {type(isci_gunler)=}")
            print(f"{isci_gunler.tetil_gunleri} -- {type(isci_gunler.tetil_gunleri)=}")
            if isci_gunler.tetil_gunleri is not None:
                isci_gunler_tetil_gunleri = obj_gunler_tetil_gunleri.rstrip("]").lstrip("[").split(",")
                print(f"{isci_gunler_tetil_gunleri=}----{type(isci_gunler_tetil_gunleri)=} -- {len(isci_gunler_tetil_gunleri)=}")
                for i in isci_gunler_tetil_gunleri:
                    new_el = i.strip().strip("'").strip('"')
                    q_date_list.append(new_el)
                print(f"{q_date_list=}----{type(q_date_list)=}")

                for i in date_list:
                    print(f"{i=}")
                    if i in q_date_list:
                        print(f"silinen i - {i}")
                        q_date_list.remove(i)
            isci_gunler.tetil_gunleri = list(q_date_list)
            isci_gunler.is_gunleri_count = float(days_in_mont) - len(date_list)
            isci_gunler.qeyri_is_gunu_count = len(date_list)
            isci_gunler.save()
    elif(
        (serializer.validated_data.get("istisna_isciler") != None) 
        and 
        (serializer.validated_data.get("tetil_gunleri") != None)
    ):
        for isci in u_istisna_isciler:
            isci_gunler = IsciGunler.objects.get(isci=isci, tarix=tarix)
            print(f"{isci_gunler=} --- {type(isci_gunler)=}")
            if isci_gunler.tetil_gunleri is not None:
                isci_gunler_tetil_gunleri = obj_gunler_tetil_gunleri.rstrip("]").lstrip("[").split(",")
                print(f"{isci_gunler_tetil_gunleri=}----{type(isci_gunler_tetil_gunleri)=} -- {len(isci_gunler_tetil_gunleri)=}")
                for i in isci_gunler_tetil_gunleri:
                    new_el = i.strip().strip("'").strip('"')
                    q_date_list.append(new_el)
                print(f"{q_date_list=}----{type(q_date_list)=}")

                if len(date_list) == len(q_date_list):
                    isci_gunler.tetil_gunleri = list(q_date_list)
                    isci_gunler.is_gunleri_count = float(days_in_mont)
                    isci_gunler.qeyri_is_gunu_count = 0
                    isci_gunler.save()
                else:
                    for i in date_list:
                        print(f"{i=}")
                        if i in q_date_list:
                            print(f"silinen i - {i}")
                            q_date_list.remove(i)
                        isci_gunler.tetil_gunleri = list(q_date_list)
                        isci_gunler.is_gunleri_count = float(days_in_mont) - len(date_list)
                        isci_gunler.qeyri_is_gunu_count = len(date_list)
                        isci_gunler.save()

    # serializer.save(tetil_gunleri=date_list, istisna_isciler=u_istisna_isciler)
    serializer.save()

def istisna_isci_delete(obj_gunler, obj_istisna_isci):
    istisna_isciler = obj_istisna_isci.istisna_isciler.all()
    print(f"{istisna_isciler=}")

    tarix = obj_gunler.tarix
    print(f"tarix==>{tarix}----{type(tarix)}")

    indi = datetime.date.today()
    print(f"indi ==> {indi}")

    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
    print(f"days_in_mont ==> {days_in_mont}")

    for isci in istisna_isciler:
        isci_gunler = IsciGunler.objects.get(isci=isci, tarix=tarix)
        print(f"{isci_gunler=} --- {type(isci_gunler)=}")
        if isci_gunler.tetil_gunleri is not None: 
            isci_gunler.tetil_gunleri = None
            isci_gunler.is_gunleri_count = float(days_in_mont)
            isci_gunler.qeyri_is_gunu_count = 0
            isci_gunler.save()


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

def gunler_update(serializer, company, company_name, obj_gunler):
    print(f"obj_gunler==>{obj_gunler}----{type(obj_gunler)}")

    tarix = obj_gunler.tarix
    print(f"tarix==>{tarix}----{type(tarix)}")
    
    # holding = obj_gunler.company
    # print(f"{holding=}")

    is_gunleri_count = obj_gunler.is_gunleri_count
    print(f"{is_gunleri_count=}")

    qeyri_is_gunu_count = obj_gunler.qeyri_is_gunu_count
    print(f"{qeyri_is_gunu_count=}")

    date_list = []
    k_date_list = []
    u_date_list = []

    k_tetil_gunleri = obj_gunler.tetil_gunleri
    if k_tetil_gunleri is not None:
        print(f"{k_tetil_gunleri=} -- {type(k_tetil_gunleri)}")
        k_tetil_gunleri_l = k_tetil_gunleri.rstrip("]").lstrip("[").split(",")
        print(f"{k_tetil_gunleri_l=}----{type(k_tetil_gunleri_l)=} -- {len(k_tetil_gunleri_l)=}")
        for i in k_tetil_gunleri_l:
            new_el = i.strip().strip("'").strip('"')
            k_date_list.append(new_el)
    else:
        k_date_list = []
    print(f"{k_date_list=}----{type(k_date_list)=}")

    tetil_gunleri = serializer.validated_data.get("tetil_gunleri")
    if tetil_gunleri == None:
        tetil_gunleri = k_date_list
        tetil_gunleri_l = tetil_gunleri
    else:
        print(f"tetil_gunleri==>{tetil_gunleri}----{type(tetil_gunleri)}")
        tetil_gunleri_l = tetil_gunleri.rstrip("]").lstrip("[").split(",")
        print(f"tetil_gunleri_l==>{tetil_gunleri_l}----{type(tetil_gunleri_l)} -- {len(tetil_gunleri_l)}")
        for i in tetil_gunleri_l:
            new_el = i.strip().strip("'").strip('"')
            date_list.append(new_el)
        print(f"date_list==>{date_list}----{type(date_list)}")

    for i in date_list:
        u_date_list.append(i)

    for j in k_date_list:
        if j in u_date_list:
            continue
        else:
            u_date_list.append(j)

    print(f"{u_date_list=}----{type(u_date_list)=}")

    k_qeyri_is_gunleri = obj_gunler.qeyri_is_gunu_count
    print(f"k_qeyri_is_gunleri==>{k_qeyri_is_gunleri}----{type(k_qeyri_is_gunleri)}")

    qeyri_is_gunu_count = len(date_list)
    print(f"qeyri_is_gunu_count==>{qeyri_is_gunu_count}----{type(qeyri_is_gunu_count)}")

    k_is_gunleri_count = obj_gunler.is_gunleri_count
    is_gunleri_count = float(k_is_gunleri_count) - abs((float(k_qeyri_is_gunleri) - float(qeyri_is_gunu_count)))

    print(f"is_gunleri_count==>{is_gunleri_count}----{type(is_gunleri_count)}")
    
    company_isci_tetil_hesablama(
        company=company, 
        company_name=company_name, 
        tarix=tarix, 
        tetil_gunleri=u_date_list, 
        is_gunleri_count=is_gunleri_count, 
        qeyri_is_gunu_count=qeyri_is_gunu_count
    )

    serializer.save(
        qeyri_is_gunu_count = qeyri_is_gunu_count, 
        is_gunleri_count = is_gunleri_count,
        tetil_gunleri=u_date_list
    )

# --------------------------------------------------------------------------------------------------------------------------

def holding_gunler_update(self, request, *args, **kwargs):
    holding_gunler = self.get_object()
    serializer = HoldingGunlerSerializer(holding_gunler, data=request.data, partial=True)
    print(f"{holding_gunler=}")

    if serializer.is_valid():
        gunler_update(serializer=serializer, company="holding", company_name=holding_gunler.holding, obj_gunler=holding_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)


def holding_istisna_isci_gunler_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    
    if serializer.is_valid():
        holding_gunler = serializer.validated_data.get("holding_gunler")

        print(f"holding_gunler==>{holding_gunler}")
        
        instisna_isci_create(serializer=serializer, company="holding", company_name=holding_gunler.holding, obj_gunler=holding_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def holding_istisna_isci_gunler_update(self, request, *args, **kwargs):
    holding_istisna_isci_obj = self.get_object()
    print(f"{holding_istisna_isci_obj=}")
    serializer = HoldingIstisnaIsciSerializer(holding_istisna_isci_obj, data=request.data, partial=True)
    
    if serializer.is_valid():
        
        istisna_isci_update(serializer=serializer, company="holding", company_name=holding_istisna_isci_obj.holding_gunler.holding, obj_gunler=holding_istisna_isci_obj.holding_gunler, obj_istisna_isci=holding_istisna_isci_obj)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def holding_istisna_isci_gunler_delete(self, request, *args, **kwargs):
    holding_istisna_isci_obj = self.get_object()
    print(f"{holding_istisna_isci_obj=}")
    try:
        istisna_isci_delete(
            obj_gunler=holding_istisna_isci_obj.holding_gunler, 
            obj_istisna_isci=holding_istisna_isci_obj
        )
        holding_istisna_isci_obj.delete()
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    except:
        return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------------------------------------------------------

def ofis_gunler_update(self, request, *args, **kwargs):
    ofis_gunler = self.get_object()
    serializer = OfisGunlerSerializer(ofis_gunler, data=request.data, partial=True)
    print(f"{ofis_gunler=}")

    if serializer.is_valid():
        gunler_update(serializer=serializer, company="ofis", company_name=ofis_gunler.ofis, obj_gunler=ofis_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def ofis_istisna_isci_gunler_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    
    if serializer.is_valid():
        ofis_gunler = serializer.validated_data.get("ofis_gunler")

        print(f"ofis_gunler==>{ofis_gunler}")
        
        instisna_isci_create(serializer=serializer, company="ofis", company_name=ofis_gunler.ofis, obj_gunler=ofis_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def ofis_istisna_isci_gunler_update(self, request, *args, **kwargs):
    ofis_istisna_isci_obj = self.get_object()
    print(f"{ofis_istisna_isci_obj=}")
    serializer = OfisIstisnaIsciSerializer(ofis_istisna_isci_obj, data=request.data, partial=True)
    
    if serializer.is_valid():
        istisna_isci_update(serializer=serializer, company="ofis", company_name=ofis_istisna_isci_obj.ofis_gunler.ofis, obj_gunler=ofis_istisna_isci_obj.ofis_gunler, obj_istisna_isci=ofis_istisna_isci_obj)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def ofis_istisna_isci_gunler_delete(self, request, *args, **kwargs):
    ofis_istisna_isci_obj = self.get_object()
    print(f"{ofis_istisna_isci_obj=}")
    try:
        istisna_isci_delete(
            obj_gunler=ofis_istisna_isci_obj.holding_gunler, 
            obj_istisna_isci=ofis_istisna_isci_obj
        )
        ofis_istisna_isci_obj.delete()
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    except:
        return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------------------------------------------------------

def shirket_gunler_update(self, request, *args, **kwargs):
    shirket_gunler = self.get_object()
    serializer = ShirketGunlerSerializer(shirket_gunler, data=request.data, partial=True)
    print(f"{shirket_gunler=}")

    if serializer.is_valid():
        gunler_update(serializer=serializer, company="shirket", company_name=shirket_gunler.shirket, obj_gunler=shirket_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def shirket_istisna_isci_gunler_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    
    if serializer.is_valid():
        shirket_gunler = serializer.validated_data.get("shirket_gunler")

        print(f"shirket_gunler==>{shirket_gunler}")
        
        instisna_isci_create(serializer=serializer, company="shirket", company_name=shirket_gunler.shirket, obj_gunler=shirket_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def shirket_istisna_isci_gunler_update(self, request, *args, **kwargs):
    shirket_istisna_isci_obj = self.get_object()
    print(f"{shirket_istisna_isci_obj=}")
    serializer = ShirketIstisnaIsciSerializer(shirket_istisna_isci_obj, data=request.data, partial=True)
    
    if serializer.is_valid():
        istisna_isci_update(serializer=serializer, company="shirket", company_name=shirket_istisna_isci_obj.shirket_gunler.shirket, obj_gunler=shirket_istisna_isci_obj.shirket_gunler, obj_istisna_isci=shirket_istisna_isci_obj)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def shirket_istisna_isci_gunler_delete(self, request, *args, **kwargs):
    shirket_istisna_isci_obj = self.get_object()
    print(f"{shirket_istisna_isci_obj=}")
    try:
        istisna_isci_delete(
            obj_gunler=shirket_istisna_isci_obj.holding_gunler, 
            obj_istisna_isci=shirket_istisna_isci_obj
        )
        shirket_istisna_isci_obj.delete()
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    except:
        return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------------------------------------------------------

def shobe_gunler_update(self, request, *args, **kwargs):
    shobe_gunler = self.get_object()
    serializer = ShobeGunlerSerializer(shobe_gunler, data=request.data, partial=True)
    print(f"{shobe_gunler=}")

    if serializer.is_valid():
        gunler_update(serializer=serializer, company="shobe", company_name=shobe_gunler.shobe, obj_gunler=shobe_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def shobe_istisna_isci_gunler_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    
    if serializer.is_valid():
        shobe_gunler = serializer.validated_data.get("shobe_gunler")

        print(f"shobe_gunler==>{shobe_gunler}")
        
        instisna_isci_create(serializer=serializer, company="shobe", company_name=shobe_gunler.shobe, obj_gunler=shobe_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def shobe_istisna_isci_gunler_update(self, request, *args, **kwargs):
    shobe_istisna_isci_obj = self.get_object()
    print(f"{shobe_istisna_isci_obj=}")
    serializer = ShobeIstisnaIsciSerializer(shobe_istisna_isci_obj, data=request.data, partial=True)
    
    if serializer.is_valid():
        istisna_isci_update(serializer=serializer, company="shobe", company_name=shobe_istisna_isci_obj.shobe_gunler.shobe, obj_gunler=shobe_istisna_isci_obj.shobe_gunler, obj_istisna_isci=shobe_istisna_isci_obj)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def shobe_istisna_isci_gunler_delete(self, request, *args, **kwargs):
    shobe_istisna_isci_obj = self.get_object()
    print(f"{shobe_istisna_isci_obj=}")
    try:
        istisna_isci_delete(
            obj_gunler=shobe_istisna_isci_obj.holding_gunler, 
            obj_istisna_isci=shobe_istisna_isci_obj
        )
        shobe_istisna_isci_obj.delete()
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    except:
        return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)
# ------------------------------------------------------------------------------------------------

def komanda_gunler_update(self, request, *args, **kwargs):
    komanda_gunler = self.get_object()
    serializer = KomandaGunlerSerializer(komanda_gunler, data=request.data, partial=True)
    print(f"{komanda_gunler=}")

    if serializer.is_valid():
        gunler_update(serializer=serializer, company="komanda", company_name=komanda_gunler.komanda, obj_gunler=komanda_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def komanda_istisna_isci_gunler_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    
    if serializer.is_valid():
        komanda_gunler = serializer.validated_data.get("komanda_gunler")

        print(f"komanda_gunler==>{komanda_gunler}")
        
        instisna_isci_create(serializer=serializer, company="komanda", company_name=komanda_gunler.komanda, obj_gunler=komanda_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def komanda_istisna_isci_gunler_update(self, request, *args, **kwargs):
    komanda_istisna_isci_obj = self.get_object()
    print(f"{komanda_istisna_isci_obj=}")
    serializer = KomandaIstisnaIsciSerializer(komanda_istisna_isci_obj, data=request.data, partial=True)
    
    if serializer.is_valid():
        istisna_isci_update(serializer=serializer, company="komanda", company_name=komanda_istisna_isci_obj.komanda_gunler.komanda, obj_gunler=komanda_istisna_isci_obj.komanda_gunler, obj_istisna_isci=komanda_istisna_isci_obj)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def komanda_istisna_isci_gunler_delete(self, request, *args, **kwargs):
    komanda_istisna_isci_obj = self.get_object()
    print(f"{komanda_istisna_isci_obj=}")
    try:
        istisna_isci_delete(
            obj_gunler=komanda_istisna_isci_obj.holding_gunler, 
            obj_istisna_isci=komanda_istisna_isci_obj
        )
        komanda_istisna_isci_obj.delete()
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    except:
        return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------------------------------------------------------------------------

def vezife_gunler_update(self, request, *args, **kwargs):
    vezife_gunler = self.get_object()
    serializer = VezifeGunlerSerializer(vezife_gunler, data=request.data, partial=True)
    print(f"{vezife_gunler=}")

    if serializer.is_valid():
        gunler_update(serializer=serializer, company="vezife", company_name=vezife_gunler.vezife, obj_gunler=vezife_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def vezife_istisna_isci_gunler_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    
    if serializer.is_valid():
        vezife_gunler = serializer.validated_data.get("vezife_gunler")

        print(f"vezife_gunler==>{vezife_gunler}")
        
        instisna_isci_create(serializer=serializer, company="vezife", company_name=vezife_gunler.vezife, obj_gunler=vezife_gunler)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)

def vezife_istisna_isci_gunler_update(self, request, *args, **kwargs):
    vezife_istisna_isci_obj = self.get_object()
    print(f"{vezife_istisna_isci_obj=}")
    serializer = VezifeIstisnaIsciSerializer(vezife_istisna_isci_obj, data=request.data, partial=True)
    
    if serializer.is_valid():
        istisna_isci_update(serializer=serializer, company="vezife", company_name=vezife_istisna_isci_obj.vezife_gunler.vezife, obj_gunler=vezife_istisna_isci_obj.vezife_gunler, obj_istisna_isci=vezife_istisna_isci_obj)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    return Response({"detail": "Xəta!"}, status=status.HTTP_400_BAD_REQUEST)
    
def vezife_istisna_isci_gunler_delete(self, request, *args, **kwargs):
    vezife_istisna_isci_obj = self.get_object()
    print(f"{vezife_istisna_isci_obj=}")
    try:
        istisna_isci_delete(
            obj_gunler=vezife_istisna_isci_obj.holding_gunler, 
            obj_istisna_isci=vezife_istisna_isci_obj
        )
        vezife_istisna_isci_obj.delete()
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    except:
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


