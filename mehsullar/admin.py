from django.contrib import admin
from .models import Anbar,Kateqoriyalar,Mehsullar, AnbarQeydler, Emeliyyat, Muqavile, Dates
# Register your models here.
admin.site.register(Mehsullar)
admin.site.register(Kateqoriyalar)
admin.site.register(Anbar)
admin.site.register(AnbarQeydler)
admin.site.register(Emeliyyat)
admin.site.register(Muqavile)
admin.site.register(Dates)


