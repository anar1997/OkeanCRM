from django.contrib import admin

from gunler.models import (
    HoldingGunler,
    IsciGunler,
    KomandaGunler,
    OfisGunler,
    ShirketGunler,
    ShobeGunler,
    VezifeGunler,
    HoldingIstisnaIsci
)

# Register your models here.
admin.site.register(HoldingGunler)
admin.site.register(IsciGunler)
admin.site.register(KomandaGunler)
admin.site.register(OfisGunler)
admin.site.register(ShirketGunler)
admin.site.register(ShobeGunler)
admin.site.register(VezifeGunler)
admin.site.register(HoldingIstisnaIsci)


