from rest_framework import status

from rest_framework.response import Response

from mehsullar.models import ( 
    Muqavile,  
    Anbar, 
    Mehsullar,
    Stok
)

from rest_framework_simplejwt.views import TokenObtainPairView
from api.v1.utils.muqavile_utils import stok_mehsul_ciximi
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