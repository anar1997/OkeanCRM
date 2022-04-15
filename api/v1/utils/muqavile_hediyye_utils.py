from rest_framework import status

from rest_framework.response import Response

from mehsullar.models import ( 
    Muqavile,  
    Anbar, 
    Mehsullar,
    Stok
)

from api.v1.utils.muqavile_utils import stok_mehsul_ciximi, stok_mehsul_elave
from rest_framework.generics import get_object_or_404


def muqavile_hediyye_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    mehsul_id = request.data.get("mehsul_id")
    muqavile_id = request.data.get("muqavile_id")
    print(f"hediyye mehsul_id ==> {mehsul_id}")
    print(f"hediyye muqavile_id ==> {muqavile_id}")

    try:
        mehsul = get_object_or_404(Mehsullar, pk=mehsul_id)
        print(f"hediyye mehsul ==> {mehsul}")
        try:
            muqavile = get_object_or_404(Muqavile, pk=muqavile_id)
            print(f"hediyye muqavile ==> {muqavile}")
            vanleader = muqavile.vanleader
            print(f"vanleader ==> {vanleader}")
            try:
                anbar = get_object_or_404(Anbar, ofis=vanleader.ofis)
                print(f"anbar ==> {anbar}")
            except:
                return Response({"detail": "Anbar tapılmadı"}, status=status.HTTP_400_BAD_REQUEST)
            try:
                stok = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul)
                print(f"stok ==> {stok}")
            except:
                return Response({"detail": "Stokda məhsul qalmayıb"}, status=status.HTTP_404_NOT_FOUND)
            stok_mehsul_ciximi(stok, 1)
            return Response({"detail": f"{muqavile} müqaviləsinə {mehsul} hədiyyə edildi"}, status=status.HTTP_200_OK)
        except:
            return Response({"detail": "Bu adlı müqavilə tapılmadı"}, status=status.HTTP_400_BAD_REQUEST)

    except:
        return Response({"detail": "Bu adlı məhsul tapılmadı"}, status=status.HTTP_400_BAD_REQUEST)

def muqavile_hediyye_destroy(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    muqavile_hediyye =  self.get_object()

    mehsul = muqavile_hediyye.mehsul
    muqavile = muqavile_hediyye.muqavile
    vanleader = muqavile.vanleader
    print(f"vanleader ==> {vanleader}")
    anbar = get_object_or_404(Anbar, ofis=muqavile.ofis)
    print(f"anbar ==> {anbar}")
    try:
        stok = get_object_or_404(Stok, anbar=anbar, mehsul=mehsul)
        print(f"stok ==> {stok}")
        stok_mehsul_elave(stok, 1)
        self.perform_destroy(muqavile_hediyye)
        return Response({"detail": "Hədiyyə stok-a geri qaytarıldı"}, status=status.HTTP_200_OK)
    except:
        stok = Stok.objects.create(anbar=anbar, mehsul=mehsul, say=1)
        stok.save()
        self.perform_destroy(muqavile_hediyye)
        return Response({"detail": "Hədiyyə stok-a geri qaytarıldı"}, status=status.HTTP_200_OK)