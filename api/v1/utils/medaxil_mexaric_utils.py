from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from company.models import Holding, HoldingKassa, Ofis, OfisKassa, Shirket, ShirketKassa


# *************** Holding Kassa medaxil mexaric ***************
def holding_kassa_medaxil_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    mebleg = request.data.get("mebleg")
    print(f"mebleg ==> {mebleg}")

    if(mebleg != ""):
        holding = get_object_or_404(Holding, holding_adi="Alliance")
        print(f"holding ==> {holding}")
        holding_kassa = get_object_or_404(HoldingKassa, holding=holding)
        print(f"holding_kassa ==> {holding_kassa}")

        medaxil_tarixi = request.data.get("medaxil_tarixi")
        print(f"medaxil_tarixi ==> {medaxil_tarixi}")

        if(medaxil_tarixi == ""):
            medaxil_tarixi = datetime.today().strftime('%Y-%m-%d')

        qeyd = request.data.get("qeyd")
        print(f"qeyd ==> {qeyd}")

        holding_kassa_balans = holding_kassa.balans
        print(f"holding_kassa_balans ==> {holding_kassa_balans}")

        yekun_balans = float(mebleg) + float(holding_kassa_balans)

        if(serializer.is_valid()):
            holding_kassa.balans = yekun_balans
            holding_kassa.save()
            serializer.save(holding_kassa=holding_kassa, medaxil_tarixi=medaxil_tarixi)
            return Response({"detail": f"{holding} holdinqinə {mebleg} azn mədaxil edildi"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"detail": "Məbləği daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

def holding_kassa_mexaric_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    mebleg = request.data.get("mebleg")
    print(f"mebleg ==> {mebleg}")

    qeyd = request.data.get("qeyd")
    print(f"qeyd ==> {qeyd}")

    holding = get_object_or_404(Holding, holding_adi="Alliance")
    print(f"holding ==> {holding}")
    holding_kassa = get_object_or_404(HoldingKassa, holding=holding)
    print(f"holding_kassa ==> {holding_kassa}")

    holding_kassa_balans = holding_kassa.balans
    print(f"holding_kassa_balans ==> {holding_kassa_balans}")

    mexaric_tarixi = request.data.get("mexaric_tarixi")
    print(f"mexaric_tarixi ==> {mexaric_tarixi}")

    if(mexaric_tarixi == ""):
        mexaric_tarixi = datetime.today().strftime('%Y-%m-%d')

    if(holding_kassa_balans != 0):
        if(mebleg != ""):
            if(float(mebleg) <= float(holding_kassa_balans)):
                yekun_balans = float(holding_kassa_balans) - float(mebleg)
                if(serializer.is_valid()):
                    holding_kassa.balans = yekun_balans
                    holding_kassa.save()
                    serializer.save(holding_kassa=holding_kassa, mexaric_tarixi=mexaric_tarixi)
                    return Response({"detail": f"{holding} holdinqindən {mebleg} azn məxaric edildi"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"detail": "Daxil etdiyiniz məbləğ holdinqin balansıdan böyük ola bilməz"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Məbləği doğru daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Holdinqin balansı 0-dır"}, status=status.HTTP_400_BAD_REQUEST)

# *************** Shirket Kassa medaxil mexaric ***************

def shirket_kassa_medaxil_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    mebleg = request.data.get("mebleg")
    print(f"mebleg ==> {mebleg}")
    
    if(mebleg != ""):
        shirket_kassa_id = request.data.get("shirket_kassa_id")
        print(f"shirket_kassa_id ==> {shirket_kassa_id}")
        shirket_kassa = get_object_or_404(ShirketKassa, pk=shirket_kassa_id)
        print(f"shirket_kassa ==> {shirket_kassa}")

        medaxil_tarixi = request.data.get("medaxil_tarixi")
        print(f"medaxil_tarixi ==> {medaxil_tarixi}")

        if(medaxil_tarixi == ""):
            medaxil_tarixi = datetime.today().strftime('%Y-%m-%d')

        qeyd = request.data.get("qeyd")
        print(f"qeyd ==> {qeyd}")

        shirket_kassa_balans = shirket_kassa.balans
        print(f"shirket_kassa_balans ==> {shirket_kassa_balans}")

        yekun_balans = float(mebleg) + float(shirket_kassa_balans)

        if(serializer.is_valid()):
            shirket_kassa.balans = yekun_balans
            shirket_kassa.save()
            serializer.save(shirket_kassa=shirket_kassa, medaxil_tarixi=medaxil_tarixi)
            return Response({"detail": f"{shirket_kassa.shirket} şirkətinə {mebleg} azn mədaxil edildi"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"detail": "Məbləği daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

def shirket_kassa_mexaric_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    mebleg = request.data.get("mebleg")
    print(f"mebleg ==> {mebleg}")

    qeyd = request.data.get("qeyd")
    print(f"qeyd ==> {qeyd}")

    shirket_kassa_id = request.data.get("shirket_kassa_id")
    print(f"shirket_kassa_id ==> {shirket_kassa_id}")
    shirket_kassa = get_object_or_404(ShirketKassa, pk=shirket_kassa_id)
    print(f"shirket_kassa ==> {shirket_kassa}")

    shirket_kassa_balans = shirket_kassa.balans
    print(f"shirket_kassa_balans ==> {shirket_kassa_balans}")

    mexaric_tarixi = request.data.get("mexaric_tarixi")
    print(f"mexaric_tarixi ==> {mexaric_tarixi}")

    if(mexaric_tarixi == ""):
        mexaric_tarixi = datetime.today().strftime('%Y-%m-%d')

    if(shirket_kassa_balans != 0):
        if(mebleg != ""):
            if(float(mebleg) <= float(shirket_kassa_balans)):
                yekun_balans = float(shirket_kassa_balans) - float(mebleg)
                if(serializer.is_valid()):
                    shirket_kassa.balans = yekun_balans
                    shirket_kassa.save()
                    serializer.save(shirket_kassa=shirket_kassa, mexaric_tarixi=mexaric_tarixi)
                    return Response({"detail": f"{shirket_kassa.shirket} şirkətindən {mebleg} azn məxaric edildi"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"detail": "Daxil etdiyiniz məbləğ şirkətinin balansıdan böyük ola bilməz"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Məbləği doğru daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Şirkətin balansı 0-dır"}, status=status.HTTP_400_BAD_REQUEST)

# *************** Ofis Kassa medaxil mexaric ***************

def ofis_kassa_medaxil_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    mebleg = request.data.get("mebleg")
    print(f"mebleg ==> {mebleg}")

    if(mebleg != ""):
        ofis_kassa_id = request.data.get("ofis_kassa_id")
        ofis_kassa = get_object_or_404(OfisKassa, pk=ofis_kassa_id)
        print(f"ofis_kassa ==> {ofis_kassa}")
        

        medaxil_tarixi = request.data.get("medaxil_tarixi")
        print(f"medaxil_tarixi ==> {medaxil_tarixi}")

        if(medaxil_tarixi == ""):
            medaxil_tarixi = datetime.today().strftime('%Y-%m-%d')

        qeyd = request.data.get("qeyd")
        print(f"qeyd ==> {qeyd}")

        ofis_kassa_balans = ofis_kassa.balans
        print(f"ofis_kassa_balans ==> {ofis_kassa_balans}")

        yekun_balans = float(mebleg) + float(ofis_kassa_balans)

        if(serializer.is_valid()):
            ofis_kassa.balans = yekun_balans
            ofis_kassa.save()
            serializer.save(ofis_kassa=ofis_kassa, medaxil_tarixi=medaxil_tarixi)
            return Response({"detail": f"{ofis_kassa.ofis} ofisinə {mebleg} azn mədaxil edildi"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"detail": "Məbləği daxil edin"}, status=status.HTTP_400_BAD_REQUEST)

def ofis_kassa_mexaric_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    mebleg = request.data.get("mebleg")
    print(f"mebleg ==> {mebleg}")

    qeyd = request.data.get("qeyd")
    print(f"qeyd ==> {qeyd}")

    ofis_kassa_id = request.data.get("ofis_kassa_id")
    ofis_kassa = get_object_or_404(OfisKassa, pk=ofis_kassa_id)
    print(f"ofis_kassa ==> {ofis_kassa}")

    ofis_kassa_balans = ofis_kassa.balans
    print(f"ofis_kassa_balans ==> {ofis_kassa_balans}")

    mexaric_tarixi = request.data.get("mexaric_tarixi")
    print(f"mexaric_tarixi ==> {mexaric_tarixi}")

    if(mexaric_tarixi == ""):
        mexaric_tarixi = datetime.today().strftime('%Y-%m-%d')

    if(ofis_kassa_balans != 0):
        if(mebleg != ""):
            if(float(mebleg) <= float(ofis_kassa_balans)):
                yekun_balans = float(ofis_kassa_balans) - float(mebleg)
                if(serializer.is_valid()):
                    ofis_kassa.balans = yekun_balans
                    ofis_kassa.save()
                    serializer.save(ofis_kassa=ofis_kassa, mexaric_tarixi=mexaric_tarixi)
                    return Response({"detail": f"{ofis_kassa.ofis} ofisindən {mebleg} azn məxaric edildi"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"detail": "Daxil etdiyiniz məbləğ ofisin balansıdan böyük ola bilməz"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Məbləği doğru daxil edin"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Ofisin balansı 0-dır"}, status=status.HTTP_400_BAD_REQUEST)