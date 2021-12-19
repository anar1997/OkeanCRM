from django.urls import path, include
from django.urls.resolvers import URLPattern
from api import views

urlpatterns=[
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
    path('kateqoriyalar/', views.KateqoriyalarListCreateAPIView.as_view(), name="kateqoriyalar"),
    path('kateqoriyalar/<int:pk>', views.KateqoriyalarDetailAPIView.as_view(), name="kateqoriyalar_detail"),
    path('merkezler/', views.MerkezlerListCreateAPIView.as_view(), name="merkezler"),
    path('merkezler/<int:pk>', views.MerkezlerDetailAPIView.as_view(), name="merkezler_detail"),
    path('vezifeler/', views.VezifelerListCreateAPIView.as_view(), name="vezifeler"),
    path('vezifeler/<int:pk>', views.VezifelerDetailAPIView.as_view(), name="vezifeler_detail"),
    path('qeydler/', views.QeydlerListCreateAPIView.as_view(), name="qeydler"),
    path('qeydler/<int:pk>', views.QeydlerDetailAPIView.as_view(), name="qeydler_detail"),
    
]


