from rest_framework import status

from rest_framework.response import Response

from mehsullar.models import (
    Anbar,
    Mehsullar,
    Stok
)

from rest_framework.generics import get_object_or_404


def stok_update(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    mehsul_id = int(request.POST["mehsul_id"])
    say = int(request.POST["say"])
    anbar_id = int(request.POST["anbar_id"])
    print(f"mehsul id ==> {mehsul_id}")
    print(f"anbar id ==> {anbar_id}")
    print(f"say ==> {say}")

    mehsul = get_object_or_404(Mehsullar, pk=mehsul_id)
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
