from django.urls import path, include
from django.urls.resolvers import URLPattern
from api import views

urlpatterns=[
    path('users/', views.UserListCreateAPIView.as_view(), name="users"),
    path('users/<int:pk>', views.UserDetailAPIView.as_view(), name="user_detail"),

    path('musteriler/', views.MusteriListCreateAPIView.as_view(), name="musteriler"),
    path('musteriler/<int:pk>', views.MusteriDetailAPIView.as_view(), name="musteri_detail"),
    path('muqavile/', views.MuqavileListCreateAPIView.as_view(), name="muqavile"),
    path('muqavile/<int:pk>', views.MuqavileDetailAPIView.as_view(), name="muqavile_detail"),
    path('dates/', views.DatesListCreateAPIView.as_view(), name="dates"),
    path('dates/<int:pk>', views.DatesDetailAPIView.as_view(), name="dates_detail"),
    path('anbar/', views.AnbarListCreateAPIView.as_view(), name="anbar"),
    path('anbar/<int:pk>', views.AnbarDetailAPIView.as_view(), name="anbar_detail"),
    path('mehsullar/', views.MehsullarListCreateAPIView.as_view(), name="mehsullar"),
    path('mehsullar/<int:pk>', views.MehsullarDetailAPIView.as_view(), name="mehsullar_detail"),
    # path('kateqoriyalar/', views.KateqoriyalarListCreateAPIView.as_view(), name="kateqoriyalar"),
    # path('kateqoriyalar/<int:pk>', views.KateqoriyalarDetailAPIView.as_view(), name="kateqoriyalar_detail"),
    path('merkezler/', views.MerkezlerListCreateAPIView.as_view(), name="merkezler"),
    path('merkezler/<int:pk>', views.MerkezlerDetailAPIView.as_view(), name="merkezler_detail"),
    path('vezifeler/', views.VezifelerListCreateAPIView.as_view(), name="vezifeler"),
    path('vezifeler/<int:pk>', views.VezifelerDetailAPIView.as_view(), name="vezifeler_detail"),
    path('anbar-qeydler/', views.AnbarQeydlerListCreateAPIView.as_view(), name="anbar_qeydler"),
    path('anbar-qeydler/<int:pk>', views.AnbarQeydlerDetailAPIView.as_view(), name="anbar_qeydler_detail"),
    path('musteri-qeydler/', views.MusteriQeydlerListCreateAPIView.as_view(), name="musteri_qeydler"),
    path('musteri-qeydler/<int:pk>', views.MusteriQeydlerDetailAPIView.as_view(), name="musteri_qeydler_detail"),
    path('shirket/', views.ShirketListCreateAPIView.as_view(), name="shirket"),
    path('shirket/<int:pk>', views.ShirketDetailAPIView.as_view(), name="shirket_detail"),
    path('shobe/', views.ShobeListCreateAPIView.as_view(), name="shobe"),
    path('shobe/<int:pk>', views.ShobeDetailAPIView.as_view(), name="shobe_detail"),
    path('emeliyyat/', views.EmeliyyatListCreateAPIView.as_view(), name="emeliyyat"),
    path('emeliyyat/<int:pk>', views.EmeliyyatDetailAPIView.as_view(), name="emeliyyat_detail"),
    path('hediyye/', views.HediyyeListCreateAPIView.as_view(), name="hediyye"),
    path('hediyye/<int:pk>', views.HediyyeDetailAPIView.as_view(), name="hediyye_detail"),
    # path('hediyye2/', views.Hediyye2ListCreateAPIView.as_view(), name="hediyye2"),
    # path('hediyye2/<int:pk>', views.Hediyye2DetailAPIView.as_view(), name="hediyye2_detail"),
    # path('hediyye3/', views.Hediyye3ListCreateAPIView.as_view(), name="hediyye3"),
    # path('hediyye3/<int:pk>', views.Hediyye3DetailAPIView.as_view(), name="hediyye3_detail"),


]


