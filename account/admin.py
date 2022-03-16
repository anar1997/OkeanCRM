from django.contrib import admin
from account.models import (
    MusteriQeydler, 
    User, 
    Musteri, 
    Maas,
    Bonus,
    Bolge,
    IsciSatisSayi
)
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(User)
admin.site.register(IsciSatisSayi)

admin.site.register(Musteri)
admin.site.register(MusteriQeydler)

admin.site.register(Maas)
admin.site.register(Bonus)
admin.site.register(Bolge)



admin.site.register(Permission)