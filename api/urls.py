from django.conf import settings
from django.urls import path
from api import views
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

    path('dates/', views.DatesListCreateAPIView.as_view(), name="dates"),
    path('dates/<int:pk>', views.DatesDetailAPIView.as_view(), name="dates_detail"),
    
    path('anbar/', views.AnbarListCreateAPIView.as_view(), name="anbar"),
    path('anbar/<int:pk>', views.AnbarDetailAPIView.as_view(), name="anbar_detail"),
    
    path('mehsullar/', views.MehsullarListCreateAPIView.as_view(), name="mehsullar"),
    path('mehsullar/<int:pk>', views.MehsullarDetailAPIView.as_view(), name="mehsullar_detail"),
    
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

    path('komanda/', views.KomandaListCreateAPIView.as_view(), name="komanda"),
    path('komanda/<int:pk>', views.KomandaDetailAPIView.as_view(), name="komanda_detail"),

    path('servis/', views.ServisListCreateAPIView.as_view(), name="servis"),
    path('servis/<int:pk>', views.ServisDetailAPIView.as_view(), name="servis_detail"),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
