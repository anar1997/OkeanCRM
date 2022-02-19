from django.contrib import admin
from .models import Anbar,Mehsullar, AnbarQeydler, Emeliyyat, Muqavile, OdemeTarix, Servis, Stok

# Register your models here.
admin.site.register(Mehsullar)
admin.site.register(Anbar)
admin.site.register(AnbarQeydler)
admin.site.register(Emeliyyat)
admin.site.register(Muqavile)
admin.site.register(OdemeTarix)
admin.site.register(Servis)
admin.site.register(Stok)