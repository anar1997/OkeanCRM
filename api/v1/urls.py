from django.conf import settings
from django.urls import path

from api.v1.all_views import account_views, company_views, muqavile_views, maas_views, gunler_views

from rest_framework_simplejwt.views import token_refresh
from django.conf.urls.static import static

urlpatterns=[  
    # account views *****************************************
    path('users/', account_views.UserList.as_view()),
    path('users/<int:pk>', account_views.UserDetail.as_view()),
    path('register/', account_views.RegisterApi.as_view()),
    path('permission-list/', account_views.PermissionListApi.as_view()),

    path('permission-group/', account_views.GroupListCreateApi.as_view()),
    path('permission-group/<int:pk>', account_views.GroupDetailApi.as_view()),

    path("login/", account_views.Login.as_view()),
    path("token-refresh/", token_refresh),

    path('musteriler/', account_views.MusteriListCreateAPIView.as_view(), name="musteriler"),
    path('musteriler/<int:pk>', account_views.MusteriDetailAPIView.as_view(), name="musteri_detail"),

    path('musteri-qeydler/', account_views.MusteriQeydlerListCreateAPIView.as_view(), name="musteri_qeydler"),
    path('musteri-qeydler/<int:pk>', account_views.MusteriQeydlerDetailAPIView.as_view(), name="musteri_qeydler_detail"),

    path('bolge/', account_views.BolgeListCreateAPIView.as_view(), name="bolge"),
    path('bolge/<int:pk>', account_views.BolgeDetailAPIView.as_view(), name="bolge_detail"),

    path('isci-satis-sayi/', account_views.IsciSatisSayiListCreateAPIView.as_view(), name="isci_satis_sayi"),
    path('isci-satis-sayi/<int:pk>', account_views.IsciSatisSayiDetailAPIView.as_view(), name="isci_satis_sayi"),

    path('isci-status/', account_views.IsciStatusListCreateAPIView.as_view(), name="isci_status"),
    path('isci-status/<int:pk>', account_views.IsciStatusDetailAPIView.as_view(), name="isci_status_detail"),

    # maas views *****************************************
    path('maas-goruntuleme/', maas_views.MaasGoruntulemeListCreateAPIView.as_view(), name="maas_goruntuleme"),
    path('maas-goruntuleme/<int:pk>', maas_views.MaasGoruntulemeDetailAPIView.as_view(), name="maas_goruntuleme_detail"),
    
    path('bonus/', maas_views.BonusListCreateAPIView.as_view(), name="bonus"),
    path('bonus/<int:pk>', maas_views.BonusDetailAPIView.as_view(), name="bonus_detail"),

    path('maas-ode/', maas_views.MaasOdeListCreateAPIView.as_view()),
    path('maas-ode/<int:pk>', maas_views.MaasOdeDetailAPIView.as_view()),
    
    path('avans/', maas_views.AvansListCreateAPIView.as_view(), name="avans"),
    path('avans/<int:pk>', maas_views.AvansDetailAPIView.as_view(), name="avans_detail"),
    
    path('kesinti/', maas_views.KesintiListCreateAPIView.as_view(), name="kesinti"),
    path('kesinti/<int:pk>', maas_views.KesintiDetailAPIView.as_view(), name="kesinti_detail"),

    path('office-leader-prim/', maas_views.OfficeLeaderPrimListCreateAPIView.as_view()),
    path('office-leader-prim/<int:pk>', maas_views.OfficeLeaderPrimDetailAPIView.as_view()),
    
    path('vanleader-prim/', maas_views.VanLeaderPrimListCreateAPIView.as_view()),
    path('vanleader-prim/<int:pk>', maas_views.VanLeaderPrimDetailAPIView.as_view()),

    path('canvasser-prim/', maas_views.CanvasserPrimListCreateAPIView.as_view()),
    path('canvasser-prim/<int:pk>', maas_views.CanvasserPrimDetailAPIView.as_view()),

    path('dealer-prim/', maas_views.DealerPrimListCreateAPIView.as_view()),
    path('dealer-prim/<int:pk>', maas_views.DealerPrimDetailAPIView.as_view()),

    path('kreditor-prim/', maas_views.KreditorPrimListCreateAPIView.as_view()),
    path('kreditor-prim/<int:pk>', maas_views.KreditorPrimDetailAPIView.as_view()),

    # gunler views *****************************************
    path('holding-gunler/', gunler_views.HoldingGunlerListCreateAPIView.as_view()),
    path('holding-gunler/<int:pk>', gunler_views.HoldingGunlerDetailAPIView.as_view()),
    path('holding-istisna-isci/', gunler_views.HoldingIstisnaIsciListCreateAPIView.as_view()),
    path('holding-istisna-isci/<int:pk>', gunler_views.HoldingIstisnaIsciDetailAPIView.as_view()),
    
    path('shirket-gunler/', gunler_views.ShirketGunlerListCreateAPIView.as_view()),
    path('shirket-gunler/<int:pk>', gunler_views.ShirketGunlerDetailAPIView.as_view()),
    path('shirket-istisna-isci/', gunler_views.ShirketIstisnaIsciListCreateAPIView.as_view()),
    path('shirket-istisna-isci/<int:pk>', gunler_views.ShirketIstisnaIsciDetailAPIView.as_view()),   

    path('ofis-gunler/', gunler_views.OfisGunlerListCreateAPIView.as_view()),
    path('ofis-gunler/<int:pk>', gunler_views.OfisGunlerDetailAPIView.as_view()),
    path('ofis-istisna-isci/', gunler_views.OfisIstisnaIsciListCreateAPIView.as_view()),
    path('ofis-istisna-isci/<int:pk>', gunler_views.OfisIstisnaIsciDetailAPIView.as_view()),
    
    path('shobe-gunler/', gunler_views.ShobeGunlerListCreateAPIView.as_view()),
    path('shobe-gunler/<int:pk>', gunler_views.ShobeGunlerDetailAPIView.as_view()),
    path('shobe-istisna-isci/', gunler_views.ShobeIstisnaIsciListCreateAPIView.as_view()),
    path('shobe-istisna-isci/<int:pk>', gunler_views.ShobeIstisnaIsciDetailAPIView.as_view()),

    path('komanda-gunler/', gunler_views.KomandaGunlerListCreateAPIView.as_view()),
    path('komanda-gunler/<int:pk>', gunler_views.KomandaGunlerDetailAPIView.as_view()),
    path('komanda-istisna-isci/', gunler_views.KomandaIstisnaIsciListCreateAPIView.as_view()),
    path('komanda-istisna-isci/<int:pk>', gunler_views.KomandaIstisnaIsciDetailAPIView.as_view()),
    
    path('vezife-gunler/', gunler_views.VezifeGunlerListCreateAPIView.as_view()),
    path('vezife-gunler/<int:pk>', gunler_views.VezifeGunlerDetailAPIView.as_view()),
    path('vezife-istisna-isci/', gunler_views.VezifeIstisnaIsciListCreateAPIView.as_view()),
    path('vezife-istisna-isci/<int:pk>', gunler_views.VezifeIstisnaIsciDetailAPIView.as_view()),

    path('isci-gunler/', gunler_views.IsciGunlerListCreateAPIView.as_view()),
    path('isci-gunler/<int:pk>', gunler_views.IsciGunlerDetailAPIView.as_view()),

    path('isci-gelib-getme-vaxtlari/', gunler_views.IsciGelibGetmeVaxtlariListCreateAPIView.as_view()),
    path('isci-gelib-getme-vaxtlari/<int:pk>', gunler_views.IsciGelibGetmeVaxtlariDetailAPIView.as_view()),

    # company views *****************************************
    path('muqavile-kreditor/', company_views.MuqavileKreditorListCreateAPIView.as_view()),
    path('muqavile-kreditor/<int:pk>', company_views.MuqavileKreditorDetailAPIView.as_view()),
    
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

    path('servis-odeme/', muqavile_views.ServisOdemeListCreateAPIView.as_view()),
    path('servis-odeme/<int:pk>', muqavile_views.ServisOdemeDetailAPIView.as_view()),

    path('stok/', muqavile_views.StokListCreateAPIView.as_view(), name="stok"),
    path('stok/<int:pk>', muqavile_views.StokDetailAPIView.as_view(), name="stok_detail"),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
