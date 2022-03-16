from django.conf import settings
from django.urls import path

from api.v1.all_views import account_views, company_views, muqavile_views

from rest_framework_simplejwt.views import token_refresh
from django.conf.urls.static import static

urlpatterns=[  
    # account views *****************************************
    path('users/', account_views.UserList.as_view()),
    path('users/<int:pk>', account_views.UserDetail.as_view()),
    path('register/', account_views.RegisterApi.as_view()),

    path("login/", account_views.Login.as_view()),
    path("token-refresh/", token_refresh),

    path('musteriler/', account_views.MusteriListCreateAPIView.as_view(), name="musteriler"),
    path('musteriler/<int:pk>', account_views.MusteriDetailAPIView.as_view(), name="musteri_detail"),

    path('musteri-qeydler/', account_views.MusteriQeydlerListCreateAPIView.as_view(), name="musteri_qeydler"),
    path('musteri-qeydler/<int:pk>', account_views.MusteriQeydlerDetailAPIView.as_view(), name="musteri_qeydler_detail"),

    path('maas/', account_views.MaasListCreateAPIView.as_view(), name="maas"),
    path('maas/<int:pk>', account_views.MaasDetailAPIView.as_view(), name="maas_detail"),

    path('bonus/', account_views.BonusListCreateAPIView.as_view(), name="bonus"),
    path('bonus/<int:pk>', account_views.BonusDetailAPIView.as_view(), name="bonus_detail"),

    path('bolge/', account_views.BolgeListCreateAPIView.as_view(), name="bolge"),
    path('bolge/<int:pk>', account_views.BolgeDetailAPIView.as_view(), name="bolge_detail"),

    path('isci-satis-sayi/', account_views.IsciSatisSayiListCreateAPIView.as_view(), name="isci_satis_sayi"),
    path('isci-satis-sayi/<int:pk>', account_views.IsciSatisSayiDetailAPIView.as_view(), name="isci_satis_sayi"),

    # company views *****************************************
    path('komanda/', company_views.KomandaListCreateAPIView.as_view(), name="komanda"),
    path('komanda/<int:pk>', company_views.KomandaDetailAPIView.as_view(), name="komanda_detail"),

    path('ofisler/', company_views.OfisListCreateAPIView.as_view(), name="ofisler"),
    path('ofisler/<int:pk>', company_views.OfisDetailAPIView.as_view(), name="ofisler_detail"),

    path('vezifeler/', company_views.VezifelerListCreateAPIView.as_view(), name="vezifeler"),
    path('vezifeler/<int:pk>', company_views.VezifelerDetailAPIView.as_view(), name="vezifeler_detail"),

    path('shirket/', company_views.ShirketListCreateAPIView.as_view(), name="shirket"),
    path('shirket/<int:pk>', company_views.ShirketDetailAPIView.as_view(), name="shirket_detail"),

    path('shobe/', company_views.ShobeListCreateAPIView.as_view(), name="shobe"),
    path('shobe/<int:pk>', company_views.ShobeDetailAPIView.as_view(), name="shobe_detail"),

    path('holding/', company_views.HoldingListCreateAPIView.as_view(), name="holding"),
    path('holding/<int:pk>', company_views.HoldingDetailAPIView.as_view(), name="holding_detail"),

    path('holding-kassa/', company_views.HoldingKassaListCreateAPIView.as_view(), name="holding_kassa"),
    path('holding-kassa/<int:pk>', company_views.HoldingKassaDetailAPIView.as_view(), name="holding_kassa_detail"),

    path('shirket-kassa/', company_views.ShirketKassaListCreateAPIView.as_view(), name="shirket_kassa"),
    path('shirket-kassa/<int:pk>', company_views.ShirketKassaDetailAPIView.as_view(), name="shirket_kassa_detail"),

    path('ofis-kassa/', company_views.OfisKassaListCreateAPIView.as_view(), name="ofis_kassa"),
    path('ofis-kassa/<int:pk>', company_views.OfisKassaDetailAPIView.as_view(), name="ofis_kassa_detail"),

    path('shirket-holding-transfer/', company_views.ShirketdenHoldingeTransferListCreateAPIView.as_view(), name="shirket_holding_transfer"),
    path('shirket-holding-transfer/<int:pk>', company_views.ShirketdenHoldingeTransferDetailAPIView.as_view(), name="shirket_holding_transfer_detail"),

    path('holding-shirket-transfer/', company_views.HoldingdenShirketlereTransferListCreateAPIView.as_view(), name="holding_shirket_transfer"),
    path('holding-shirket-transfer/<int:pk>', company_views.HoldingdenShirketlereTransferDetailAPIView.as_view(), name="holding_shirket_transfer_detail"),
    
    path('shirket-ofis-transfer/', company_views.ShirketdenOfislereTransferListCreateAPIView.as_view(), name="shirket_ofis_transfer"),
    path('shirket-ofis-transfer/<int:pk>', company_views.ShirketdenOfislereTransferDetailAPIView.as_view(), name="shirket_ofis_transfer_detail"),

    path('ofis-shirket-transfer/', company_views.OfisdenShirketeTransferListCreateAPIView.as_view(), name="ofis_shirket_transfer"),
    path('ofis-shirket-transfer/<int:pk>', company_views.OfisdenShirketeTransferDetailAPIView.as_view(), name="ofis_shirket_transfer_detail"),

    path('holding-kassa-medaxil/', company_views.HoldingKassaMedaxilListCreateAPIView.as_view(), name="holding_kassa_medaxil"),
    path('holding-kassa-medaxil/<int:pk>', company_views.HoldingKassaMedaxilDetailAPIView.as_view(), name="holding_kassa_medaxil_detail"),

    path('holding-kassa-mexaric/', company_views.HoldingKassaMexaricListCreateAPIView.as_view(), name="holding_kassa_mexaric"),
    path('holding-kassa-mexaric/<int:pk>', company_views.HoldingKassaMexaricDetailAPIView.as_view(), name="holding_kassa_mexaric_detail"),

    path('shirket-kassa-medaxil/', company_views.ShirketKassaMedaxilListCreateAPIView.as_view(), name="shirket_kassa_medaxil"),
    path('shirket-kassa-medaxil/<int:pk>', company_views.ShirketKassaMedaxilDetailAPIView.as_view(), name="shirket_kassa_medaxil_detail"),

    path('shirket-kassa-mexaric/', company_views.ShirketKassaMexaricListCreateAPIView.as_view(), name="shirket_kassa_mexaric"),
    path('shirket-kassa-mexaric/<int:pk>', company_views.ShirketKassaMexaricDetailAPIView.as_view(), name="shirket_kassa_mexaric_detail"),

    path('ofis-kassa-medaxil/', company_views.OfisKassaMedaxilListCreateAPIView.as_view(), name="ofis_kassa_medaxil"),
    path('ofis-kassa-medaxil/<int:pk>', company_views.OfisKassaMedaxilDetailAPIView.as_view(), name="ofis_kassa_medaxil_detail"),

    path('ofis-kassa-mexaric/', company_views.OfisKassaMexaricListCreateAPIView.as_view(), name="ofis_kassa_mexaric"),
    path('ofis-kassa-mexaric/<int:pk>', company_views.OfisKassaMexaricDetailAPIView.as_view(), name="ofis_kassa_mexaric_detail"),

    # muqavile views *****************************************
    path('muqavile/', muqavile_views.MuqavileListCreateAPIView.as_view(), name="muqavile"),
    path('muqavile/<int:pk>', muqavile_views.MuqavileDetailAPIView.as_view(), name="muqavile_detail"),

    path('odemetarixleri/', muqavile_views.OdemeTarixListCreateAPIView.as_view(), name="odemetarix"),
    path('odemetarixleri/<int:pk>', muqavile_views.OdemeTarixDetailAPIView.as_view(), name="odemetarix_detail"),
    
    path('anbar/', muqavile_views.AnbarListCreateAPIView.as_view(), name="anbar"),
    path('anbar/<int:pk>', muqavile_views.AnbarDetailAPIView.as_view(), name="anbar_detail"),
    
    path('mehsullar/', muqavile_views.MehsullarListCreateAPIView.as_view(), name="mehsullar"),
    path('mehsullar/<int:pk>', muqavile_views.MehsullarDetailAPIView.as_view(), name="mehsullar_detail"),  
    
    path('anbar-qeydler/', muqavile_views.AnbarQeydlerListCreateAPIView.as_view(), name="anbar_qeydler"),
    path('anbar-qeydler/<int:pk>', muqavile_views.AnbarQeydlerDetailAPIView.as_view(), name="anbar_qeydler_detail"),
     
    path('emeliyyat/', muqavile_views.EmeliyyatListCreateAPIView.as_view(), name="emeliyyat"),
    path('emeliyyat/<int:pk>', muqavile_views.EmeliyyatDetailAPIView.as_view(), name="emeliyyat_detail"),
    
    path('hediyye/', muqavile_views.MuqavileHediyyeListCreateAPIView.as_view(), name="hediyye"),
    path('hediyye/<int:pk>', muqavile_views.MuqavileHediyyeDetailAPIView.as_view(), name="hediyye_detail"),

    path('servis/', muqavile_views.ServisListCreateAPIView.as_view(), name="servis"),
    path('servis/<int:pk>', muqavile_views.ServisDetailAPIView.as_view(), name="servis_detail"),

    path('stok/', muqavile_views.StokListCreateAPIView.as_view(), name="stok"),
    path('stok/<int:pk>', muqavile_views.StokDetailAPIView.as_view(), name="stok_detail"),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
