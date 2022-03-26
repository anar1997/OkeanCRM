from django.contrib import admin
from . models import Avans,Kesinti,MaasGoruntuleme, VanLeaderPrim, DealerPrim
# Register your models here.

# class PrimAdmin(admin.ModelAdmin):
#     list_filter = [
#         "prim_status__status_adi",
#         'mehsul__mehsulun_adi',
#         'odenis_uslubu',
#         'vezife__vezife_adi'
#     ]
#     search_fields = (
#         "prim_status__status_adi",
#     )
# admin.site.register(Prim, PrimAdmin)

admin.site.register(MaasGoruntuleme)
admin.site.register(VanLeaderPrim)
admin.site.register(DealerPrim)


admin.site.register(Avans)
admin.site.register(Kesinti)
