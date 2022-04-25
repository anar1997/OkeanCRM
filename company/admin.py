from django.contrib import admin

from company.models import (
    Holding, 
    HoldingKassa, 
    HoldingdenShirketlereTransfer, 
    Komanda, 
    Ofis, 
    OfisKassa, 
    OfisdenShirketeTransfer, 
    Shirket, 
    ShirketKassa, 
    ShirketdenHoldingeTransfer, 
    ShirketdenOfislereTransfer, 
    Shobe, 
    Vezifeler,
    HoldingKassaMedaxil,
    HoldingKassaMexaric,
    OfisKassaMedaxil,
    OfisKassaMexaric,
    ShirketKassaMedaxil,
    ShirketKassaMexaric
) 

# Register your models here.
admin.site.register(Vezifeler)
admin.site.register(Ofis)
admin.site.register(Shirket)
admin.site.register(Shobe)

admin.site.register(Komanda)
admin.site.register(Holding)
admin.site.register(ShirketKassa)
admin.site.register(OfisKassa)
admin.site.register(HoldingKassa)
admin.site.register(HoldingdenShirketlereTransfer)
admin.site.register(OfisdenShirketeTransfer)
admin.site.register(ShirketdenHoldingeTransfer)
admin.site.register(ShirketdenOfislereTransfer)

admin.site.register(HoldingKassaMedaxil)
admin.site.register(HoldingKassaMexaric)
admin.site.register(OfisKassaMedaxil)
admin.site.register(OfisKassaMexaric)
admin.site.register(ShirketKassaMedaxil)
admin.site.register(ShirketKassaMexaric)
