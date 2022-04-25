from django.contrib import admin
from . models import Avans, Kesinti, Bonus, MaasGoruntuleme, VanLeaderPrim, DealerPrim, OfficeLeaderPrim, CanvasserPrim, KreditorPrim
# Register your models here.

admin.site.register(MaasGoruntuleme)

admin.site.register(OfficeLeaderPrim)
admin.site.register(VanLeaderPrim)
admin.site.register(DealerPrim)
admin.site.register(CanvasserPrim)

admin.site.register(Bonus)
admin.site.register(Avans)
admin.site.register(Kesinti)
admin.site.register(KreditorPrim)