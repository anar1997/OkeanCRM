from django.contrib.auth import user_logged_in
from rest_framework import status, generics, permissions

from rest_framework.response import Response
from rest_framework import generics

from api.v1.all_serializers.account_serializers import (
    BolgeSerializer,
    RegisterSerializer,
    UserSerializer,
    MusteriSerializer,
    MusteriQeydlerSerializer,
    IsciSatisSayiSerializer,
    IsciStatusSerializer,
    PermissionSerializer,
    GroupSerializer
)

from account.models import (
    Bolge,
    IsciSatisSayi,
    MusteriQeydler, 
    User, 
    Musteri,
    IsciStatus
)

from django.contrib.auth.models import Permission, Group

from rest_framework_simplejwt.views import TokenObtainPairView

from api.v1.utils import (
    utils
)

from api.v1.permissions.account_permissions import permissions as account_permissions

from django_filters.rest_framework import DjangoFilterBackend

from api.v1.filters.account_filters.filters import (
    BolgeFilter,
    IsciStatusFilter,
    MusteriFilter,
    MusteriQeydlerFilter,
    UserFilter
)

# ********************************** permission model get post put delete **********************************
class PermissionListApi(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [account_permissions.PermissionModelPermissions]

# ********************************** permission group model get post put delete **********************************
class GroupListCreateApi(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [account_permissions.GroupPermissions]

class GroupDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [account_permissions.GroupPermissions]
# ********************************** user get post put delete **********************************


class RegisterApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if(serializer.is_valid()):
            isci_status = serializer.validated_data.get('isci_status')
            standart_status = IsciStatus.objects.get(status_adi="STANDART")
            print("isci_status=",isci_status)
            if isci_status == "" or isci_status == None:
                if standart_status is not None:
                    serializer.save(isci_status=standart_status)
            else:
                serializer.save()
        return Response({"detail": "İşçi qeydiyyatdan keçirildi"}, status=status.HTTP_201_CREATED)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    permission_classes = [account_permissions.UserPermissions]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    permission_classes = [account_permissions.UserPermissions]

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({"detail": "İşçi qeyri-atkiv edildi"}, status=status.HTTP_200_OK)


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
    filter_backends = [DjangoFilterBackend]
    filterset_class = MusteriFilter
    permission_classes = [account_permissions.MusteriPermissions]


class MusteriDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musteri.objects.all()
    serializer_class = MusteriSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MusteriFilter
    permission_classes = [account_permissions.MusteriPermissions]

    def destroy(self, request, *args, **kwargs):
        musteri = self.get_object()
        musteri.is_active = False
        musteri.save()
        return Response({"detail": "Müştəri qeyri-atkiv edildi"}, status=status.HTTP_200_OK)

# ********************************** musteriqeydlerin put delete post get **********************************

class MusteriQeydlerListCreateAPIView(generics.ListCreateAPIView):
    queryset = MusteriQeydler.objects.all()
    serializer_class = MusteriQeydlerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MusteriQeydlerFilter
    permission_classes = [account_permissions.MusteriQeydlerPermissions]


class MusteriQeydlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MusteriQeydler.objects.all()
    serializer_class = MusteriQeydlerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MusteriQeydlerFilter
    permission_classes = [account_permissions.MusteriQeydlerPermissions]

# ********************************** bolge put delete post get **********************************

class BolgeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bolge.objects.all()
    serializer_class = BolgeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BolgeFilter
    permission_classes = [account_permissions.BolgePermissions]


class BolgeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bolge.objects.all()
    serializer_class = BolgeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BolgeFilter
    permission_classes = [account_permissions.BolgePermissions]


# ********************************** isci satis sayi put delete post get **********************************

class IsciSatisSayiListCreateAPIView(generics.ListCreateAPIView):
    queryset = IsciSatisSayi.objects.all()
    serializer_class = IsciSatisSayiSerializer
    permission_classes = [account_permissions.IsciSatisSayiPermissions]


class IsciSatisSayiDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IsciSatisSayi.objects.all()
    serializer_class = IsciSatisSayiSerializer
    permission_classes = [account_permissions.IsciSatisSayiPermissions]


# ********************************** status put delete post get **********************************

class IsciStatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = IsciStatus.objects.all()
    serializer_class = IsciStatusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = IsciStatusFilter
    permission_classes = [account_permissions.IsciStatusPermissions]


class IsciStatusDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = IsciStatus.objects.all()
    serializer_class = IsciStatusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = IsciStatusFilter
    permission_classes = [account_permissions.IsciStatusPermissions]
