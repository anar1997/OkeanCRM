from django.conf import settings
from django.urls import path
from api.v1 import views
from rest_framework_simplejwt.views import token_refresh
from django.conf.urls.static import static

urlpatterns=[
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('register/', views.RegisterApi.as_view()),

    path("login/", views.Login.as_view()),
    path("token-refresh/", token_refresh),

    path('musteriler/', views.MusteriListCreateAPIView.as_view(), name="musteriler"),
    path('musteriler/<int:pk>', views.MusteriDetailAPIView.as_view(), name="musteri_detail"),

    path('muqavile/', views.MuqavileListCreateAPIView.as_view(), name="muqavile"),
    path('muqavile/<int:pk>', views.MuqavileDetailAPIView.as_view(), name="muqavile_detail"),

    path('odemetarixleri/', views.OdemeTarixListCreateAPIView.as_view(), name="odemetarix"),
    path('odemetarixleri/<int:pk>', views.OdemeTarixDetailAPIView.as_view(), name="odemetarix_detail"),
    
    path('anbar/', views.AnbarListCreateAPIView.as_view(), name="anbar"),
    path('anbar/<int:pk>', views.AnbarDetailAPIView.as_view(), name="anbar_detail"),
    
    path('mehsullar/', views.MehsullarListCreateAPIView.as_view(), name="mehsullar"),
    path('mehsullar/<int:pk>', views.MehsullarDetailAPIView.as_view(), name="mehsullar_detail"),
    
    path('ofisler/', views.OfisListCreateAPIView.as_view(), name="ofisler"),
    path('ofisler/<int:pk>', views.OfisDetailAPIView.as_view(), name="ofisler_detail"),

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

    path('komanda/', views.KomandaListCreateAPIView.as_view(), name="komanda"),
    path('komanda/<int:pk>', views.KomandaDetailAPIView.as_view(), name="komanda_detail"),

    path('servis/', views.ServisListCreateAPIView.as_view(), name="servis"),
    path('servis/<int:pk>', views.ServisDetailAPIView.as_view(), name="servis_detail"),

    path('stok/', views.StokListCreateAPIView.as_view(), name="stok"),
    path('stok/<int:pk>', views.StokDetailAPIView.as_view(), name="stok_detail"),

    path('holding/', views.HoldingListCreateAPIView.as_view(), name="holding"),
    path('holding/<int:pk>', views.HoldingDetailAPIView.as_view(), name="holding_detail"),
    
    path('holding-kassa/', views.HoldingKassaListCreateAPIView.as_view(), name="holding_kassa"),
    path('holding-kassa/<int:pk>', views.HoldingKassaDetailAPIView.as_view(), name="holding_kassa_detail"),

    path('shirket-kassa/', views.ShirketKassaListCreateAPIView.as_view(), name="shirket_kassa"),
    path('shirket-kassa/<int:pk>', views.ShirketKassaDetailAPIView.as_view(), name="shirket_kassa_detail"),

    path('ofis-kassa/', views.OfisKassaListCreateAPIView.as_view(), name="ofis_kassa"),
    path('ofis-kassa/<int:pk>', views.OfisKassaDetailAPIView.as_view(), name="ofis_kassa_detail"),

    path('shirket-holding-transfer/', views.ShirketdenHoldingeTransferListCreateAPIView.as_view(), name="shirket_holding_transfer"),
    path('shirket-holding-transfer/<int:pk>', views.ShirketdenHoldingeTransferDetailAPIView.as_view(), name="shirket_holding_transfer_detail"),

    path('holding-shirket-transfer/', views.HoldingdenShirketlereTransferListCreateAPIView.as_view(), name="holding_shirket_transfer"),
    path('holding-shirket-transfer/<int:pk>', views.HoldingdenShirketlereTransferDetailAPIView.as_view(), name="holding_shirket_transfer_detail"),
    
    path('shirket-ofis-transfer/', views.ShirketdenOfislereTransferListCreateAPIView.as_view(), name="shirket_ofis_transfer"),
    path('shirket-ofis-transfer/<int:pk>', views.ShirketdenOfislereTransferDetailAPIView.as_view(), name="shirket_ofis_transfer_detail"),

    path('ofis-shirket-transfer/', views.OfisdenShirketeTransferListCreateAPIView.as_view(), name="ofis_shirket_transfer"),
    path('ofis-shirket-transfer/<int:pk>', views.OfisdenShirketeTransferDetailAPIView.as_view(), name="ofis_shirket_transfer_detail"),

    path('maas/', views.MaasListCreateAPIView.as_view(), name="maas"),
    path('maas/<int:pk>', views.MaasDetailAPIView.as_view(), name="maas_detail"),

    path('bonus/', views.BonusListCreateAPIView.as_view(), name="bonus"),
    path('bonus/<int:pk>', views.BonusDetailAPIView.as_view(), name="bonus_detail"),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
