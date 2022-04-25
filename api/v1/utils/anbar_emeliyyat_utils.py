from rest_framework import status
from rest_framework.response import Response

from mehsullar.models import (
    Anbar, 
    Mehsullar, 
    Stok
)
from rest_framework.generics import get_object_or_404

def emeliyyat_create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    # try:
    if serializer.is_valid():
        gonderen = request.data.get("gonderen_id")
        print(f"Gonderen id ==> {gonderen}")
        gonderen_anbar = get_object_or_404(Anbar, pk=gonderen)
        print(f"Gonderen anbar ==> {gonderen_anbar}")
        qebul_eden_id = request.data.get("qebul_eden_id")
        print(f"qebul_eden id ==> {qebul_eden_id}")
        qebul_eden = get_object_or_404(Anbar, pk=qebul_eden_id)
        print(f"qebul_eden anbar ==> {qebul_eden}")

        gonderilen_mehsul_id = request.data.get("gonderilen_mehsul_id")
        print(f"Gonderilen mehsul id ==> {gonderilen_mehsul_id}")
        gonderilen_mehsul = get_object_or_404(Mehsullar, pk=gonderilen_mehsul_id)
        print(f"Gonderilen mehsul ==> {gonderilen_mehsul}")
        say = request.data.get("mehsulun_sayi")
        print(f"say ==> {say}")

        qeyd = request.data.get("qeyd")
        print(f"qeyd ==> {qeyd}")


        stok1 = get_object_or_404(Stok, anbar=gonderen_anbar, mehsul=gonderilen_mehsul)
        if stok1 == None:
            return Response({"detail": "Göndərən anbarda məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
        print(f"Stok1 ==> {stok1}")
        print(f"stok1.say ==> {stok1.say}")
        if (say > stok1.say):
            return Response({"detail": "Göndərən anbarda yetəri qədər məhsul yoxdur"}, status=status.HTTP_404_NOT_FOUND)
        try:
            stok2 = get_object_or_404(Stok, anbar=qebul_eden, mehsul=gonderilen_mehsul)
            print(f"stok2 ==> {stok2}")
            if (stok1 == stok2):
                print("307 ISE DUSDU")
                return Response({"detail": "Göndərən və göndərilən anbar eynidir!"}, status=status.HTTP_404_NOT_FOUND)
            stok1.say = stok1.say - say
            stok1.save()
            print(f"stok1.say ==> {stok1.say}")
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
            return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
        except:
            stok2 = Stok.objects.create(anbar=qebul_eden, mehsul=gonderilen_mehsul, say=say)
            if (stok1 == stok2):
                print("BURA DAAAA ISE DUSDU")
                return Response({"detail": "Göndərən və göndərilən anbar eynidir!"}, status=status.HTTP_404_NOT_FOUND)
            stok2.save()
            stok1.say = stok1.say - say
            stok1.save()
            print(f"stok2.say ==> {stok2.say}")
            print("4 calisdi **********")
            if (serializer.is_valid()):
                serializer.save(gonderen=gonderen_anbar)
        return Response({"detail": "Əməliyyat uğurla yerinə yetirildi"}, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "Məlumatları doğru daxil edin"}, status=status.HTTP_404_NOT_FOUND)
