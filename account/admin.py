from django.contrib import admin
from account.models import (
    MusteriQeydler, 
    Shirket, 
    Shobe, 
    User, 
    Musteri, 
    Vezifeler, 
    Ofis, 
    Komanda, 
    Holding, 
    ShirketKassa, 
    OfisKassa,
    HoldingKassa,
    HoldingdenShirketlereTransfer,
    OfisdenShirketeTransfer,
    ShirketdenHoldingeTransfer,
    ShirketdenOfislereTransfer,
    Maas,
    Bonus
)
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(User)
admin.site.register(Vezifeler)
admin.site.register(Ofis)
admin.site.register(Shirket)
admin.site.register(Shobe)
admin.site.register(Musteri)
admin.site.register(MusteriQeydler)
admin.site.register(Komanda)
admin.site.register(Holding)
admin.site.register(ShirketKassa)
admin.site.register(OfisKassa)
admin.site.register(HoldingKassa)
admin.site.register(HoldingdenShirketlereTransfer)
admin.site.register(OfisdenShirketeTransfer)
admin.site.register(ShirketdenHoldingeTransfer)
admin.site.register(ShirketdenOfislereTransfer)
admin.site.register(Maas)
admin.site.register(Bonus)


admin.site.register(Permission)