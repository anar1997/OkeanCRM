from django.contrib.auth import user_logged_in
from rest_framework import status, generics

from rest_framework.response import Response
from rest_framework import generics

from api.v1.all_serializers.account_serializers import (
    BolgeSerializer,
    RegisterSerializer,
    UserSerializer,
    MusteriSerializer,
    MusteriQeydlerSerializer,
    MaasSerializer,
    BonusSerializer,
    IsciSatisSayiSerializer
)

from account.models import (
    Bolge,
    IsciSatisSayi,
    MusteriQeydler, 
    User, 
    Musteri,
    Maas,
    Bonus,
)

from rest_framework_simplejwt.views import TokenObtainPairView

from api.v1.utils import (
    utils
)



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

        acces_token = utils.jwt_decode_handler(data.get("access"))

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

# ********************************** bolge put delete post get **********************************

class BolgeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bolge.objects.all()
    serializer_class = BolgeSerializer


class BolgeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bolge.objects.all()
    serializer_class = BolgeSerializer


# ********************************** isci satis sayi put delete post get **********************************

class IsciSatisSayiListCreateAPIView(generics.ListCreateAPIView):
    queryset = IsciSatisSayi.objects.all()
    serializer_class = IsciSatisSayiSerializer


class IsciSatisSayiDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IsciSatisSayi.objects.all()
    serializer_class = IsciSatisSayiSerializer
