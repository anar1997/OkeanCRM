from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework import generics, serializers

from rest_framework.views import APIView
from rest_framework import status

from rest_framework.response import Response
from rest_framework import generics, permissions, mixins
from  .serializers import AnbarSerializer, EmeliyyatSerializer, DatesSerializer, HediyyeSerializer, MehsullarSerializer, MerkezlerSerializer, MuqavileSerializer, MusteriQeydlerSerializer, ShirketSerializer, ShobeSerializer, UserSerializer, MusteriSerializer, VezifelerSerializer, AnbarQeydlerSerializer, RegisterSerializer
from mehsullar.models import Emeliyyat, Hediyye, Muqavile, Dates, Anbar, Mehsullar, AnbarQeydler
from account.models import MusteriQeydler, Shirket, Shobe, User, Musteri,  Vezifeler, Merkezler
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import jwt_decode_handler

#Register API
class RegisterApi(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = RegisterSerializer
    
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })



# class CreateUser(APIView):

#     # permission_classes = [AllowAny]

#     def post(self, request):

#         serializer = UserSerializer(data=request.data)

#         if serializer.is_valid():

#             serializer.save()

#             data = dict(serializer.data)
#             data.pop("password")
#             return Response(data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# user get post put delete
class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class Login(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)

        data = data.data

        acces_token = jwt_decode_handler(data.get("access"))

        if not User.objects.filter(id=acces_token.get("user_id")).last(): return Response({"error": True,"message": "No such a user"},status=status.HTTP_404_NOT_FOUND)
        
        user =  User.objects.filter(id=acces_token.get("user_id")).last()
        
        user_details = UserSerializer(user)

        data["user_details"] = user_details.data    
        return Response(data)


# musteri get post put delete
class MusteriListCreateAPIView(generics.ListCreateAPIView):
    queryset=Musteri.objects.all()
    serializer_class=MusteriSerializer
class MusteriDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Musteri.objects.all()
    serializer_class=MusteriSerializer

# muqavile get post put delete

class MuqavileListCreateAPIView(generics.ListCreateAPIView):
    queryset=Muqavile.objects.all()
    serializer_class=MuqavileSerializer
class MuqavileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Muqavile.objects.all()
    serializer_class=MuqavileSerializer

# date put get post delete

class DatesListCreateAPIView(generics.ListCreateAPIView):
    queryset=Dates.objects.all()
    serializer_class=DatesSerializer
class DatesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Dates.objects.all()
    serializer_class=DatesSerializer

# anbar put get post delete

class AnbarListCreateAPIView(generics.ListCreateAPIView):
    queryset=Anbar.objects.all()
    serializer_class=AnbarSerializer
class AnbarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Anbar.objects.all()
    serializer_class=AnbarSerializer

#  mehsullar put get post delete

class MehsullarListCreateAPIView(generics.ListCreateAPIView):
    queryset=Mehsullar.objects.all()
    serializer_class=MehsullarSerializer
class MehsullarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Mehsullar.objects.all()
    serializer_class=MehsullarSerializer

#  kateqoriyalar put delete post get

# class KateqoriyalarListCreateAPIView(generics.ListCreateAPIView):
#     queryset=Kateqoriyalar.objects.all()
#     serializer_class=KateqoriyalarSerializer
# class KateqoriyalarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Kateqoriyalar.objects.all()
#     serializer_class=KateqoriyalarSerializer

#  merkezler put delete post get
class MerkezlerListCreateAPIView(generics.ListCreateAPIView):
    queryset=Merkezler.objects.all()
    serializer_class=MerkezlerSerializer

class MerkezlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Merkezler.objects.all()
    serializer_class=MerkezlerSerializer
#  vezifeler put delete post get
class VezifelerListCreateAPIView(generics.ListCreateAPIView):
    queryset=Vezifeler.objects.all()
    serializer_class=VezifelerSerializer
class VezifelerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Vezifeler.objects.all()
    serializer_class=VezifelerSerializer

class AnbarQeydlerListCreateAPIView(generics.ListCreateAPIView):
    queryset=AnbarQeydler.objects.all()
    serializer_class=AnbarQeydlerSerializer
class AnbarQeydlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=AnbarQeydler.objects.all()
    serializer_class=AnbarQeydlerSerializer

# musteriqeydlerin put delete post get

class MusteriQeydlerListCreateAPIView(generics.ListCreateAPIView):
    queryset=MusteriQeydler.objects.all()
    serializer_class=MusteriQeydlerSerializer
class MusteriQeydlerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=MusteriQeydler.objects.all()
    serializer_class=MusteriQeydlerSerializer

# shirket put delete post get

class ShirketListCreateAPIView(generics.ListCreateAPIView):
    queryset=Shirket.objects.all()
    serializer_class=ShirketSerializer
class ShirketDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Shirket.objects.all()
    serializer_class=ShirketSerializer

# shobe put delete post get

class ShobeListCreateAPIView(generics.ListCreateAPIView):
    queryset=Shobe.objects.all()
    serializer_class=ShobeSerializer

class ShobeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Shobe.objects.all()
    serializer_class=ShobeSerializer

# emeliyyat put delete post get

class EmeliyyatListCreateAPIView(generics.ListCreateAPIView):
    queryset=Emeliyyat.objects.all()
    serializer_class=EmeliyyatSerializer
class EmeliyyatDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Emeliyyat.objects.all()
    serializer_class=EmeliyyatSerializer

# put delete post get

class HediyyeListCreateAPIView(generics.ListCreateAPIView):
    queryset=Hediyye.objects.all()
    serializer_class=HediyyeSerializer
class HediyyeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Hediyye.objects.all()
    serializer_class=HediyyeSerializer
